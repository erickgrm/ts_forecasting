import tensorflow as tf
import numpy as np
import copy

#rnn seq2seq
def window_dataset(series, window_size, batch_size=32, shuffle_buffer_size=1000):
    dataset = tf.data.Dataset.from_tensor_slices(series)
    dataset = dataset.window(window_size + 1, shift=1, drop_remainder=True)
    dataset = dataset.flat_map(lambda window: window.batch(window_size + 1))
    dataset = dataset.shuffle(shuffle_buffer_size)
    dataset = dataset.map(lambda window: (window[:-1], window[-1]))
    dataset = dataset.batch(batch_size).prefetch(1)
    return dataset

# lstm_conv 
def seq2seq_window_dataset(series, window_size, batch_size=32, shuffle_buffer=1000):
    series = tf.expand_dims(series, axis=-1)
    dataset = tf.data.Dataset.from_tensor_slices(series)
    dataset = dataset.window(window_size + 1, shift=1, drop_remainder=True)
    dataset = dataset.flat_map(lambda w: w.batch(window_size + 1))
    dataset = dataset.shuffle(shuffle_buffer)
    dataset = dataset.map(lambda w: (w[:-1], w[1:]))
    return dataset.batch(batch_size).prefetch(1)

# lstm_rnn
def sequential_window_dataset(series, window_size):
    series = tf.expand_dims(series, axis=-1)
    dataset = tf.data.Dataset.from_tensor_slices(series)
    dataset = dataset.window(window_size + 1, shift=window_size, drop_remainder=True)
    dataset = dataset.flat_map(lambda window: window.batch(window_size + 1))
    dataset = dataset.map(lambda window: (window[:-1], window[1:]))
    return dataset.batch(1).prefetch(1)


def difference(timeseries, d=1):
    ts = timeseries
    baselines = []
    while 0 < d:
        baselines.append(ts[0])
        ts = ts[1:]-ts[:-1]
        d -= 1
    return ts, baselines


def dediff(diffseries, baselines, d=1):
    b = copy.deepcopy(baselines)
    if 2 < d:
       print('The value of d exceeds 2, not supported')
       return
    
    X = diffseries
    if 0 < d:
        X = one_dediff(diffseries, b.pop())
        if 1 < d:
            X = one_dediff(X, b.pop())
    
    return X


def one_dediff(diffseries, baseline=0.0):
     X = np.empty(len(diffseries) + 1)
     X[0] = baseline
     for i in range(1, len(diffseries)+1):
         X[i] = X[i-1] + diffseries[i-1]

     return X

