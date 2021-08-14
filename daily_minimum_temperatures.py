import pandas as pd
from pandas import read_csv, DataFrame
from pandas import concat
from pandas import Grouper
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot
from pandas.plotting import autocorrelation_plot
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf
import numpy as np

series = read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-min-temperatures.csv", index_col = 0, header = 0, squeeze = True, parse_dates = True)
#print(series.values)
print(series)


#date time features
df = DataFrame()
df["year"] = [series.index[i].year for i in range (len(series))]
df["month"] = [series.index[i].month for i in range (len(series))]
df["day"] = [series.index[i].day for i in range (len(series))]
df["Temperature"] = [series[i] for i in range (len(series))]
print(df)


#lag fetures
temperatures = DataFrame(series.values)
df1 = concat([temperatures.shift(3), temperatures.shift(2), temperatures.shift(1), temperatures], axis =1)
df1.columns = ["t - 2", "t -1", "t", "t + 1"]
print(df1.head(5))



#rolling window statistics
temperatures = DataFrame(series.values)
df2 = concat([temperatures.shift(1).rolling(window = 2).mean(), temperatures], axis = 1) 
df2.columns = [ ' mean(t-1,t) ' , ' t+1 ' ]
print(df2.head(5))

#general formula for rolling window
temperatures = DataFrame(series.values)
width = 3
df2 = concat([temperatures.shift(width -1).rolling(window =width).min(), temperatures.shift(width - 1).rolling(window = width).mean(), temperatures.shift(width - 1).rolling(window = width).max(), temperatures], axis = 1)
df2.columns = ["min", "mean", "max", "t + 1"]
print(temperatures.head(10))
print(df2.head(10))


#expanding window statistics
temperatures = DataFrame(series.values)
df2 = concat([temperatures.expanding().min(), temperatures.expanding().mean(), temperatures.expanding().max(), temperatures.shift(-1)], axis = 1 )
df2.columns = ["min", "mean", "max", "t + 1" ]
print(df2)

#ploting
plt.figure(1)
series.plot()
plt.title("Temperatures vs Dates")
plt.show()

plt.figure(1)
plt.title("Temperature vs Date \n scatter")
series.plot(style = ".k")
plt.show()

years = DataFrame()
groups = series.groupby(Grouper(freq = "A" ))
for i, j in groups:
	print(" i = ", i)
	print(" j.values = ", j.values)
	print("*"*80)
for i , j in groups:
	years[i.year] = j.values
print(years)

groups = series.groupby(Grouper(freq = "A" ))
years = concat([DataFrame(x[1].values) for x in groups ] , axis = 1)
years.columns = range(1981, 1991)
print(years)


years.plot(subplots = True, legend = False)
plt.show()

#histogram
plt.figure()
series.hist()
plt.show()

#density plot
plt.figure()
series.plot(kind = "kde")
plt.show()


#boxplot
years.boxplot()
plt.show()


#boxplot one year
one_year = series["1990"]
groups = one_year.groupby(Grouper(freq = "M"))
months = concat([DataFrame(x[1].values) for x in groups ], axis = 1)
months.columns = range(1, 13)
months.boxplot()
plt.show()
print(months)


#Heat map for 10 years
groups = series.groupby(Grouper(freq = "A"))
years = concat([DataFrame(x[1].values) for x in groups], axis = 1)
years.columns = range(1981, 1991)
years = years.T
print(years)
plt.matshow(years, interpolation = None, aspect = "auto")
plt.show()


#Heat map for a year
year = series["1990"]
groups = year.groupby(Grouper(freq = "M"))
months = concat([DataFrame(x[1].values) for x in groups] , axis = 1)
months.columns = range(1, 13)
plt.matshow(months, interpolation = None, aspect = "auto")
plt.show()
print(months)


#lag plots
lag_plot(series, lag =1)
plt.show()

#autocorelation method 1
autocorrelation_plot(series)
plt.show()

#autocorelation method 2
plot_acf(series)
plt.show()
