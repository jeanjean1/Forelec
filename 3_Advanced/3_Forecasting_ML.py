import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation

fname =  open('fname.txt','r').read()
cons = pd.read_csv(fname, index_col=0, parse_dates=True).consumption # Insert your own filename

'''
Covered contents:
- SARIMAX
- Decision Trees
- XGBoost
'''

from sklearn import train_test_split



# ========================= SARIMAX =========================






# ========================= Decision Tree =========================






# ========================= XGBoost =========================
from xgboost import XGBRegressor 

xgb = XGBRegressor()
xgb.fit(X_train_scaled, y_train)
pred = xgb.predict(X_test)

plotModelResults(xgb, 
                 X_train=X_train_scaled, 
                 X_test=X_test_scaled, 
                 plot_intervals=True, plot_anomalies=True)