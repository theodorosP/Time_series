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


X = series.values
train = X[1:len(X) - 7]
test = X[len(X) - 7: len(X)]

model = AR(train)
model_fit = model.fit()
print("Lags: ", model_fit.k_ar)
print("Coefficients: ", model_fit.params)


predictions = model_fit.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
print(predictions)

for i in range(len(predictions)):
        print("prediction = % f, expected = % f" % (predictions[i], test[i]))

rmse = math.sqrt(mean_squared_error(test, predictions))
print(rmse)

plt.plot(test, label = "actual")
plt.plot(predictions, label = "predictions")
plt.legend(loc = "best")
plt.show()


predictions2 = model_fit.predict(start=len(train), end=len(train)+len(test) + 10, dynamic=False)

plt.plot(test, label = "actual")
plt.plot(predictions2, label = "predictions")
plt.legend(loc = "best")
plt.show()
