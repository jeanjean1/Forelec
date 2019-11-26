import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

fname =  open('fname.txt','r').read()
df = pd.read_csv(fname, index_col=0, parse_dates=True) # Insert your own filename
daily = df.resample('D').sum().consumption

'''
3. Forecast
- naive models
- Default ARIMA (correlation with previous measures &/OR average of errors)
'''


