import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

fname =  open('fname.txt','r').read()
df = pd.read_csv(fname, index_col=0, parse_dates=True) # Insert your own filename
daily = df.resample('D').sum().consumption

'''
Topics Covered :
- naive models
- Default ARIMA (correlation with previous measures &/OR average of errors)
'''


# ======================= Naive Models =======================

# Naive models assume no change between the present and the future. For example:

# Next value will be the same as the previous : Yt =Yt-1
forecast = df.shift(1)

# Next value will be the same as yesterday at the same time (60*24 = 1440) : Yt =Yt-1440
forecast = df.shift(1440)


# ======================= Rolling average =======================
# Next value = average of last x values. Ex: last hour
forecast = df.rolling(60)


########
# Why does the simpler model score better than the rolling average ?
# Because of correlation: last week's value is more highly correlated to today's value
# than yesterday's value is. In other words, it is a better predictor.
# We will learn better tools to detect correlation in the Intermediate course.
# For now, let's use a library made by smart people that will figure that out for us.
########



# ======================= Facebook Prophet =======================
from fbprophet import Prophet

# Create the object Prophet, who has all the functions we need
m = Prophet()

# Let it find the equation for us
m.fit(df)

# Create a new dataframe (= table)
future = m.make_future_dataframe(periods=365)

# Predict !
forecast = m.predict(future)
print(forecast.tail())  # [['ds', 'yhat', 'yhat_lower', 'yhat_upper']]




'''
END OF THE BEGINNER COURSE
'''

