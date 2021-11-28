import pandas as pd
import random as rd
import statsmodels.tsa.seasonal as stm
import matplotlib.pyplot as plt

series = list()
for i in range(0, 100):
        series.append(i**2)
results = stm.seasonal_decompose(series, freq = 1)
results.plot()
plt.show()