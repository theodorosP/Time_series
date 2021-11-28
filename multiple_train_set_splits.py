from matplotlib import colors
from numpy.lib.shape_base import column_stack
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.model_selection as sms

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/monthly-sunspots.csv", header = 0 , index_col= 0 , parse_dates = True)
columns = [col for col in series.columns]
values = series["Sunspots"].values
print(values)
splits = sms.TimeSeriesSplit(n_splits = 3).split(values)
index = 1

for train_index , test_index in splits:
    train = values[train_index]
    test = values[test_index]
    print("train = ", train)
    print("test = ", test)
    plt.subplot(310 + index)
    plt.plot(train, color = "blue", label = "train")
    plt.plot([None for i in train] + [j for j in test], color = "green", label = "rest" )
    plt.legend(loc = "best")
    index = index + 1
plt.show()