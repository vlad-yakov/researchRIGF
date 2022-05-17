import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL = "https://rigf2012.ru/prog/?p=speakers"

r = requests.get(URL)
print(r.status_code)

def parse(url = URL) :
    pattern = {'surname': [], 'name': [], 'org': [], 'region': [], 'year': []}
    soup = bs(r.text, "html.parser")
    #забираем строки с определённым фоном
    sheet = soup.find_all(attrs={'style': ['background-color:#FFFFFF','background-color:#e9e7ef']})
    for cell in sheet :
        pattern['surname'].append(cell.contents[1].text)
        pattern['name'].append(cell.contents[2].text)
        pattern['org'].append(cell.contents[3].text)
        pattern['region'].append(cell.contents[4].text)
        pattern['year'].append('2012')
    return pattern

df12 = pd.DataFrame(data=parse())

parse()