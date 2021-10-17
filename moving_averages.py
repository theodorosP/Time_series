from pandas import read_csv
from pandas import concat

series = read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-total-female-births.csv", header = 0, index_col = 0, parse_dates = True) 
series.index = range(0, len(series),1)
lag1 = series.shift(1)
width = 3
lag3 = series.shift(width -1).rolling(window=width).mean()
series = concat([lag3, lag1, series], axis = 1)
series.columns = ["mean", "t", "t+1"]
print(series)
X = series.values
print(X)
history = [X[i] for i in range(width)]
test = [X[i] for i in range(width, len(X))]
print(history)
#print("*"*80)
#print(test)
print(len(history))
print(type(history))
