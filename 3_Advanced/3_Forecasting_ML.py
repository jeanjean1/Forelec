
#         UPDATING

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


