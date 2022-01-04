import pandas as pd
import matplotlib.pyplot as plt
import pandas.plotting as pdpl
from statsmodels.graphics.tsaplots import plot_acf

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-min-temperatures.csv", header= 0 , index_col= 0, parse_dates= True)
print(series)
pdpl.lag_plot(series)
plt.show()

df = pd.DataFrame()
df = pd.concat([series.shift(1), series], axis = 1)
df.columns = ["t", "t+1"]

results = df.corr()
print(results)


plot_acf(series, lags = 400)

plt.show()