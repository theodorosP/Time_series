from matplotlib import colors
from numpy.lib.shape_base import column_stack
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.algorithms import value_counts

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/monthly-sunspots.csv", header= 0 , index_col = 0, parse_dates= True)


split = int(len(series)*0.66)
columns = [col for col in series.columns]
values = series[columns[0]].values
train = values[0 : split]
test = values[split : len(values)]
print(train)
print(test)

plt.plot(train, color = "blue", label = "train")
plt.plot([None for i in train] + [j for j in test], color = "green", label = "test")
plt.legend(loc = "best")
plt.show()
