import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.algorithms import mode
from sklearn.linear_model import LinearRegression
import datetime as dtm

def parser(x):
        return dtm.datetime.strptime("190" + x, "%Y-%m")

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/shampoo.csv", index_col= 0 , header = 0, parse_dates = True, date_parser = parser )
print(series)

x = list()
for i in range(len(series)):
    x.append(i)
x = np.reshape(x, (len(series), 1))
print(x)

columns = list()
for col in series.columns:
        columns.append(col)

y = list()
for i in range(len(series)):
    y.append(series[columns[0]][i])
print(y)


model = LinearRegression()
model.fit(x, y)
trend = model.predict(x)
plt.plot(trend, label = "trend")
plt.plot(y, label = "actual values")
plt.legend(loc = "best")
plt.show()
detrend = list()
for i in range(len(series)):
    detrend.append(y[i] - trend[i])
plt.plot(detrend)
plt.show()
