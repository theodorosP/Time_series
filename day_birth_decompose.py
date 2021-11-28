import statsmodels.tsa.seasonal as stat
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
from datetime import datetime

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-total-female-births.csv", header = 0, parse_dates = True, index_col = 0 )

x_labels = series.index.tolist()
for i in range(len(x_labels)):
	x_labels[i] = (x_labels[i].strftime("%d-%m-%Y"))
print(x_labels)

results = stat.seasonal_decompose(series, model = "multiplicative")
print(type(results.trend))

'''
results.trend.plot()
#plt.xticks(series.index, x_labels, rotation=25)
plt.show()

results.seasonal.plot()
plt.show()

results.resid.plot()
plt.show()

results.observed.plot()
plt.show()
'''
results.plot()
plt.show()

