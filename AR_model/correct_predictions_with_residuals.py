import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-total-female-births.csv", header= 0, index_col= 0 , parse_dates= True)
df = pd.DataFrame()
df = pd.concat([series.shift(1), series], axis = 1)
df.columns = ["t", "t+1"]
length = int(0.66*len(df))
expected = df["t+1"][1 : length]
predicted = df["t"][1 : length]
test_expected = df["t+1"][length : ]
test_predicted = df["t"][length :]

train_resid = [expected[i] - predicted[i] for i in range (len(expected))]
model = AR(train_resid)
model_fit = model.fit()
window = model_fit.k_ar
coef = model_fit.params


#error = [test_expected[i] - test_predicted[i] for i in range(len(test_predicted))]
predictions = list()
error_list = list()
for i in range(len(test_predicted)):
    yhat = test_predicted[i]
    error = test_expected[i] - test_predicted[i]
    #error_list.append(error)
    pred_error = coef[0]
    for j in range(window):
        pred_error += coef[j + 1] * train_resid[-j - 1]
    yhat += pred_error
    predictions.append(yhat)
    train_resid.append(error)
    print("Predicted = %f, Expected = %f" % (yhat, test_expected[i]))

rmse = sqrt(mean_squared_error(predictions, test_expected))
print(rmse)

list_test_expected = list()
for i in range(len(test_expected)):
    list_test_expected.append(test_expected[i])
print("predictions: ", len(predictions))
print("test_expected: ", len(test_expected))
plt.plot(list_test_expected, label = "Actual values")
plt.plot(predictions, label = "Predictions")
plt.legend(loc = "best")
plt.show()