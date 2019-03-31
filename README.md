# slither
A simple, easy to use framework for adding randomized, anonymous IP addresses and user-agents to web scrapers, crawlers, and penetration testing solutions

Slither is designed to add randomized User-Agent strings and Anonymous IP addresses from proxy sources around the web for use in your
web scraping, penetration testing, or data aggregation projects. Please respect the owners and hardware of the data you are scraping
I BEAR NO RESPONIBILITY IF YOU USE THIS SOFTWARE WITHOUT PERMISSION OR TO DO HARM TO WEB ASSETS. RESPECT THE DATA AND PLATFORMS. BE ETHICAL
WITH YOUR SCRAPING AND UNDERSTAND THAT ALL ASSETS HAVE FINITE RESOURCES. DONT DDOS THINGS. ITS BAD.

To use slither, download this package, add it to your scraper project's directory structure, and `pip install -r requirements.txt`

From there, simply `from slither import Slither` to add the package to the project file that contains your scraping code.

Each instance of the Slither class has two variables, `ip` and `ua` for IP Address and User-Agent respectively. The IPs are
pulled, in real time, from web proxy sources every time you declare and instance of the Slither class so no need to worry about
IPs going stale. The majority of the addresses are less than 20 minutes old when pulled down and many are less than 10.
An example of anonymizing your scraper with the Requests library looks like this:

```python
import requests

from bs4 import BeautifulSoup
from slither import Slither

headers = {
    "User-Agent" : Slither().ua
    }
    
requests.get('https://www.example.com', headers=headers, proxies=Slither().ip)
```
This method also supports concurrency and adding an individual IP and/or UA to each thread or process that is spawned by your
project! Have fun and happy scraping!
