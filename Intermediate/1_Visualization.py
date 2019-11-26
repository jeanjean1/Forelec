import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

fname =  open('fname.txt','r').read()
df = pd.read_csv(fname, index_col=0, parse_dates=True) # Insert your own filename

# ================= Seasonality =======================

## Manual
freq = 60*24*7 # Weekly moving average
df['trend_a'] = df.consumption.rolling(window=freq).mean()
df['detrend_a'] = df.consumption-df.trend_a
df['season_a'] = '' # average of detrend_a for each time period

df['trend_m'] = df.consumption.rolling(window=freq).mean()
df['detrend_m'] = df.consumption/df.trend_m
df['season_m'] = '' # average of detrend_m for each time period

'''
# Statsmodel
from statsmodels.tsa.seasonal import seasonal_decompose
frequencies = [60*24,60*24*7, 60*24*30] # daily, weekly, monthly

# Note that this is the same as
fig , ax = plt.subplots(len(frequencies), 1, sharex=True)

for freq in frequencies:
    result = seasonal_decompose(df.consumption, model='additive', freq = freq)
    result.plot()
'''

    
