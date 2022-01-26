from argparse import _MutuallyExclusiveGroup
from math import sqrt
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
import warnings 

def evaluate_arima_model(X, arima_order):
    length = int(len(X) * 0.66)
    train = X[0 : length]
    test = X[length : ]
    predictions = list()
    for i in range(len(test)):
        model = sm.tsa.arima.ARIMA(train, arima_order)
        model_fit = model.fit()
        yhat = model_fit.forecast()
        predictions.append(yhat)
        test.append(train[i])
    rmse = sqrt(mean_squared_error(test, predictions))
    print(rmse)
    return rmse
