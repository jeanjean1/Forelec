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
- Summary Statistics (quartiles, boxplots...)
- Trend & Seasonality
- ACF, PACF
'''

# ========================= Summary Statistics =========================
df.describe()





# ========================= Stationarity =========================
# Is there a trend that we remove ? (= Stationary)

# 1. look at graph
# 2. remove stationarity


# ========================= Autocorrelation ===========================
# 2. Is the current value largely influenced by a given past value ? (= Autocorrelation)

# ACF


# PACF








