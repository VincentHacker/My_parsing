# valuta.kg
# python3 -m venv venv - для начала нужно установить venv через sudo apt и т.д. (установлено)
# . venv/bin/add_activate
# делаем в json (до этого делали в csv) 


# {'USD': {'покупка': 12, 'продажа': 12}}

# установить venv
# pip install -r requirements.txt
# pypi.org - там библиотеки

# pip freeze - показывает все что установлено в виртуальной папке venv:
# beautifulsoup4==4.11.1
# certifi==2022.5.18.1
# charset-normalizer==2.0.12
# idna==3.3
# lxml==4.9.0
# requests==2.27.1
# soupsieve==2.3.2.post1
# urllib3==1.26.9

import requests
from bs4 import BeautifulSoup

URL = 'https://www.nbkr.kg/index.jsp?lang=RUS'

def get_html(url):
    response = requests.get(url).text
    return response

def get_table(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find_all('div', class_ = 'sticker-body')
    return table[2]
# это функциональное программирование, до этого писали процедурное программирование

def get_data(table: BeautifulSoup):
    names = table.find_all('td', class_ = 'excurr')
    prices = table.find_all('td', class_ = 'exrate')
    names_ = [i.text for i in names if '/' in i.text]
    prices_ = [i.text for i in prices]
    a = {
        names_[0]: prices_[0],
        names_[1]: prices_[2],
        names_[2]: prices_[4],
        names_[3]: prices_[6],


    }
    # print(names_)
    # print(prices_)
    return a

def write_to_json(data):
    import json
    with open('rate.json', 'w') as file:
        json.dump(data, fp = file, indent = 4)

def parse():
    html = get_html(URL)
    table = get_table(html)
    data = get_data(table)
    write_to_json(data)

if __name__ == '__main__': # срабатывает только в этом модуле
    parse()


# fastapi, djangoapi








