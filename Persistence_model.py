import pandas as pd
import matplotlib.pyplot as plt
import datetime as dtm
from math import sqrt
from sklearn.metrics import mean_squared_error

def parser(x):
    return dtm.datetime.strptime("190" +x , "%Y-%m")

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/shampoo.csv", header = 0, index_col= 0 , parse_dates= True, date_parser= parser)
df = pd.DataFrame()
df = pd.concat([series.shift(1), series], axis =1)
df = pd.DataFrame(df.values)
df.columns = ["t", "t+1"]
x = df.values
train_size = int(len(df) * 0.66)
train = x[1: train_size]
test = x[train_size : len(x)]
train_X = train[:,0]
train_Y = train[:,1]
test_X = test[:, 0]
test_Y = test[:, 1]
print(train)
print(test_X)
def model_persistence(x):
    return x
predictions = list()
for x in test_X:
    yhat = model_persistence(x)
    predictions.append(yhat)
rmse = sqrt(mean_squared_error(test_Y, predictions))
print(rmse)


plt.plot(train_Y)
plt.plot([None for i in train_Y] + [j for j in predictions], label = "predictions")
plt.plot([None for i in train_Y] + [j for j in test_Y],   label = "test")
plt.legend(loc = "best")
plt.show()
