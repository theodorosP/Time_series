from matplotlib.dates import DateFormatter
from pandas import read_csv
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

def parser(x):
        return( datetime.strptime( '190' + x, '%Y-%m' ))

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/shampoo.csv", index_col = 0, squeeze = True, header = 0, date_parser=parser, parse_dates = True)

print(series)


upsample = series.resample("D").mean().interpolate(method = "linear")




print(upsample)



fig, ax = plt.subplots()
ax.plot(upsample)
date_format = DateFormatter('%d %b %Y')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()
plt.show()




upsample = series.resample("D").mean().interpolate(method = "spline", order = 2)
fig, ax = plt.subplots()
ax.plot(upsample)
date_format = DateFormatter('%d %b %Y')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()
plt.show()


resample = series.resample( ' q ' ).mean()

print(resample)

fig, ax = plt.subplots()
ax.plot(resample)
date_format = DateFormatter("%d %b %Y")
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()
plt.show()


resample = series.resample("A").sum()
fig, ax = plt.subplots()
ax.plot(resample)
date_format = DateFormatter("%d %b %Y")
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()
plt.show()

