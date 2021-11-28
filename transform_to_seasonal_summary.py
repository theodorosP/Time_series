from numpy.core.fromnumeric import mean, var
from numpy.lib.shape_base import column_stack
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/airline-passengers.csv", header = 0, index_col= 0 , parse_dates= True)
columns = [col for col in series.columns]
series[columns[0]].hist()
plt.show()
series[columns[0]].plot()
plt.show()

transformed_data = np.log(series[columns[0]])
plt.hist(transformed_data)
plt.show()

transformed_data = transformed_data.tolist()
split = int(len(transformed_data) / 2)
split_1 = transformed_data[0 : split]
split_2 = transformed_data[split : len(transformed_data)]

mean_1 = np.mean(split_1)
mean_2 = np.mean(split_2)

var_1 = np.var(split_1)
var_2 = np.var(split_2)

print(mean_1, mean_2)
print(var_1, var_2)