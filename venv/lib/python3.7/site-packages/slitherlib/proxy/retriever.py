import requests

from slitherlib.config import Config
from random import choices
from bs4 import BeautifulSoup

class Retriever:

    def __init__(self, thread_count=all):
        self.s = requests.Session()
        self.sources = Config.PROXY_SOURCES
        if thread_count == 'all':
            self.thread_ips = self.clean_and_sort(self.connect_and_parse())
        else:
            self.thread_ips = choices(self.clean_and_sort(self.connect_and_parse()), k=thread_count)

    def __repr__(self):
        return f'<ProxyRetriever object containing {len(self.thread_ips)} addresses>'

    def connect_and_parse(self):
        website = self.sources[0]
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
        ip_list = []
        for item in data_set:
            ip_list.append(f'{item[0]}:{item[1]}')
        return ip_list