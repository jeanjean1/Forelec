import pandas as pd
import numpy as np
import glob

pd.options.display.max_rows=40
pd.set_option('display.max_rows', 500)

def merge():
    files = glob.glob("../dataset/*.csv")
    df=pd.read_csv(files[0],parse_dates=True, index_col=0)
    
    for file in files[2:]:
    	df = df.append(pd.read_csv(file,parse_dates=True, index_col=0))
    	print(file)
    
    #Subset
    df = df.replace('None', np.NaN)
    df = df.loc[:,['Whitman.kW','Whitman.kWh']].astype('float32')

    df = df.sort_index()
    df.to_csv("../dataset/princeton_energycons.csv")

merge()


# Clean


serie = pd.read_csv("../dataset/princeton_energycons.csv", parse_dates=True, index_col=0)
serie = serie.sort_index()

"""
# Explore
watt = df[df.columns[~df.columns.to_series().str.contains('kWh')]]
watt.astype('float32')['Whitman.kW'].plot()
"""