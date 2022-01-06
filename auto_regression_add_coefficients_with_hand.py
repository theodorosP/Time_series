import pandas as pd
from math import sqrt
from pandas.core.window.rolling import Window
from scipy.stats.stats import mode
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AR

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-min-temperatures.csv", header= 0 , index_col= 0 , parse_dates= True)
X = series.values

train = X[1 : len(X) - 7]
test = X[len(X) - 7 : len(X)]
model = AR(train)
model_fit = model.fit()
window = model_fit.k_ar
coef = model_fit.params
print(window)


history = train[len(train) - window : len(train)]
history = [history[i] for i in range(len(history))]
predictions = list()
for i in range(len(test)): 
    length = len(history)
    lag = [history[i] for i in range(length - window, length)]
    yhat = coef[0]
    for j in range(window):
        yhat += coef[j + 1] * lag[window -j - 1]
    predictions.append(yhat)
    obs = test[i]
    history.append(obs)


rmse = sqrt(mean_squared_error(test, predictions))
print(rmse)
plt.plot(test, label = "actual values")
plt.plot(predictions, label = "predicted")
plt.legend(loc = "best")
plt.show()




b = 3

l = train[-22:] 
l = [l[i] for i in range (len(l))]

l = l + predictions
print(l)
#l = train[-22:].values + predictions


for i in range (b):
    yhat = coef[0]
    lags = [l[i] for i in range(len(l))]
    print(len(lags))
    for j in range(window):
         yhat += coef[j + 1] * lags[- j - 1]
    l.append(yhat)
print(l)


plt.plot(X[-7 :] , label = "actual values")
plt.plot(l[-7 - b :], label = "predicted data")
plt.legend(loc = "best")
plt.show()


