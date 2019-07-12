import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    
    PROXY_SOURCES = [
        'https://www.free-proxy-list.net',
        'http://www.spys.one/en/',
        'https://www.hide-my-ip.com/proxylist.shtml'
    ]

    UA_SOURCES = [
        'https://deviceatlas.com/blog/list-of-user-agent-strings#desktop'
   ]

