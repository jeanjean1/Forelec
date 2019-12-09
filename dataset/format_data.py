import pandas as pd
import numpy as np

ori = pd.read_csv('household_power_consumption.txt', sep=';')
df = ori[1600236:] # from 2010
df.head()


df['Datetime'] = df.Date + " " + df.Time
df['Datetime'] = pd.to_datetime(df.Datetime)
df = df.set_index('Datetime')

df2 = pd.DataFrame(df.Global_reactive_power, index=df.index)
df2 = df2.replace("?", np.NaN)
df2.Global_reactive_power = df2.Global_reactive_power.astype('float32')

daily = df2.resample('D').sum()
daily.to_csv('daily_house_elec.csv')
