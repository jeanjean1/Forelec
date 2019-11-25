import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

fname =  open('fname.txt','r').read()
df = pd.read_csv(fname, index_col=0, parse_dates=True) # Insert your own filename
daily = df.resample('D').sum().consumption

# 1. Is there a trend that we remove ? (= Stationary)
# 2. Is the current value largely influenced by a given past value ? (= Autocorrelation)
# 3. 

# ========================= Stationarity =========================
# Augmented DFuller test 
## Test for a unit root : constant + Yt-1 * X + noise
from statsmodels.tsa.stattools import adfuller
result = adfuller(daily.dropna())
print('p-value: %f' % result[1])


# ========================= Autocorrelation =================================

# ACF


# PACF



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
from statsmodels.tsa.arima_model import ARIMA
arima = ARIMA(df.consumption, order=(5,1,0))
model_fit = arima.fit()#disp=0)
print(model_fit.summary())
'''

# SARIMAX
