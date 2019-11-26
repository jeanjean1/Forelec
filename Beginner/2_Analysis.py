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
# Histogram
cons.hist()
plt.show()

cons.describe()
cons.plot.box()
# ================= Resampling =================

daily = df.resample('D').sum()



# ================= Correlation =================
