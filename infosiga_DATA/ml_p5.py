#ML Tutorial whith Python Classes

import pandas as pd
import quandl
import math,datetime
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

# Quandl is a stock data base - this case is a Google stock
df = quandl.get('WIKI/GOOGL')

#print(df.head())

# Creating a matrix: Labels and features
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

#Make the magic - take the how much one value s bigger (or smoller) than another
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

#take the labels and values really intresting
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))
print(forecast_out)

df['label'] = df[forecast_col].shift(-forecast_out)


X = np.array(df.drop(['label'],1))
X = preprocessing.scale(X)
X = X[:-forecast_out]
X_lately = X[-forecast_out:]

df.dropna(inplace=True)

y = np.array(df['label'])

#shuffle
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y, test_size=0.2)

#Classifier
#clf = svm.SVR(kernel='poly')
clf = LinearRegression(n_jobs=-1)

#train
clf.fit(X_train, y_train)

#test
accuracy = clf.score(X_test, y_test)

forecast_set = clf.predict(X_lately)

print(forecast_set, accuracy, forecast_out)

style.use('ggplot')
df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]


df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()


#print (df.head())
