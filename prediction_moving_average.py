import pandas as pd
import numpy as np
from numpy import sqrt
from numpy import mean
from sklearn.metrics import mean_squared_error
from pandas import read_csv
import matplotlib.pyplot as plt

series = read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-total-female-births.csv", header = 0, index_col = 0, parse_dates = True)

X = series.values

window = 3
first = [X[i] for i in range(window)]
actual = [X[i] for i in range(window, len(X))]

predictions = []
for i in range(len(actual)):
	length = len(first)
	avg = mean([first[i] for i in range(length - window, length)])
	predictions.append(avg)
	first.append(actual[i])
	print("predicted = %f, expected = %f" %(predictions[i], actual[i]))
rmse = sqrt(mean_squared_error(actual, predictions))
print(rmse)

fig, ax = plt.subplots()
ax.plot(actual[:50], label = "actual")
ax.plot(predictions[:50], label = "predictions")
plt.legend(loc = "best")
plt.show()

