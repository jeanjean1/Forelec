
#         UPDATING

import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation

fname =  open('fname.txt','r').read()
cons = pd.read_csv(fname, index_col=0, parse_dates=True).consumption # Insert your own filename

# Predict 1 hour based on the last 12 hours


# ==================== Data Preparation ====================

# Train/test split
split = -30000 # ~20 % of 150,000
train, test = cons[:split], cons[split:]

#from keras.preprocessing.sequence import TimeseriesGenerator
#data_gen = TimeseriesGenerator(data=cons, targets=cons.shift(),length=10, sampling_rate=2,batch_size=5)

#Change input data into a supervised learning dataset
n_steps = 60*12
train = cons.values
train_x, train_y = [], []
for i in range(n_steps, len(train)):
    train_x.append(train[i-n_steps:i])
    train_y.append(train[i])

n_epochs = 4
n_batch = 60

# ==================== Model ====================

# LSTM
