import pandas as pd
import statsmodels.tsa.seasonal as stat
import random as rd
import matplotlib.pyplot as plt

series = []
for i in range (1,100):
	series.append(i + rd.randrange(10))
#results = stat.seasonal_decompose(series, model = "additive", freq = 1)
#results.plot()
#plt.show()

df = pd.DataFrame(series)
print(df)

#frequency every day new data
results = stat.seasonal_decompose(df, model = "additive", freq = 1)
results.plot()
plt.show()

