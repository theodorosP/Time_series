from os import error
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
from statsmodels.tsa.ar_model import AR

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-total-female-births.csv", header=0, index_col= 0 , parse_dates= True)
df =pd.DataFrame()
df = pd.concat([series.shift(1) , series], axis = 1)
df.columns = ["t" , "t+1"]

lenght = int(0.66 * len(df))
expected = df["t+1"][1 : lenght]
predicted = df["t"][1 : lenght]
test_expected = df["t+1"][lenght :]
test_predicted = df["t"][lenght :]

train_resid = [expected[i] - predicted[i] for i in range(len(expected))]
model = AR(train_resid)
model_fit = model.fit()
window = model_fit.k_ar
coef = model_fit.params

predictions = list()
error_list= list()
for i in range (len(test_predicted)):
    error = test_expected[i] - test_predicted[i]
    error_list.append(error)
    yhat = coef[0]
    for j in range(window):
        yhat += coef[j + 1]*train_resid[-j - 1]
    predictions.append(yhat)
    train_resid.append(error) 


print(predictions)
#forecast = list()
b = 5
for i in range(b):
    yhat = coef[0]
    for j in range(window):
        yhat += coef[j + 1] * predictions[-j -1] 
    #forecast.append(yhat)
    predictions.append(yhat)

mod = predictions[-len(error_list) - b:]
plt.plot(error_list, label = "actual error")
plt.plot(mod, label = "trained error")
plt.legend(loc = 1)
plt.show()
