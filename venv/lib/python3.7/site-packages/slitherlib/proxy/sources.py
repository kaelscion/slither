import requests

from bs4 import BeautifulSoup

class Source():

    url = None

    def __init__(self):
        self.s = requests.Session()

    def get_markup(self, source):
        r = self.s.get(source)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup

class FreeProxyList(Source):

    url = 'https://www.free-proxy-list.net'

    def connect_and_parse(self, soup_obj):
        proxy_table = soup_obj.find('tbody')
        proxy_list = proxy_table.find_all('tr')
        elites = [tr for tr in proxy_list if 'elite' in tr.text]
        tds = []
        for tr in elites:
            tds.append([td.text.strip() for td in tr])   
        return tds

class HideMyIP(Source):
    
    url = "https://www.hide-my-ip.com/proxylist.shtml"
    
    def get_markup(self):
        r = self.s.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup
        
    def connect_and_parse(self):
        proxy_table = self.get_markup().find("tbody")
        breakpoint()
        proxy_list = proxy_table.find_all('tr')
        breakpoint()
        proxies = [td for td in proxy_list if td.text]
        breakpoint()
        addresses = []
        for proxy in proxies:
           addresses.append(f'{proxy[0].text.strip()}:{proxy[1].text.strip()}')
        return addresses



        