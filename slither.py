from proxy_retriever import proxyRetriever as pr
from user_agent import UserAgent as ua


class Slither:

    def __init__(self):
        self.ip = pr()
        self.ua = ua()

