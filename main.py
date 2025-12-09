import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from firstPart import df1
from secondPart import df2

# объединение фреймов данных, вывод в csv
OUTFILE = 'stats.csv'
df = pd.merge(df1, df2, how='outer')
df.to_csv(OUTFILE)

plt.interactive(True)
fig = plt.figure()
plt.scatter(1.0, 1.0)

plt.show()

# закуск проекта из этого файла
