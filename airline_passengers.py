import pandas as pd
import numpy as np
from pandas import read_csv
import matplotlib.dates as mpl_dates
from pandas import DataFrame
import matplotlib.pyplot as plt
from scipy.stats import boxcox

series = read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/airline-passengers.csv", index_col = 0, header = 0, parse_dates= True)
print(series)


fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(series["Passengers"])
ax2.hist(series["Passengers"])
#date_format = mpl_dates.DateFormatter("%d %b %Y")
#ax1.xaxis.set_major_formatter(date_format)
#fig.autofmt_xdate()
plt.show()

'''
fig, (ax1, ax2) = plt.subplots(2)
fun = [i**2 for i in range(1,100)]
ax1.plot(fun)
ax2.plot(np.sqrt(fun))
plt.show()


fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(np.sqrt(series["Passengers"]))
ax2.hist(np.sqrt(series["Passengers"]))
plt.show()

fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(np.log(series["Passengers"]))
ax2.hist(np.log(series["Passengers"]))
plt.show()
'''

series["Passengers"], lam = boxcox(series["Passengers"])
print( lam)
plt.hist(series["Passengers"])
plt.show()

