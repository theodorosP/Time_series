import pandas as pd
from math import sqrt, exp, log
from sklearn.metrics import mean_squared_error
import scipy.stats as scipystats
import os
import warnings
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as sm
import statsmodels.graphics.tsaplots as sgt
import statsmodels.api as stm
from statsmodels.graphics.gofplots import qqplot
import numpy as np
from statsmodels.tsa.arima.model import ARIMAResults

series = pd.read_csv("/home/thodoris/Downloads/machine_learning/Datasets-master/robberies_modified.csv", header = 0, index_col = 0, parse_dates= True)
os.chdir("/home/thodoris/Downloads/machine_learning")


#test harness, vallidation dataset 10% fo the dataset, validation is 10% of the initial, 12/120
split_point = len(series) - 12
data_set = series[0 : split_point]
validation = series[split_point : ]
data_set.to_csv("data_set.csv")
validation.to_csv("validation.csv")


warnings.filterwarnings("ignore")
os.system("pwd")
#Persistence model
series1 = pd.read_csv("data_set.csv", header = 0, index_col = 0, parse_dates = True)
length = int(len(series1) * 0.5)
columns = list()
train = series1[ : length]
test = series1[length : ]
for col in series1.columns:
    columns.append(col)
test_list = list()
train_list = list()
for i in range(len(train)):
    train_list.append(train[columns[0]][i])
for i in range(len(test)):
    test_list.append(test[columns[0]][i])


def get_df_columns(data_set):
    columns = list()
    for col in data_set.columns:
        columns.append(col)
    return columns


def difference(data_set):
    difference = list()
    columns = get_df_columns(data_set)
    for i in range(1, len(data_set)):
        difference.append(data_set[columns[0]][i] -data_set[columns[0]][i - 1] )
    df_difference = pd.DataFrame(difference)
    df_difference.columns = ["Difference"]
    return df_difference

stationary_data = difference(series1)
stationary_data.index = series1.index[1 : ]
result = sm.adfuller(stationary_data)
print("ADF statistics: ", result[0])
print("p value: ", result[1])

stationary_data.to_csv("stationary_data.csv", header = True)
series3 = pd.read_csv("stationary_data.csv", index_col = 0, header = 0 , parse_dates = True)
print(series3)

sgt.plot_acf(series1)
plt.show()
sgt.plot_pacf(series1)
plt.show()

#ARIMA(11, 1, 2) found from acf and pacf, now I test the model for p values from 0 to 12, d values from 0 to 3 and q values from 0 to 12
#11 might has problem to converge

def evaluate_arima_model(dataset, arima_order):
    columns = list()
    for col in dataset.columns:
        columns.append(col)
    length = int(len(dataset) * 0.5)
    train = dataset[columns[0]][: length]
    test = dataset[columns[0]][length : ]
    predictions = list()
    train = [i for i in train]
    test = [i for i in test]
    for i in range(len(test)):
        model = stm.tsa.arima.ARIMA(train, order = arima_order)
        model_fit = model.fit()
        yhat = model_fit.forecast()
        predictions.append(yhat)
        train.append(test[i])
    rmse = sqrt(mean_squared_error(test, predictions))
    return rmse

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
    print("Best ARIMA%s RMSE=%.3f" % (best_cfg, best_score) )                    


p_values = [1, 2, 3]
d_values = [1, 2, 3]
q_values = [1, 2, 3]
warnings.filterwarnings("ignore")
evaluate_models(series1, p_values, d_values, q_values)

#ARIMA(1, 1, 1) was found to be the one with the least RMSE, p value for 11 makes model to diverge

#find residual erros, they should follow gaussian distribution and must show no correlation



predictions = list()
for i in range(len(test_list)):
    model = stm.tsa.arima.ARIMA(train_list, order = (1, 1, 1))
    model_fit = model.fit()
    yhat = model_fit.forecast()
    predictions.append(yhat)
    train_list.append(test_list[i])
