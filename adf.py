import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as smst

rd.seed(1)
random_walk = []
if rd.random() < 0.5:
	random_walk.append(-1)
else:
	random_walk.append(1)

for i in range(1, 1000):
	if rd.random() < 0.5:
		movement = -1
	else:
		movement = 1
	step = random_walk[i - 1] + movement
	random_walk.append(step)
series = pd.DataFrame(random_walk)
series.columns = ["values"]
series.plot() 
plt.show()
results = smst.adfuller(series)
print("ADF statistics: ", results[0])
#p_value < 0.05 stationary data. p_values > 0.05 not stationary data
print("p value: ", results[1])
for i, j in results[4].items():
	print(i, round(j,2))
diff = list()
for i in range(1, len(random_walk)):
	value = random_walk[i] - random_walk[i - 1]
	diff.append(value)
series = pd.DataFrame(diff)
results = smst.adfuller(diff)
#p value  < 0.05 stationary, else non stationary data
print("p value: ", results[1])
