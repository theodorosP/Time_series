from pandas import read_csv
import pandas as pd

series = read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-total-female-births.csv", header = 0, index_col = 0,  parse_dates = True, squeeze = True )
#header =  0 --> name of columns in first row
#parse_date = True first column has dates that need to be parsed
#index_col = 0, column number 0 is the index
#squeeze = True We hint that we only have one data column and that we are interested in a Series and not a DataFrame 
print(series)
print(type(series))
print(series.head())
print(series.head(10))
print(series.size)
print(len(series))
print(series["1959-"])
print(series["1959-01-01"])
print(series.describe())
'''
df = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-total-female-births.csv")
#df.set_index('Date', inplace=True)
print(df)

for col in df.columns:
	print(col)

'''

