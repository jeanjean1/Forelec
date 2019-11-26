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
# Helps get a feel of the data, 
# and detect some trends based on the frequency you choose

# Moving average


# ======================= Detailed viz =======================
# heatmap: day of week vs hour of day ?
import seaborn as sns
sns.set()
sns.heatmap(cons)


# ================= Summary Statistics =======================
# Boxplots
# per day, week and month




    
