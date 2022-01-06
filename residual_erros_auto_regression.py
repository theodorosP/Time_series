import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
from pandas.core.reshape.concat import concat
from scipy.stats.stats import Ttest_1sampResult, mode
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.ar_model import AR

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-total-female-births.csv", header=0, index_col= 0 , parse_dates= True)
df = pd.DataFrame()
df = concat([series.shift(1), series], axis = 1)
df.columns = ["t", "t+1"]
lenght = int(0.66*len(df))
columns = list()
for col in df.columns:
    columns.append(col)
expected = df[columns[1]][1 : lenght]
predicted = df[columns[0]][1 : lenght]
test_expected = df[columns[1]][lenght :].values
test_predicted = df[columns[0]][lenght  :].values

residual_erros = [expected.values[i] - predicted.values[i] for i in range(len(expected))]
train_resid = residual_erros
model = AR(train_resid)
model_fit = model.fit()
window = model_fit.k_ar
coef = model_fit.params
print( ' Lag=%d, Coef=%s ' % (window, coef))

history = train_resid[-window:]
predictions = list()
expected_error = list()
for i in range(len(test_expected)):
    error = test_expected[i] - test_predicted[i]
    expected_error.append(error)
    yhat = coef[0]
    for j in range(window):
        yhat += coef[j + 1]*history[-j -1]
    predictions.append(yhat)
    history.append(error)
print(predictions)








#predictions2 = model_fit.predict(start=len(residual_erros), end=len(residual_erros)+ 125, dynamic=False)
#print(predictions2)
#print(len(predicted))