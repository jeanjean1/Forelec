import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

fname =  open('fname.txt','r').read()
cons = pd.read_csv(fname, index_col=0, parse_dates=True).consumption # Insert your own filename

'''
Covered contents:
    - Autoregression
    - Removing Trend
    - ARIMA
'''

# Instead of using the same value at a previous time step,
# let's use the coefficient of past values, based on their correlation.

# ========================= Regression ===========================
# Let's follow the PACF plot advice for
X = cons.shift(???)
y = cons

# Same as usual: import, create object, fit and see the result
from sklearn import LinearRegression
reg = LinearRegression()
reg.fit(X, y)
reg.score(X, y)

# Visualize the result
plt.scatter(cons)
plt.plot(X,y)

# How about we do that for each previous timestep ?

# ========================= Autoregression =========================
# Doing regression of a serie on its previous values = autoregression
# The forecast will be computed based on the coefficient (or weight)
# of each previous time step 

X = [cons.shift(1),cons.shift(2),cons.shift(3),cons.shift(4),cons.shift(5)]
y = cons

reg.fit(X, y)
reg.coef_

# This is called an AR model.


# ========================= Removing Trend =========================
# A trend is a change over time:
df.plot()
df.rolling(60*24*30).plot()

# If there is a trend, it is hard to calculate coefficients over time.
# Instead of changing the coefficients for each small period, we remove the trend.
df.diff().plot()

# In other words, we make the time serie "stationary"



# ======================= ARIMA =======================
# ARIMA model is the combination of these two concepts.
# ARIMA uses the correlation with previous time steps to make forecast.

## ARIMA = AutoRregression + I (remove trend) + Moving Average
# This is the same concept as we have seen in visualization.
# (Moving average is for errors, which we won't use here)

from statsmodels.tsa.arima_model import ARIMA
arima = ARIMA(df.consumption, order=(5,1,0))
model_fit = arima.fit() #(disp=0)
prediction = model_fit.forecast()

df.plot()
prediction.plot()
print(model_fit.summary())





'''
END OF THE INTERMEDIATE COURSE
'''





