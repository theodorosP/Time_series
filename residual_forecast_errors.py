from numpy.core.fromnumeric import reshape
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-total-female-births.csv", header = 0, index_col= 0, parse_dates= True)
df = pd.concat([series.shift(1), series] , axis =1)
df.columns = ["t", "t+1"]
train_size = int(len(series)*0.66)
X = df.values
train = X[1 : train_size]
test = X[train_size : len(X)]
test_x = test[:, 0]
test_y = test[:, 1]
train_x = train[:, 0]
train_y = train[:, 1]

predictions = [i  for i in test_x]
actuals = [i for i in test_y]

plt.plot(actuals)
plt.plot([None for i in actuals] + [j for j in predictions], label = "predictions")
plt.plot([None for i in actuals] + [j for j in actuals], label = "train")
plt.legend(loc = "best")
plt.show()

residuals = [actuals[i] - predictions[i] for i in range (len(predictions))]
print(residuals)

plt.plot(residuals)
plt.show()

res_df = pd.DataFrame(residuals)
print(res_df.describe())
#add the mean to the prediction to improve the model

res_df.hist()
plt.show()

res_df.plot(kind= "kde")
plt.show()