import pandas as pd
import matplotlib.pyplot as plt

series = pd.read_csv("path/to/the/file", header = 0, index_col = 0, parse_dates = True)

def box_plot(data_set, start, end)
      # i.e start, end = "1993"
      years = series[start : end]
      groups = years.groupby(pd.Grouper(freq = "A"))
      df_years = pd.concat([pd.DataFrame(x[1].values) for x in groups ], axis = 1)
      df_years.boxplot()
      plt.show()

      
