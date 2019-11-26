import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

fname =  open('fname.txt','r').read()
df = pd.read_csv(fname, index_col=0, parse_dates=True) # Insert your own filename


'''
Seaborn lib
'''

    
