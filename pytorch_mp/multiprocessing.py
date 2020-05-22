#
# See https://docs.python.org/3.1/library/multiprocessing.html for more.
#
# This sample is a follow-up on this discussion:
# https://discuss.pytorch.org/t/using-torch-tensor-over-multiprocessing-queue-process-fails/2847/2
#
# Might want to get torch, e.g.
#
# $ conda install pytorch torchvision cudatoolkit=10.2 -c pytorch
# 
# To run(on Ubuntu): 
#
# $ python3 multiprocessing.py 
# one more process added to producers list  0
#    extractor_worker() started...
# one more process added to producers list  1
#    extractor_worker() started...
# one more process added to producers list  2
# one more process added to producers list  3
# one more process added to producers list  4
# getting worker result
#    extractor_worker() started...
#    extractor_worker() started...
#    extractor_worker() started...
# got result, appending to the result_arrays
# getting worker result
# ended worker, ended_workers 1
# getting worker result
# got result, appending to the result_arrays
# getting worker result
# ended worker, ended_workers 2
# getting worker result
# got result, appending to the result_arrays
# getting worker result
# ended worker, ended_workers 3
# getting worker result
# got result, appending to the result_arrays
# getting worker result
# ended worker, ended_workers 4
# getting worker result
# got result, appending to the result_arrays
# getting worker result
# ended worker, ended_workers 5

import multiprocessing as mp
import torch

mytotal_workers = 10
done = mp.Event()

def extractor_worker(done_queue):
    print("   extractor_worker() started...")
    done_queue.put(torch.Tensor(10,10))
    done_queue.put(None)
    done.wait()

producers = []
done_queue = mp.Queue()
for i in range(0, mytotal_workers):
    process = mp.Process(target=extractor_worker,
                         args=(done_queue,))
    process.start()
    producers.append(process)
    print("one more process added to producers list ", i)

result_arrays = []
nb_ended_workers = 0
while nb_ended_workers != mytotal_workers:
    print("getting worker result")
    worker_result = done_queue.get()
    if worker_result is None:
        nb_ended_workers += 1
        print("ended worker, ended_workers", nb_ended_workers)
    else:
        print("got result, appending to the result_arrays")
        result_arrays.append(worker_result)
done.set()
