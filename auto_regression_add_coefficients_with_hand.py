import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
from pandas.core.window.rolling import Window
from scipy.stats.stats import mode 
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.ar_model import AR

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-min-temperatures.csv", header= 0 , index_col= 0 , parse_dates= True)

X = series.values
train = X[1 : len(X) - 7]
test = X[len(X) - 7  :]
model = AR(train)
model_fit = model.fit()
window = model_fit.k_ar
coef = model_fit.params
print("coef", coef)

#put the last values in a list
history1 = train[len(train) - window : len(train)]
history2 = [history1[i] for i in range(len(history1))]


predictions = list()
for i in range(len(test)):
    length = len(history2)
    yhat = coef[0]
    lag = [history2[i] for i in range(length - window, length)]
    for j in range(window):
        #need the latest value
        yhat += coef[j + 1] * lag[window - j - 1]
    obs = test[i]
    history2.append(obs)
    predictions.append(yhat)
