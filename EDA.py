import pandas as pd

fname =  open('fname.txt','r').read()
df = pd.read_csv(fname, index_col=0, parse_dates=True) # Insert your own filename

# Seasonality
from statsmodels.tsa.seasonal import seasonal_decompose
frequencies = [60*24,60*24*7 , 60*24*30] # daily, weekly, monthly
for freq in frequencies:
    result = seasonal_decompose(df.consumption, model='additive', freq = freq)
    result.plot()
    #te


    