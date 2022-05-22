import pandas as pd
from firstPart import df1
from secondPart import df2

import matplotlib.pyplot as plt

#слияние датасетов в выгрузка в файл
OUTFILE = 'stats.csv'
dfа = pd.merge(df1, df2, how='outer')
dfа.to_csv(OUTFILE)


