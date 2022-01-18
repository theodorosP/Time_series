import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
from datetime import datetime
import warnings

def parser(x):
    return datetime.strptime("190" +x, "%Y-%m")

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/shampoo.csv", header = 0, index_col= 0 , parse_dates=True, date_parser= parser) 


lenngth = int(0.66*len(series))
train = series[0 : lenngth]
test = series[lenngth : ]
train_list = list()
test_list = list()
columns = list()

for col in series.columns:
    columns.append(col)


for i in range(len(train)):
    train_list.append(train[columns[0]][i])

for i in range(len(test)):
    test_list.append(test[columns[0]][i])

predictions = list()
for i in range(len(test_list)):
    warnings.filterwarnings("ignore")
    model = sm.tsa.arima.ARIMA(train_list, order=(5, 1, 0))
    model_fit = model.fit()
    output = model_fit.forecast()
    print(output)
    predictions.append(output)
    train_list.append(test_list[i])

rmse = sqrt(mean_squared_error(predictions, test_list))
print(rmse)

plt.plot(test_list, label = "actual values")
plt.plot(predictions, label = "predictions" )
plt.legend(loc = "best")
plt.show()


#first way, pass each prediction to train set, I use as train set the predictions found above
#b is the number of forecasts you want
future_values_2 = predictions
b = 5
for i in range(b):
    model = sm.tsa.arima.ARIMA(future_values_2, order=(5, 1, 0))
    model_fit = model.fit()
    output = model_fit.forecast()
    print(output)
    future_values_2.append(output)



plt.plot(test_list, label = "actual values")
plt.plot(future_values_2, label = "predictions" )
plt.legend(loc = "best")
plt.show()


#second way automated
future_values = predictions
model = sm.tsa.arima.ARIMA(future_values, order=(5, 1, 0))
model_fit = model.fit()
output = model_fit.forecast(steps = 5 )
output = output.tolist()
for i in range(len(output)):
    future_values.append(output[i])
print(future_values)

plt.plot(test_list, label = "actual values")
plt.plot(future_values, label = "predictions" )
plt.legend(loc = "best")
plt.show()

    