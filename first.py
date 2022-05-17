import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL = "https://rigf2010.ru/rus/speakers.php"


r = requests.get(URL)
print(r.status_code)

def parse(url = URL) :
    pattern = {'surname': [], 'name': [], 'org': [], 'region': [], 'year': []}
    soup = bs(r.text, "html.parser")
    #забираем часть строк таблицы
    sheet = soup.find_all('tr')[4:-2]
    for cell in sheet :
        fname = cell.contents[3].text.split()
        pattern['surname'].append(fname[0])
        pattern['name'].append(fname[1])
        pattern['org'].append(cell.contents[5].text)
        pattern['region'].append(cell.contents[7].text)
        pattern['year'].append('2010')
    return pattern

df10 = pd.DataFrame(data=parse())



