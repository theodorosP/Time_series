import pandas as pd
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
import numpy as np

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-min-temperatures.csv", header= 0 , index_col=0, parse_dates= True)
days_year = 365
print(series)
l = list()
for col in series.columns:
    l.append(col)
deseasonaled = list()
for i in range(days_year, len(series)):
    deseasonaled.append(series[l[0]][i] - series[l[0]][i-365])

series["Dates"] = pd.to_datetime(series.index)
series["Dates"] = series["Dates"].apply(mpl_dates.date2num)
series.index = series["Dates"]
series.index = range(0, len(series), 1)

series["deseasonaled"] = np.nan
j = 0
for i in range(days_year, len(series)):
    series.loc[i, "deseasonaled"] = deseasonaled[j]
    j = j + 1


series.index = series["Dates"]
plt.rcParams["figure.figsize"] = [12, 7 ]
plt.rc("font" , size = 14)
fig, ax = plt.subplots()
ax.plot(series["deseasonaled"])
date_format = mpl_dates.DateFormatter('%d %b %Y')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate() 
plt.show()