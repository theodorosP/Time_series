from audioop import rms
from os import renames


import pandas as pd
from math import sqrt
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
import warnings
from datetime import datetime

def parser(x):
    return datetime.strptime("190" + x, "%Y-%m")

series = pd.read_csv("/home/thodoris/Downloads/machine_learning/Datasets-master/shampoo.csv", header = 0, index_col= 0, parse_dates= True, date_parser= parser)


def evaluate_arima_model(dataset, arima_order):
    columns = list()
    for col in dataset.columns:
        columns.append(col)
    length = int(len(dataset) * 0.66)
    train = dataset[columns[0]][: length]
    test = dataset[columns[0]][length : ]
    predictions = list()
    train = [i for i in train]
    test = [i for i in test]
    for i in range(len(test)):
        model = sm.tsa.arima.ARIMA(train, order = arima_order)
        model_fit = model.fit()
        yhat = model_fit.forecast()
        predictions.append(yhat)
        train.append(test[i])
    rmse = sqrt(mean_squared_error(test, predictions))
    #print(rmse)
    return rmse

#test function
evaluate_arima_model(series, (0, 0, 2))
evaluate_arima_model(series, (0, 0, 3))

def evaluate_models(dataset, p_values, d_values, q_values):
    best_score = float("inf")
    best_cfg = None
    for p in range(len(p_values)):
        for d in range(len(d_values)):
            for q in range(len(q_values)):
                order = (p_values[p], d_values[d], q_values[q])
                rmse = evaluate_arima_model(dataset, order)
                if rmse < best_score:
                    best_cfg = order
                    best_score = rmse
                    print("ARIMA:", order, ", rmse:%.3f " %rmse)
                else:
                     print("ARIMA:", order, ", rmse:%.3f " %rmse, " > ",  best_score , "which is for: ", best_cfg)
    print("Best ARIMA%s RMSE=%.3f" % (best_cfg, rmse) )                    


p_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d_values = [0, 1, 2, 3]
q_values = [0, 1, 2, 3]
warnings.filterwarnings("ignore")
evaluate_models(series, p_values, d_values, q_values)

