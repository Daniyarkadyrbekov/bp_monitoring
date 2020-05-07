import pandas as pd
import numpy as np
import sklearn.linear_model as lm
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as mse
import glob
import os
from sklearn import metrics
from math import sqrt
import matplotlib.pyplot as plt

filenames = ['Temirlan_summary.txt',
             'Lera_summary.txt'    , 
             'Lev_summary.txt'     ,
             'Angelina_summary.txt',
             'Deniska_summary.txt' , 
             'Yarik_summary.txt'   ,
             'Sofa_summary.txt'    ,
             'Dimon_summary.txt'   ]

df = []
for filename in filenames:
    li = pd.read_csv(filename, index_col = None, header=None, sep='\t')
    df.append(li)
df = pd.concat(df, axis = 0, ignore_index=True)
df.rename(columns={0: 'shift', 1: 'bpm', 2: 'attitude', 3: 'bp'}, inplace=True)
df = df.sample(n=80, random_state=42)
X_train, X_test, y_train, y_test = df[['shift', 'bpm', 'attitude']][:50].values, df[['shift', 'bpm', 'attitude']][50:].values,df['bp'][:50].values,df['bp'][50:].values
skm = lm.LinearRegression()
skm.fit(X_train, y_train)
predicted = skm.predict(X_test)



absolute_error = metrics.mean_absolute_error(y_test, predicted)

rmse = np.sqrt(metrics.mean_squared_error(y_test, predicted))

plt.scatter(y_test, predicted)
plt.show()

print(y_test)
print(predicted)

print(absolute_error, rmse)
print(skm.corr_)