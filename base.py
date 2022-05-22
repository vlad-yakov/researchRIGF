import pandas as pd
from firstPart import df1
from secondPart import df2

import matplotlib.pyplot as plt

#слияние датасетов в выгрузка в файл
OUTFILE = 'stats.csv'
dfа = pd.merge(df1, df2, how='outer')
dfа.to_csv(OUTFILE)

fig = plt.figure()
# Добавление на рисунок прямоугольной (по умолчанию) области рисования
fig.add_axes([0, 0, 1, 1])
plt.scatter(1.0, 1.0)
plt.show