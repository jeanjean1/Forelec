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


# ======================= Visualization =======================
# Line Plot
# Inside the 'series' object, there is a function called "plot" which graphs the data:
cons.plot()

# <Customize the plot>
# We import a module, with the nickname "plt":
import matplotlib.pyplot as plt
print(plt) 

# Inside this module, the function "title" 
# allows you to set the "title" (attribute) of the "plot" (object)
print("Type:", type(plt.title))  
print("Parameters of the function:", plt.title) 
plt.title('Electricity Consumption')
print("Value of the 'plot' attribute:", plt.title)

# Same for all other functions:
plt.xlabel('Date & Time')
plt.ylabel('Electricity Consumption (Wh)')




    
