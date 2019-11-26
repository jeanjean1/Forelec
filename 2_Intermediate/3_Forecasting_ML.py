
#         UPDATING

import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation

fname =  open('fname.txt','r').read()
cons = pd.read_csv(fname, index_col=0, parse_dates=True).consumption # Insert your own filename


# ===== Data Engineering =====

'''
# =========================ARMA models =================================
from statsmodels.tsa import arima_model as arm
train, test = daily[:100], daily[100:]

# ____ Testing our Findings ___
# AR (Autoregressive model)  
## lag of T determined automatically; Should match with ACF
model = arm.AR(train)
model_fit = model.fit()
print('Lag: %s' % model_fit.k_ar)
print('Coefficients: \n%s' % model_fit.params) # lag 1 and lag 7 have the biggest weights
pred = model_fit.predict(start=len(train), end=len(train)+len(test))
plt.plot(daily)
plt.plot(pred)


# MA 
## Moving average of the error 




# ARIMA
## ARIMA = AR model + MA model + differencing (I)
from statsmodels.tsa.arima_model import ARIMA
arima = ARIMA(df.consumption, order=(5,1,0))
model_fit = arima.fit()#disp=0)
print(model_fit.summary())
'''

# SARIMAX