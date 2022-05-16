import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL = "https://rigf2021.ru/prog/?p=speakers"
OUTFILE = 'stats.csv'

r = requests.get(URL)
print(r.status_code)

def parse(url = URL) :
    pattern = {'surname': [], 'name': [], 'org': [], 'region': []}
    soup = bs(r.text, "html.parser")
    #забираем строки таблицы
    cells = soup.find_all('tr')
    for cell in cells :
        # исключаем шапку таблицы
        if cell.td :
            pattern['surname'].append(cell.contents[1].text)
            pattern['name'].append(cell.contents[2].text)
            pattern['org'].append(cell.contents[3].text)
            pattern['region'].append(cell.contents[4].text)
    return pattern

df = pd.DataFrame(data=parse())

df['year'] = '2021'

df.to_csv(OUTFILE)