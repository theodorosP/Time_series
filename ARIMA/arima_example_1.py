import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pandas.plotting import autocorrelation_plot 
import statsmodels.api as sm
import warnings


def parser(x):
    return datetime.strptime("190" +x , "%Y-%m")
series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/shampoo.csv", header= 0 , index_col= 0 , parse_dates= True, date_parser=parser)
print(series)

columns = list()
for col in series.columns:
    columns.append(col)


series.plot()
plt.show()

autocorrelation_plot(series)
plt.show()
warnings.filterwarnings("ignore")

model = sm.tsa.arima.ARIMA(series, order=(5, 1, 0))
#model = ARIMA(series, order=(5, 1, 0))
model_fit = model.fit()
print(model_fit.summary())

residuals = pd.DataFrame(model_fit.resid)
residuals.plot()
plt.show()

residuals.plot(kind="kde")
plt.show()