residuals = [test_list[i] - predictions[i] for i in range(len(test_list))]
df_residuals = pd.DataFrame(residuals)
df_residuals.plot(kind = "kde")
plt.show()

sgt.plot_acf(df_residuals)
plt.show()
sgt.plot_pacf(df_residuals)
plt.show()


test_list1 = list()
train_list1 = list()
for i in range(len(train)):
    train_list1.append(train[columns[0]][i])
for i in range(len(test)):
    test_list1.append(test[columns[0]][i])

#use box cox to re-evaluate ARIMA(1, 1, 1)
def inverse_box_cox(values, lam):
    if lam == 0 :
        return values
    return exp(log(lam * values + 1) / lam)
y_hat_values = list()
for i in range (len(test_list1)):
    new_data, lam = scipystats.boxcox(train_list1)
    #if lamda gets less than -5, we set it to 1
    if lam < -5:
        new_data = train_list1
        lam = 1
    model = stm.tsa.arima.ARIMA(new_data, order = (1, 1, 1))
    model_fit = model.fit()
    predict = model_fit.forecast()
    predict = inverse_box_cox(predict, lam)
    y_hat_values.append(predict)
    train_list1.append(test_list1[i])
    print("Expected: ", test_list1[i], "predicted: ", y_hat_values[i])
rmse = sqrt(mean_squared_error(test_list1, y_hat_values))
print(rmse)#indeed it gives a better rmse



def boxcox_inverse(value, lam):
    if lam == 0:
        return exp(value)
    return exp(log(lam * value + 1) / lam)

#Validate Model
series_validation = pd.read_csv("/home/thodoris/Downloads/machine_learning/validation.csv", header = 0, index_col = 0, parse_dates = True)
print(series_validation)

validation_columns = get_df_columns(series_validation)

my_model = ARIMAResults.load("model.pkl")
lam = np.load("model_lambda.npy")
predictions = list()
yhat = my_model.forecast()
yhat = boxcox_inverse(yhat, lam)
predictions.append(yhat)
print(predictions)

val_cols = get_df_columns(series_validation)
val_list = list()
for i in range(len(series_validation)):
    val_list.append(series_validation[val_cols[0]][i])



history = list()
for i in range(len(series1)):
    history.append(series1[columns[0]][i])
values = history.copy()
for i in range(1, len(series_validation)):
    transformed_new, lam_new = scipystats.boxcox(history)
    print(lam)
    if lam_new < -5:
        transformed_new = history
        lam_new = 1
    model = stm.tsa.arima.ARIMA(transformed_new, order = (1, 1, 1))
    model_fit = model.fit()
    yhat_new = model_fit.forecast()
    yhat_new = boxcox_inverse(yhat_new, lam_new)
    predictions.append(yhat_new)
    history.append(series_validation[validation_columns[0]][i])
    print(yhat_new, series_validation[validation_columns[0]][i])

rmse = sqrt(mean_squared_error(predictions, val_list))
print(rmse)


l1 = predictions.copy()
model_data = values + predictions
print(model_data)

forecast = list()
#b is the number of months we wwant to predict
b = 0
while b <= 2:
    transformed_new, lam_new = scipystats.boxcox(model_data)
    print(lam)
    if lam_new < -5:
        transformed_new = model_data
        lam_new = 1
    model = stm.tsa.arima.ARIMA(transformed_new, order = (1, 1, 1))
    model_fit = model.fit()
    yhat_new = model_fit.forecast()
    yhat_new = boxcox_inverse(yhat_new, lam_new)
    model_data.append(yhat_new)
    forecast.append(yhat_new)
    b = b + 1
print(forecast)
mod = l1 + forecast


total_data = values + val_list
plt.plot(values, label = "actual values")
plt.plot([None for i in values] + [i for i in mod], label = "predictions")
plt.plot([None for i in values] + [i for i in val_list], label = "expected")
plt.legend(loc = "best")
plt.show()


plt.plot(mod, label = "predictions")
plt.plot(val_list, label = "expected")
plt.legend(loc = "best")
plt.show()
