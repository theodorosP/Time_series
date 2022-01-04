from numpy.core.fromnumeric import mean
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from math import sqrt

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-min-temperatures.csv", header = 0, index_col= 0 , parse_dates= True)

df = pd.DataFrame()
df = pd.concat([series.shift(1), series], axis = 1)
df.columns = ["t", "t+1"]
print(df)
print(df.values)

train = df["t+1"][:len(df) - 7]
test = df["t+1"][len(df) - 7:]
predictions = df["t"][len(df) - 7:]

#plt.plot(train)
plt.plot(test, label = "test")
plt.plot(predictions, label = "predictions")
plt.legend(loc = "best")
plt.show()
rmse = sqrt(mean_squared_error(test, predictions))
print(rmse)