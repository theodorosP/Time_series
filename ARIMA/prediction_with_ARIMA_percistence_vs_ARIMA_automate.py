from cProfile import label
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
import warnings
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm


def parser(x):
    return datetime.strptime("190" + x, "%Y-%m")

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/shampoo.csv", header = 0, index_col= 0 , parse_dates= True, date_parser= parser)
print(series)

columns = list()
for col in series.columns:
    columns.append(col)

length = int(len(series) * 0.66)

train = series[ :length]
test = series[length : ]

train_list = list()
test_list = list()

for i in range(len(train)):
    train_list.append(train[columns[0]][i])

for i in range(len(test)):
    test_list.append(test[columns[0]][i]) 



set = list()
for i in range(len(series)):
    set.append(series[columns[0]][i])


#percistence for ARIMA model
predictions = list()
for i in range(len(test_list)):
    warnings.filterwarnings("ignore")
    model = sm.tsa.arima.ARIMA(train_list, order=(5, 1, 0))
    model_fit = model.fit()
    output = model_fit.forecast()
    predictions.append(output)
    train_list.append(test_list[i])

rmse = sqrt(mean_squared_error(test_list, predictions))
print("rmse percistence: ", rmse)

warnings.filterwarnings("ignore")
model = sm.tsa.arima.ARIMA(train_list, order=(5, 1, 0))
model_fit = model.fit()
output = model_fit.forecast(steps = len(predictions))

rmse = sqrt(mean_squared_error(test_list, output))
print("rmse automate: ", rmse)


plt.plot(test_list, label = "tested values")
plt.plot(predictions, label = "predictions percistence model")
plt.plot(output, label = "predictions automated ARIMA")
plt.legend(loc = "best")
plt.show()

#keep only the percistence model ARIMA with the lower rmse
b = 10
future_values = predictions
for i in range(b):
    warnings.filterwarnings("ignore")
    model = sm.tsa.arima.ARIMA(future_values, order = (5, 1, 0))
    model_fit = model.fit()
    output = model_fit.forecast()
    future_values.append(output)

plt.plot(test_list, label = "test_list")
plt.plot(future_values, label = "predicted")
plt.legend(loc = 1)
plt.show()

set1 = set[ : (len(set) - len(test_list))]
plt.plot(set, label = "set")
#plt.plot([None for i in train_list] + [j for j in test_list], label = "test")
plt.plot([None for i in set1] + [j for j in predictions], label = "trained model")
plt.legend(loc = "best")
plt.show()
