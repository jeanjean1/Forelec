'''
Visualization - Beginner level
'''

# ======================= Import Data  =======================
# Security
fname =  open('fname.txt','r').read()

# Use the pandas library to read data into a table (dataframe)
import pandas as pd
dataframe = pd.read_csv(fname, index_col=0, parse_dates=True) # Insert your own filename

# Select one column (index is kept)
cons = dataframe.consumption


# ======================= Overall viz =======================
# Line Plot (for zoom)
cons.plot()

# Customize a plot : Modify the object's attributes
import matplotlib.pyplot as plt
print(plt) # We just imported the module plt
print(plt.title) # inside this module, there is a function called title
type(plt.title)  # But we can use it an attritube of the object (here, of type string)...
plt.title = 'Electricity Consumption' # to change its value
print(plt.title)


# ======================= Detailed viz =======================
# heatmap: day of week vs hour of day ?
import seaborn as sns
sns.set()
sns.heatmap(cons)

    
