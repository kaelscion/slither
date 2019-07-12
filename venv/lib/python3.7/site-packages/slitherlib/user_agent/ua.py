from bs4 import BeautifulSoup
from random import choices
from slitherlib.config import Config

import requests

class UserAgent:

    ua_source_url = Config.UA_SOURCES[0]

    def __init__(self, thread_count=1):
        if thread_count == 'all':
            self.thread_uas = self.get_ua_list()
        else:
            self.thread_uas = choices(self.get_ua_list(), k=thread_count)

    def __repr__(self):
        return self.thread_uas

    def get_ua_list(self, source=ua_source_url):
        r = requests.get(source)
        soup = BeautifulSoup(r.content, "html.parser")
        tables = soup.find_all('table')
        return [table.find('td').text for table in tables]

    
