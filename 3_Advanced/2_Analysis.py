import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

fname =  open('fname.txt','r').read()
df = pd.read_csv(fname, index_col=0, parse_dates=True) # Insert your own filename
daily = df.resample('D').sum().consumption



'''
Topics Covered :
- Stationarity Test
- Trend & Seasonality 
- FFT (for what ?)
- Librosa : ?
'''

# ========================= Stationarity Test =========================
# Augmented DFuller test 
## Test for a unit root : constant + Yt-1 * X + noise
from statsmodels.tsa.stattools import adfuller
result = adfuller(daily.dropna())
print('p-value: %f' % result[1])


# ========================= Trend & Seasonality =========================
# Library ?
# (algo from scratch)
## Manual
freq = 60*24*7 # Weekly moving average
df['trend_a'] = df.consumption.rolling(window=freq).mean()
df['detrend_a'] = df.consumption-df.trend_a
df['season_a'] = '' # average of detrend_a for each time period

df['trend_m'] = df.consumption.rolling(window=freq).mean()
df['detrend_m'] = df.consumption/df.trend_m
df['season_m'] = '' # average of detrend_m for each time period



# ========================= Decomposition - FFT =========================
