import pandas as pd
from firstPart import df1
from secondPart import df2

OUTFILE = 'stats.csv'

dfа = pd.merge(df1, df2, how='outer')

dfа.to_csv(OUTFILE)