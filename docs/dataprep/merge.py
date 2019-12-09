import pandas as pd
import glob

files = glob.glob("./*.csv")
df=pd.read_csv(files[0],parse_dates=True, index_col=0)

for file in files[2:]:
	df = df.append(pd.read_csv(file,parse_dates=True, index_col=0))
	print(file)

df.to_csv("princeton_energycons.csv")

