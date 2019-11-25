
#         UPDATING

import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation

fname =  open('fname.txt','r').read()
cons = pd.read_csv(fname, index_col=0, parse_dates=True).consumption # Insert your own filename


# ===== Data Engineering =====
"""
def series_to_supervised(batch_size, data):
    '''Change input data into a supervised learning dataset'''
    serie = []
    start, end, i = 1, 0, 1        
    while(start < (data - batch_size)) :    
        end = batch_size * i
        batch_av = np.average(data[-end:-start])
        serie.append(batch_av)
        start = end
    return serie    
"""
from keras.preprocessing.sequence import TimeseriesGenerator

split = -30000 # ~20 % of 150,000
train_x, train_y = cons[:split], ""
test_x, test_y = cons[split:], ""

data_gen = TimeseriesGenerator(cons.values, cons.shift().values),
                               length=10, sampling_rate=2,
                               batch_size=60)


# ===== Model =====
model = Sequential([
    Dense(32, input_shape=(len(train))),
    Activation('relu'),
    Dense(1),
])

model.compile(loss='mse', optimizer='adam')
model.fit(train_x, train_y, epochs=n_epochs, batch_size=n_batch, verbose=0)