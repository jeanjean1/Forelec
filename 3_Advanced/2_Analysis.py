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




# ========================= Decomposition - FFT =========================
