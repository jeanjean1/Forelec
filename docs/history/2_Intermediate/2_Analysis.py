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
    - Trend
    - Regression
    - ACF, PACF
'''


# Box plots give the distribution
# But what if the distribution is spread over time ?
# What if the level (for example, average) is changing is changing over time ?
# The boxplots are then not representative of each period, but just an average of otherwise
# very different periods. If our sales have increased constantly by 10% every month, the boxplot
# of december is going to be spread out.

# To check that, let's see if there is a "trend" in the data.

# ========================= Trend =========================
# A trend is a change over time:
df.plot()
df.rolling(60*24*30).plot()



# ========================= Autocorrelation ===========================
# Remember the scatter plot used to estimate correlation ?
# Let's do it for all the time steps. We're looking at the correlation of a series with
# itself at previous time steps : autocorrelation

# ACF
from pandas.plotting import autocorrelation_plot
autocorrelation_plot(df.consumption)

# PACF
# Partial Auto-correlation is the same, but removes the impact of previous time steps.
# better choice to decide on what time step we need to focus.
from statsmodels.graphics.tsaplots import plot_acf
plot_pacf(df.consumption, lags=60*24*7)





