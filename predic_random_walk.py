import random as rd
import pandas as pd
import math as math
import sklearn.metrics as sk

rd.seed(1)
random_walk = []
if rd.random() < 0.5:
	random_walk.append(-1)
else:
	random_walk.append(-1)

for i in range(0, 1000):
	if rd.random() < 0.5:
		random_walk.append(random_walk[-1] -1)
	else:
		random_walk.append(random_walk[-1] + 1)
df = pd.DataFrame(random_walk)
df.columns = ["random walk"]
print(df)

train_size = int((len(df) * 0.66))
train = random_walk[ : train_size]
test = random_walk[train_size : ]
res = "\n".join("{} {}".format(x, y) for x, y in zip(test, train))
print(res)
history = train[-1]
predict = list()
for i in range(len(test)):
	yhat = history
	predict.append(yhat)
	history = test[i]
rmse = math.sqrt(sk.mean_squared_error(test, predict))
print(rmse)
