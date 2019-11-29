import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
import matplotlib.pyplot as plt

fname =  open('./fname.txt','r').read()
cons = pd.read_csv(fname, index_col=0, parse_dates=True).consumption # Insert your own filename

'''
At that stage, a neural network with only 1 layer is merely finds the
optimal coefficients for the linear regressions of each input (time step).
This is called a linear transformation.

Let's try to predict 1 hour based on the last 12 hours !
'''

#%% ==================== Data Preparation ====================

# Train/test split
split = -30000 # ~20 % of 150,000
train, test = cons[:split], cons[split:]

#Change input data into a supervised learning dataset
n_steps = 60*12
horizon = 60

train_x = []
train_y = []
for i in range(n_steps, len(train)):
    train_x.append(train[i-n_steps:i].values)
    train_y.append(train[i:i+horizon].values)

n_epochs = 2
n_batch = 60


#%% ==================== Model Training ====================

model = Sequential()
model.add(Dense(32, input_shape=(n_steps,), activation='relu'))
model.add(Dense(horizon))

model.compile(loss='mse', optimizer='adam')

#%%
model.fit([train_x], [train_y], epochs=n_epochs, batch_size=n_batch, verbose=1)


#%% ==================== Testing ====================
test_x = []
test_y = []
for i in range(n_steps, len(test)):
    test_x.append(test[i-n_steps:i])
    test_y.append(test[i])

pred = model.predict([test_x])
#%%

plt.plot(test_y, label='test data')
plt.plot(pred.ravel(), label='prediction')
plt.legend()