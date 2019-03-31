from bs4 import BeautifulSoup

import random
import requests

class UserAgent:

    ua_source_url='https://deviceatlas.com/blog/list-of-user-agent-strings#desktop'

    def __init__(self):
        self.new_ua = random.choice(self.get_ua_list())

    def get_ua_list(self, source=ua_source_url):
        r = requests.get(source)
        soup = BeautifulSoup(r.content, "html.parser")
        tables = soup.find_all('table')
        return [table.find('td').text for table in tables]

    def __repr__(self):
        return self.new_ua
