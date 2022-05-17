import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL = "https://rigf2011.ru/prog/?p=speakers"

r = requests.get(URL)
print(r.status_code)

def parse(url = URL) :
    pattern = {'surname': [], 'name': [], 'org': [], 'region': [], 'year': []}
    soup = bs(r.text, "html.parser")
    #забираем часть строк таблицы
    sheet = soup.find('table', class_='tbl')
    # удаляем ненужное
    sheet.tr.decompose()
    for cell in sheet :
        try:
            pattern['surname'].append(cell.contents[1].text)
            pattern['name'].append(cell.contents[2].text)
            pattern['org'].append(cell.contents[3].text)
            pattern['region'].append(cell.contents[4].text)
            pattern['year'].append('2011')
        except AttributeError:
            pass
    return pattern

df11 = pd.DataFrame(data=parse())


