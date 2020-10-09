import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN, LSTM, Conv1D, Dropout, \
                                    BatchNormalization
import numpy as np
from .tools import *

#class auto(object):
#
#    def __init__(self):
#
#    def fit(self, X, target_col):
#
#    def search(self):


class RNNForecaster(object):

    def __init__(self, rnn_units=[100, 100], dropout=None):
        self.window_size = None
        self.model = Sequential(name='RNNForecaster')
        self.rnn_units = rnn_units
        self.batch_size = None
        self.train_size = None
        self.rnn_units = rnn_units
        self.dropout = dropout

    def fit(self, series, train_size=0.70, window_size=30, epochs=100, 
            batch_size=32, verbose=2):
        self.window_size = window_size
        self.batch_size = batch_size
        self.train_size = train_size

        # Build model
        model = Sequential()
        #model.add(BatchNormalization())
        model.add(SimpleRNN(self.rnn_units[0], return_sequences=True, 
                       input_shape=[None, 1]))

        for n in self.rnn_units[1:]:
            model.add(SimpleRNN(n, return_sequences=True))
        if not self.dropout == None:
            model.add(Dropout(self.dropout))
        model.add(Dense(units=1))

        # Compile model
        model.compile(loss=keras.losses.Huber(), optimizer='adam', metrics=['mae'])

        # Prepare data
        t = int(len(series)*train_size)
        train = series[:t]
        val = series[t:]
        train = seq2seq_window_dataset(train, window_size, batch_size)
        val = seq2seq_window_dataset(val, window_size, batch_size)

        # Callbacks and fitting
        checkpoint = keras.callbacks.ModelCheckpoint('best_rnn.h5', save_best_only=True)
        early_stopping = keras.callbacks.EarlyStopping(patience=50)

        model.fit(train, epochs=epochs, validation_data=val, 
                  callbacks=[early_stopping, checkpoint], verbose=verbose)
        print('Training completed')

        self.model = keras.models.load_model("best_rnn.h5")
        del model

    def predict(self, series):
        ds = tf.data.Dataset.from_tensor_slices(series[...,np.newaxis])
        ds = ds.window(self.window_size, shift=1, drop_remainder=True)
        ds = ds.flat_map(lambda w: w.batch(self.window_size))
        ds = ds.batch(self.batch_size).prefetch(1)
        print('Predicted values from window_size-1 to len(series)')
        return self.model.predict(ds)[:, -1,0]#[int(len(series)*self.train_size)-self.window_size+1:,-1,0]


    def score(self, series):
        pred = self.predict(series)

        return 

#class LSTM(object):
#
#class AttentionLSTM(object):
