from numpy.core.fromnumeric import reshape
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.core import series
from pandas.io.formats.format import set_eng_float_format
from pandas.io.parsers import read_csv

series = read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-min-temperatures.csv", index_col= 0 , header= 0 , parse_dates= True)

x = [i% 365 for i in range(len(series))]
#x = range(0, len(series))
y = series.values
deg = 4
coef = np.polyfit(x, y, deg)
print(coef)

curve = list()
for i in range(len(series)):
    value = coef[-1]
    for d in range(deg):
        value = value + x[i]**(deg - d)*coef[d]
    curve.append(value)


plt.plot(series.values)
plt.plot(curve, linewidth = 3)
plt.show()
'''
flatten_y = np.concatenate(y)
coef = np.polyfit(x, flatten_y, deg)
'''