import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

fname =  open('fname.txt','r').read()
cons = pd.read_csv(fname, index_col=0, parse_dates=True).consumption # Insert your own filename
	

'''
Topics Covered :
- Distribution
- Resampling
- Scatter plot: how related is it with t-1 (correlation)
'''

# ================= Distribution =================
# Histogram: frequency of each value
cons.hist()
plt.show()

# Boxplots : distribution of each quartile, average and median 
cons.describe()
cons.plot.box()


# ================= Resampling =================
# The series object has a function to resample the data into a given frequency 
daily = cons.resample('D').sum()
daily.plot()

weekly = cons.resample('W').sum()
weekly.plot()


# ================= Correlation =================
previous = daily.shift(-1)  # Create another series 
plt.scatter(daily, previous) # Let's 
plt.show()