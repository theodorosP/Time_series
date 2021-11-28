import pandas as pd
import matplotlib.pyplot as plt

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/monthly-sunspots.csv", header= 0, index_col= 0, parse_dates= True )
columns = [col for col in series.columns]
vals = series[columns[0]].values
n_train = 500

for i in range (n_train , len(vals)):
    train = vals[0: i]
    test = vals[i: i+1]
    print("train, test:" , len(train), len(test))
