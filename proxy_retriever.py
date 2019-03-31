import requests
from random import choice

from bs4 import BeautifulSoup

class proxyRetriever:

    def __init__(self):
        self.s = requests.Session()

    def __repr__(self):
        return choice(self.clean_and_sort(self.connect_and_parse()))['Address']

    def connect_and_parse(self, website="https://www.free-proxy-list.net"):
        r = self.s.get(website)
        soup = BeautifulSoup(r.text, "html.parser")
        proxy_table = soup.find('tbody')
        proxy_list = proxy_table.find_all('tr')
        elites = [tr for tr in proxy_list if 'elite' in tr.text]
        tds = []
        for tr in elites:
            tds.append([td.text.strip() for td in tr])   
        return tds

    def clean_and_sort(self, data_set):
        columns = ['Address', 'Port', 'Country_Code', 'Country', 'Proxy_Type']
        for item in data_set:
            ip_list = []
            ip_list.append({column : i.strip() for (column, i) in zip(columns, item)})
        return ip_list
            
