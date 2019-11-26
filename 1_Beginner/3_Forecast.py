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

# Naive models assume no change between the present and the future.
# Let's say the value will be the same as yesterday, at the same time:



# ======================= Rolling average =======================




# ======================= Analysis =======================
# Why does the simpler model score better than the rolling average ?
# Because of correlation.
# We will learn better tools to detect correlation in the Intermediate course.



# ======================= ARIMA =======================
# ARIMA uses the correlation with previous time steps to make forecast.
# This is the same concept as we have seen in visualization.
# Details of this model are explored in the Intermediate course.

from statsmodels.tsa.arima_model import ARIMA
arima = ARIMA(df.consumption, order=(5,1,0))
model_fit = arima.fit() #(disp=0)
prediction = model_fit.forecast()

df.plot()
prediction.plot()
#print(model_fit.summary())





'''
END OF THE BEGINNER COURSE
'''

