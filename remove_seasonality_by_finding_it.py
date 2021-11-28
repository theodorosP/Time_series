import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-min-temperatures.csv", index_col = 0, header=0, parse_dates= True )

x = [i%365 for i in range (len(series))]
columns = [col for col in series.columns]
print(columns)
y = series[columns[0]].values
deg = 4
coef = np.polyfit(x, y, deg)
curve = list()
for i in range(len(series)):
    values = coef[-1]
    for d in range(deg):
        values = values + x[i]**(deg - d) * coef[d]
    curve.append(values)  

plt.rcParams["figure.figsize"] = [14, 7]
plt.rc("font", size = 14)
fig, ax = plt.subplots()
ax.plot(y)
ax.plot(curve, linewidth = 4)
plt.show()

deseasonaled = [y[i] - curve[i] for i in range(len(series))]
print(deseasonaled)
plt.plot(deseasonaled)
plt.show()