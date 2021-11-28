import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.tsa.seasonal as stm

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/airline-passengers.csv", header = 0, index_col= 0 , parse_dates= True )
print(series)
results = stm.seasonal_decompose(series, model = "additive")
print("---")
results.plot()
plt.show()