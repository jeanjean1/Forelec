import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fname =  open('fname.txt','r').read()
cons = pd.read_csv(fname, index_col=0, parse_dates=True).consumption # Insert your own filename

'''
Covered contents:
- SARIMAX
- Decision Trees
- XGBoost
'''

# Prepare the data
X = timeseriesgenerator
y = 

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# ========================= SARIMAX =========================
from statsmodels.tsa.statespace.sarimax import SARIMAX

mod = SARIMAX(data['ln_wpi'], trend='c', order=(1,1,(1,0,0,1)))
mod = mod.fit(X_train)
print(mod.summary())

pred = mod.predict(X_test)
plt.plot(X, y)
plt.plot(X_test, pred)




# ========================= XGBoost =========================
from xgboost import XGBRegressor 

xgb = XGBRegressor()
xgb.fit(X_train_scaled, y_train)
pred = xgb.predict(X_test)

plt.plot()
