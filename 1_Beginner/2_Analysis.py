import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

fname =  open('fname.txt','r').read()
dataframe = pd.read_csv(fname, index_col=0, parse_dates=True) # Insert your own filename

# A column (ex: "consumption") can be extracted as an object, called series:
cons = dataframe.consumption  
print(type(cons))


'''
Topics Covered :
- Distribution
- Resampling
- Scatter plot: how related is it with t-1 (correlation)
'''


# ================= Distribution =================
# Histogram: frequency of each value
cons.hist()
plt.title('Histogram : Distribution of electricity consumption (every minute)')
plt.show()

# A figure can include one or several plots.
# We want to create plots on a different graph, so we create a new figure:
plt.figure()

# Boxplots : distribution of each quartile, average and median 
cons.describe()
cons.plot.box()


# ================= Resampling =================
# The series object has a function to resample the data into a given frequency: 

plt.figure()
daily = cons.resample('D').sum()
daily.plot()

plt.figure()
weekly = cons.resample('W').sum()
weekly.plot()


# ================= Correlation =================
# Is the value at time T correlated to the value at time T-1 ?
fig = plt.figure()
previous = daily.shift(1)  # Create another series 
scatter = plt.scatter(x=daily/1000, y=previous/1000)
plt.title('')
plt.xlabel('Consumption at T (kWh)')
plt.ylabel('Consumption at T-1 (kWh)'), 

