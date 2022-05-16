import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL = "https://rigf2010.ru/rus/speakers.php"
OUTFILE = 'stats.csv'

r = requests.get(URL)
print(r.status_code)

def parse(url = URL) :
    pattern = {'surname': [], 'name': [], 'org': [], 'region': [], 'year': ['2010']}
    soup = bs(r.text, "html.parser")
    #забираем строки таблицы
    sheet = soup.find_all('table')
    cells = sheet[2].contents

    print(cells)

#df = pd.DataFrame(data=parse())
#df.to_csv(OUTFILE)

parse()
