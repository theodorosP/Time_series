import pandas as pd
import matplotlib.pyplot as plt 
import statsmodels.tsa.stattools as sts

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-total-female-births.csv", header= 0 , index_col= 0 , parse_dates= True)
columns = [col for col in series.columns]
values = sts.adfuller(series[columns[0]])
#If statistics is negative, then series is more likely to be stable, reject null hypothesis 
print("Statistics: %f" %values[0])
# p values less than 0.05, time series is stable
print("P-value: %f" %values[1])
for i, j in values[4].items():
    print(i, round(j, 3))

#statistics give a result less than -4 . 1% gives statistics -3.449. This suggests that we can reject the null hypothesis with a significance level of less than 1%\
