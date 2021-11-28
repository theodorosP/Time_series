from random import gauss
from random import seed
import pandas as pd
from pandas.plotting import autocorrelation_plot
import matplotlib.pyplot as plt

seed(1)
series = [gauss(0, 1) for i in range(1,1000)]
series = pd.DataFrame(series)
print(series)
print(series.describe())
series.plot()
plt.show()
series.hist()
plt.show()
autocorrelation_plot(series)
plt.show()
