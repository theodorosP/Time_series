import pandas as pd
from pandas.core.indexing import check_bool_indexer
from datetime import datetime
import matplotlib.pyplot as plt

def parser(x):
    return datetime.strptime( '190' +x, '%Y-%m' )

series = pd.read_csv("/home/thodoris/Downloads/mashine_learning/Datasets-master/shampoo.csv", header = 0, index_col = 0, parse_dates= True, date_parser= parser)

columns = list()
for i in series.columns:
    columns.append(i)

values = list()
for i in range(1, len(series)):
        diff = series["Sales"][i] - series["Sales"][i-1]
        values.append( diff)
print(values)

plt.plot(values)
plt.show()
