import pandas as pd
import matplotlib.pyplot as plt
import datetime as dtm

def parser(x):
    return dtm.datetime.strptime("190" +x, "%Y-%m")
series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/shampoo.csv", header= 0 , index_col=0 , parse_dates= True, date_parser= parser)
df = pd.DataFrame()
df = pd.concat([series.shift(1), series], axis=1)
df.columns = ["t", "t+1"]
#t column  = predictions
#t + 1 column = actual values
train_size = int(len(df)*0.66)
X = df.values
train = X[1: train_size]
test = X[train_size: len(X)]
train_x = train[: , 0]
train_y = train[: , 1]
test_x = test[: , 0]
test_y = test[: , 1]

predictions = list()
for i in test_x:
    predictions.append(i)

plt.plot(train_y)
plt.plot([None for i in train_y] + [j for j in test_x], label = "predictions")
plt.plot([None for i in train_y] + [j for j in test_y], label = "test")
plt.legend(loc = "best")
plt.show()