import pandas as pd

from first import df10
from second import df11
from third import df12
#from fourth import df13
#from fifth import df14
#from sixth import df15
#from seventh import df16
#from eighth import df17
#from ninth import df18
#from tenth import df19
#from eleventh import df21

OUTFILE = 'stats.csv'

#массив датасетов по годам
#!!!создание датасета можно желать через цикл
#через массив и вазвать все парсеры

dfа = pd.merge(df10, df11, how='outer')

dfа.to_csv(OUTFILE)