import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-total-female-births.csv", header = 0, index_col= 0 , parse_dates= True)

series.hist()
#plt.show()

columns = list()
for col in series.columns:
    columns.append(col)

values = list()
for i in range (len(series)):
    values.append(series[columns[0]][i])

split = int(len(values)/2)

split1 = values[0 : split]
split2 = values[split : len(values)]

mean1 = np.mean(split1)
mean2 = np.mean(split2)

var1 = np.var(split1)
var2 = np.var(split2)

print(mean1, mean2)
print(var1, var2)