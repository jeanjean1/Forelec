import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation

fname =  open('fname.txt','r').read()
cons = pd.read_csv(fname, index_col=0, parse_dates=True).consumption # Insert your own filename


# At that stage, a neural network with only 1 layer is merely finds the
# optimal coefficients for the linear regressions of each input (time step).
# This is called a linear transformation.

# ======================= Preprocessing =======================

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


    
# =============== Simple Neural Network ===============
model = Sequential([
    Dense(32, input_shape=(len(train))),
    Activation('relu'),
    Dense(1),
])

model.compile(loss='mse', optimizer='adam')
model.fit(train_x, train_y, epochs=n_epochs, batch_size=n_batch, verbose=0)



# =============== NN with hidden layer ===============
# What if some parts of the equation are not useful ?
# We use a non-linear function to get a value tending towards 0 or 1
# This is called an "activation function".

model = Sequential([
    Dense(32, input_shape=(len(train))),
    Activation('relu'),
    Dense(1),
])

model.compile(loss='mse', optimizer='adam')
model.fit(train_x, train_y, epochs=n_epochs, batch_size=n_batch, verbose=0)