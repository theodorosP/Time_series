from numpy.core.fromnumeric import size
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import numpy as np
from pandas.core.series import Series

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-min-temperatures.csv", header = 0, index_col= 0 , parse_dates= True)
resample = series.resample("M").mean()
resample["Dates"] = pd.to_datetime(resample.index)
resample["Dates"] = resample["Dates"].apply(mpl_dates.date2num)

deseasonaled = list()
year_months = 12
for i in range(year_months, len(resample)):
    deseasonaled.append(resample["Temp"][i] - resample["Temp"][i - year_months])

resample["deseasonaled"] = np.nan
resample.index = range(0, len(resample), 1)
j = 0
for i in range(year_months, len(resample)):
    resample.loc[i, "deseasonaled"] = deseasonaled[j]
    j = j + 1

resample.index  = resample["Dates"]
plt.rcParams["figure.figsize"] = [12 ,7]
plt.rc("font", size = 14)
fig, ax = plt.subplots()
ax.plot(resample["deseasonaled"])
date_format = mpl_dates.DateFormatter("%d %b %Y") 
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()
plt.show()

