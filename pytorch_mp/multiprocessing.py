#
# This sample is a follow-up on this discussion:
# https://discuss.pytorch.org/t/using-torch-tensor-over-multiprocessing-queue-process-fails/2847/2
#
# Might want to get torch, e.g.
#
# $ conda install pytorch pyvision cudatoolkit=10.2 -c pytorch
# 
# To run: 
#
# $ python multiprocessing.py
#

import multiprocessing as mp
import torch

done = mp.Event()

def extractor_worker(done_queue):
    print("extractor_worker()")
    done_queue.put(torch.Tensor(10,10))
    done_queue.put(None)
    done.wait()

producers = []
done_queue = mp.Queue()
for i in range(0, 1):
    process = mp.Process(target=extractor_worker,
                         args=(done_queue,))
    process.start()
    producers.append(process)
    print("one more process added to producers list")

result_arrays = []
nb_ended_workers = 0
while nb_ended_workers != 1:
    print("getting worker result")
    worker_result = done_queue.get()
    if worker_result is None:
        print("ended worker")
        nb_ended_workers += 1
    else:
        print("got result, appending to the result_arrays")
        result_arrays.append(worker_result)
done.set()
