import pandas as pd
import matplotlib.pyplot as plt
import math as math
from scipy.stats.stats import mode
from statsmodels.tsa.ar_model import AR 
from sklearn.metrics import mean_squared_error

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-min-temperatures.csv", header = 0, index_col = 0, parse_dates= True)

columns = list()
for col in series.columns:
    columns.append(col)

a = 5
X = series.values
train = X[0:len(X) - a]
test = X[len(X) - a: len(X)]

model = AR(train)
model_fit = model.fit()
print("Lags: ", model_fit.k_ar)
print("Coefficients: ", model_fit.params)
coef = model_fit.params
window =  model_fit.k_ar

predictions = model_fit.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
print(predictions)

for i in range(len(predictions)):
        print("prediction = % f, expected = % f" % (predictions[i], test[i]))

rmse = math.sqrt(mean_squared_error(test, predictions))
print(rmse)


b = 10
new_train = [train[i] for i in range(len(train))]
my_prediction = list()
for i in range (b):
    yhat = coef[0]
    length = len(new_train)
    lags = [new_train[i] for i in range(len(new_train))]
    print(len(lags))
    for j in range(window):
         yhat += coef[j + 1] * lags[- j - 1]
    my_prediction.append(yhat)
    new_train.append(yhat)
print(my_prediction)

predictions2 = model_fit.predict(start=len(train), end=len(train) + 10, dynamic=False)
print(predictions2)