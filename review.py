from pandas import read_csv
from pandas import DataFrame
import pandas as pd
from pandas import concat
import numpy as np
import matplotlib.dates as mpl_dates
import datetime
import matplotlib.pyplot as plt
from pandas import Grouper
from pandas.plotting import autocorrelation_plot
from pandas.plotting import lag_plot
from datetime import datetime

'''
series = read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-min-temperatures.csv", index_col = 0, header = 0, parse_dates = True)

series.columns = ["Temp"]
#print(series.index)


#print(series.values)
temps = pd.DataFrame(series.values)
print(temps)
dataframe = concat([temps.shift(3) ,temps.shift(2) ,temps.shift(1) , temps ], axis = 1)
dataframe.columns = ["t-2", "t-1","t", "t+1"]
print(dataframe)


temps = pd.DataFrame(series.values)
dataframe = concat([temps.shift(1).rolling(window =2).mean() ,temps.shift(1), temps], axis = 1)
dataframe.columns = ["mean", "t", "t+1"]
dataframe["test"] = dataframe["t"].rolling(window = 2).mean()


#for i in range(len(dataframe)):
#	try:
#		dataframe.loc[i, "test2"] = dataframe["t"][i-2:i +1].mean()
#	except:
#		pass


print(dataframe)
#print(dataframe["mean"][0:4])

#general formula
width = 3
temps = pd.DataFrame(series.values)
dataframe = concat([temps.shift(width -1).rolling(window = width).min(), temps.shift(width -1).rolling(window = width).max(), temps.shift(width -1).rolling(window = width).mean(), temps], axis = 1)
dataframe.columns = ["min", "max", "mean", "t+1"]
print(dataframe)


fig, ax = plt.subplots(1)
ax.plot(series["Temp"])
date_format = mpl_dates.DateFormatter("%d %b %Y")
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()

plt.show()

series["Temp"].hist()
plt.show()

series["Temp"].plot(style = "k.")
plt.show()

series["Temp"].plot(kind = "kde")
plt.show()

groups = series.groupby(Grouper(freq = "A"))
years = concat([DataFrame(x[1].values) for x in groups], axis = 1)
years.columns = range(1981, 1991)
years.boxplot()
plt.show()

years.plot(subplots = True)
plt.show()


one_year = series["1990"]
groups = one_year.groupby(Grouper(freq = "M"))
months = concat([DataFrame(x[1].values) for x in groups], axis =1)
months.columns = range(1, 13)
months.boxplot()
plt.show()

groups = series.groupby(Grouper(freq = "A"))
years = concat([DataFrame(x[1].values) for x in groups], axis = 1)
years.columns = range(1981, 1991)
print(years)
years = years.T
print(years)
plt.matshow(years, interpolation = None, aspect = "auto")
plt.show()


one_year = series["1990"]
groups = series.groupby(Grouper(freq = "M"))
months = concat([DataFrame(x[1]) for x in groups], axis = 1)
months = months.T
plt.matshow(years, interpolation = None, aspect = "auto")
plt.show()


lag_plot(series)
plt.show()

values = pd.DataFrame(series["Temp"].values)
lags = 7
l = [values]
for i in range(1, lags +1):
	l.append(values.shift(i))
dataframe = concat(l, axis = 1)
names = ["t"]
for i in range(1, lags + 1):
	names.append("t-" + str(i))
dataframe.columns = names
print(dataframe)

for i in range(1, lags +1):
	ax = plt.subplot(3, 3, i)
	ax.set_title("t-" + str(i))
	plt.scatter(x=dataframe[ 't' ].values, y=dataframe[ 't-' +str(i)].values)
plt.show()
	
autocorrelation_plot(series["Temp"])
plt.show()
'''

def parser(x):
	return datetime.strptime("199" + x, "%Y-%m")

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/shampoo.csv", index_col = 0, header = 0, parse_dates = True, date_parser = parser)
'''
upsampled = series.resample("D").mean()
interpolated = upsampled.interpolate(method = "linear")
print(interpolated)
fig, ax = plt.subplots()
ax.plot(interpolated["Sales"])
date_format = mpl_dates.DateFormatter('%d %b %Y')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate() 
plt.show()

upsampled = series.resample("D").mean()
interpolated = upsampled.interpolate(method = "spline", order = 2)
print(interpolated)
fig, ax = plt.subplots()
ax.plot(interpolated["Sales"])
date_format = mpl_dates.DateFormatter("%d %b %Y")
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate() 
plt.show()
'''
print(series)
downsampled = series.resample("Q").mean()
print(downsampled)
fig, ax = plt.subplots()
ax.plot(downsampled["Sales"])
date_format = mpl_dates.DateFormatter("%d %b %Y")
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()
plt.show()


downsampled = series.resample("A").mean()
print(downsampled)
fig, ax = plt.subplots()
ax.plot(downsampled["Sales"])
date_format = mpl_dates.DateFormatter("%d %b %Y")
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()
plt.show()


downsampled = series.resample("A").sum()
print(downsampled)
fig, ax = plt.subplots()
ax.plot(downsampled["Sales"])
date_format = mpl_dates.DateFormatter("%d %b %Y")
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()
plt.show()
