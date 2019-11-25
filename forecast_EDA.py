import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

fname =  open('fname.txt','r').read()
df = pd.read_csv(fname, index_col=0, parse_dates=True) # Insert your own filename
daily = df.resample('D').sum().consumption

# ========================= Autocorrelation =================================
# Stationarity test
from statsmodels.tsa.stattools import adfuller
result = adfuller(daily.dropna())
print('p-value: %f' % result[1]) 
## NOTE ###
## ADFuller tests for unit root (regression test random walk with drift)
## Yt - Yt-1 = a + B*Yt-1 + noise    (constant + coeff*lag1 + noise)
## H0 : B=0, H1 : B<0
###########


# ACF


# PACF



'''
# =========================ARMA models =================================
from statsmodels.tsa import arima_model as arm
train, test = daily[:100], daily[100:]


# AR  (lag of T = auto)
model = arm.AR(train)
model_fit = model.fit()
print('Lag: %s' % model_fit.k_ar)
print('Coefficients: %s' % model_fit.params)
pred = model_fit.predict(start=len(train), end=len(train)+len(test))
plt.plot(daily)
plt.plot(pred)


# MA (Lagged AR forecast error: )




# ARIMA
from statsmodels.tsa.arima_model import ARIMA
arima = ARIMA(df.consumption, order=(5,1,0))
model_fit = arima.fit()#disp=0)
print(model_fit.summary())
'''

# SARIMAX


