import pandas as pd
from math import sqrt
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AR

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-min-temperatures.csv", header= 0 , index_col= 0 , parse_dates= True)

X = series.values
days_to_predict = 7
train = X[1 : len(X) - days_to_predict]
test = X[len(X) - days_to_predict : len(X)]
model = AR(train)
model_fit = model.fit()
window = model_fit.k_ar
coef = model_fit.params
print(window)


history = [train[i] for i in range(len(train))]
predictions = list()
for i in range(len(test)): 
    yhat = coef[0]
    for j in range(window):
        yhat += coef[j + 1] * history[ -j - 1]
    predictions.append(yhat)
    history.append(test[i])


rmse = sqrt(mean_squared_error(test, predictions))
print(rmse)
plt.plot(test, label = "actual values")
plt.plot(predictions, label = "predicted")
plt.legend(loc = "best")
plt.show()


b = 3
l = train[-(window - days_to_predict):] 
l = [l[i] for i in range (len(l))]
l = l + predictions
for i in range (b):
    yhat = coef[0]
    print(len(l))
    for j in range(window):
         yhat += coef[j + 1] * l[- j - 1]
    l.append(yhat)
print(l)


plt.plot(X[-days_to_predict :] , label = "actual values")
plt.plot(l[-days_to_predict - b :], label = "predicted data")
plt.legend(loc = "best")
plt.show()
