import pandas as pd
from firstPart import df1
from secondPart import df2

import numpy as np
import matplotlib.pyplot as plt

#объединение фреймов данных, вывод в csv
OUTFILE = 'stats.csv'
dfа = pd.merge(df1, df2, how='outer')
dfа.to_csv(OUTFILE)

fig = plt.figure()
plt.scatter(1.0, 1.0) 
plt.show()
