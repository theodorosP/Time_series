import random as rd
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import autocorrelation_plot

random_walk = []
rd.seed(1)
if rd.random() < 0.5:
	random_walk.append(-1)
else:
	random_walk.append(1)
movement = []
value = []
for i in range(0, 1000):
	if rd.random() < 0.5:
		movement.append(-1)
	else:
		movement.append(1)
	value = random_walk[i-1] + movement[i]
	random_walk.append(value)
print(random_walk)
series = pd.DataFrame(random_walk)
series.columns = ["values"]
print(series)
series.plot()
plt.show()
autocorrelation_plot(series)
plt.show()

