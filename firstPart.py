import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

pattern = {'surname': [], 'name': [], 'org': [], 'region': [], 'year': []}

def first(url = "https://rigf2010.ru/rus/speakers.php") :
    r = requests.get(url)
    print(r.status_code)
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

first()

#_________________________________________________________________

def second(url = "https://rigf2011.ru/prog/?p=speakers") :
    r = requests.get(url)
    print(r.status_code)
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

second()

#_________________________________________________________________

URLS = ["https://rigf2012.ru/prog/?p=speakers",
        "https://rigf2013.ru/prog/?p=speakers",
        "https://rigf2014.ru/prog/?p=speakers"]

def third_fifth() :
    for url in URLS :
        r = requests.get(url)
        print(r.status_code)
        soup = bs(r.text, "html.parser")
        #забираем строки с определённым фоном
        sheet = soup.find_all(attrs={'style': ['background-color:#FFFFFF','background-color:#e9e7ef']})
        for cell in sheet :
            pattern['surname'].append(cell.contents[1].text)
            pattern['name'].append(cell.contents[2].text)
            pattern['org'].append(cell.contents[3].text)
            pattern['region'].append(cell.contents[4].text)
            pattern['year'].append(url[12:16])
    return pattern

#выгружаем весь массив во фрейм
df1 = pd.DataFrame(data= third_fifth())





