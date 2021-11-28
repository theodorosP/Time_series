from random import seed
import pandas as pd
from random import randrange
import matplotlib.pyplot as plt


seed(1)
series = pd.DataFrame([randrange(-10, 10) for i in range(0, 1000)])
series.plot()
plt.show()


