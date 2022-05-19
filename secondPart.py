import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import csv

URLS = ["https://rigf2015.ru/prog/?p=speakers",
       "https://rigf2016.ru/prog/?p=speakers",
       "https://rigf2017.ru/prog/?p=speakers",
       "https://rigf2018.ru/prog/?p=speakers",
       "https://rigf2019.ru/prog/?p=speakers",
       "https://rigf2021.ru/prog/?p=speakers"]

def parse() :
    pattern = {'surname': [], 'name': [], 'org': [], 'region': [], 'year': []}
    for url in URLS :
        r = requests.get(url)
        print(r.status_code)
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
                pattern['year'].append(url[12:16])
    return pattern

df2 = pd.DataFrame(data=parse())

