import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tools import validation
import statsmodels.tsa.stattools as sts
import numpy as np

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/airline-passengers.csv", header = 0, index_col = 0, parse_dates= True)

columns = [col for col in series.columns]
values = series[columns[0]]
test = sts.adfuller(values)
print("Statistics: %f" %test[0])
print("P-value: %f" %test[1])
for i, j in test[4].items():
    print(i, round(j,3))

set1 = np.log(values)
test = sts.adfuller(set1)
print("Statistics: %f" % test[0]) 
print("P-values: %f" % test[1])
for i, j in test[4].items():
    print(i, round(j, 2))

