'''
Visualization - Beginner level
'''

# ======================= Import Data  =======================
# Security
fname =  open('fname.txt','r').read()

# Use the pandas library to read data into a table (dataframe)
import pandas as pd
df = pd.read_csv(fname, index_col=0, parse_dates=True) # Insert your own filename

# Select one column (index is kept)
cons = df.consumption


# ======================= Overall viz =======================
# Line Plot (for zoom)
cons.plot()

# Customize the plot
import matplotlib.pyplot as plt
plt.title = 'Electricity Consumption'



# ======================= Detailed viz =======================
# heatmap
import seaborn as sns
sns.set()
sns.heatmap(cons)

    
