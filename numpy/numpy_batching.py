import numpy as np


# Generate (using yield) batches for RNN training for text prediction
# (we overlap the y with one character at the end).
def generate_batches(orig_sample_text, samp_per_batch=5, seq_len=10):
    print(f"samp_per_batch: {samp_per_batch}")
    print(f"seq_len: {seq_len}")
    
    char_per_batch = samp_per_batch * seq_len
    print(f"char_per_batch: {char_per_batch}")
    num_batches_avail = int(len(orig_sample_text)/char_per_batch)
    print(f"num_batches_avail: {num_batches_avail}")

    # dropping the extra
    sample_text = orig_sample_text[:num_batches_avail * char_per_batch]
    print(f"dropping uneven: {sample_text}")

    sample_text = sample_text.reshape((samp_per_batch, -1))
    print(f"reshaped in batch-sized rows: {sample_text}")

    for n in range(0, sample_text.shape[1], seq_len):
        x = sample_text[:, n:n+seq_len]
        y = np.zeros_like(x)
        # good to have, because index might be messed up at the end
        try:
            y[:, :-1] = x[:, 1:]
            y[:, -1] = sample_text[:, n+seq_len]
            print("added the next in line")
        except:
            y[:, :-1] = x[:, 1:]
            #y[:, -1] = sample_text[:, 0]
            y[:, -1] = sample_text[:, n]
            print("added the index 0 instead of the next in line")
        yield x, y


sample_feed = np.arange(24)
print(sample_feed)
batch_generator = generate_batches(sample_feed, 3, 4)

for i in np.arange(2):
    x, y = next(batch_generator)
    print(f"batch number {i}")
    print("x:", x)
    print("y:", y)
