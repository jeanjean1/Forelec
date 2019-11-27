import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

fname =  open('fname.txt','r').read()
df = pd.read_csv(fname, index_col=0, parse_dates=True) # Insert your own filename

'''
Topics Covered :
- Overall visualization : moving average
- Distribution: 
 - Resampling
 - Boxplots per month, per day of week, per hour (seaborn)
'''


# ================= Overall visualization =======================

df.plot()

# Moving average
# - Helps get a feel of the data, 
# - detect some trends based on the frequency you choose
df.rolling(window = 60*24*7).plot()
df.rolling(window = 60*24*30).plot()


# ======================= Detailed viz =======================
# heatmap: day of week vs hour of day ?
import seaborn as sns
sns.set()
sns.heatmap(df.consumption)

# Heatmap allows to compare values with each other
# How do we sum that up ?


# ================= Summary Statistics =======================
# Boxplots
df.describe()
df.boxplot()

# Resampling
daily = df.resample('D').sum()
weekly = df.resample('W').sum()
monthly = df.resample('M').sum()

weekly = weekly/1000
monthly = monthly/1000

# Distribution per day, week and month
seaborn.boxplot(df.index.dayofyear, df.consumption, ax=ax)



    
