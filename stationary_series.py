import pandas as pd
import matplotlib.pyplot as plt

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/daily-total-female-births.csv", header = 0, index_col= 0 , parse_dates= True)
print(series)
series.plot()
plt.show()