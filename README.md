# slither
A simple, easy to use framework for adding randomized, anonymous IP addresses and user-agents to web scrapers, crawlers, and penetration testing solutions

Slither is designed to add randomized User-Agent strings and Anonymous IP addresses from proxy sources around the web for use in your
web scraping, penetration testing, or data aggregation projects. Please respect the owners and hardware of the data you are scraping.
**I BEAR NO RESPONIBILITY IF YOU USE THIS SOFTWARE WITHOUT PERMISSION OR TO DO HARM TO WEB ASSETS. RESPECT THE DATA AND PLATFORMS. BE ETHICAL
WITH YOUR SCRAPING AND UNDERSTAND THAT ALL ASSETS HAVE FINITE RESOURCES. DONT DDOS THINGS. ITS BAD.**

To use slither, download this package, add it to your scraper project's directory structure, and `pip install -r requirements.txt`

From there, simply `from slither import Slither` to add the package to the project file that contains your scraping code.

Each instance of the Slither class has two variables, `ip` and `ua` for IP Address and User-Agent respectively. The IPs are
pulled, in real time, from web proxy sources every time you declare and instance of the Slither class so no need to worry about
IPs going stale. The majority of the addresses are less than 20 minutes old when pulled down and many are less than 10.
An example of anonymizing your scraper with the Requests library looks like this:

```python
import requests

from random import choice
from slither import Slither

new_slither = Slither(thread_count=1)

headers = {
    "User-Agent" : choice(new_slither.uas)
    }
    
requests.get('https://www.example.com', headers=headers, proxies=choice(new_slither.ips)
```
This method also supports concurrency and adding an individual IP and/or UA to each thread or process that is spawned by your
project! Accomplishing this is done as follows:

```python
import requests

from slither import Slither
from concurrent.futures import ThreadPoolExecutor, wait, as_completed

#specify the number of threads your scraper will use as the "thread count".
#To get all available IPs and User-Agent strings, pass "all" to `thread_count` rather than an int

num_of_threads = 7
futures = list_of_urls_to_scrape
new_slither = Slither(thread_count=num_of_threads)
#returns a list of dictionaries of IPs and User-Agents
for i in new_slither.masks:
    #spawn your threads here assigning i['address'] to your thread's proxy parameter and 
    #i['user-agent'] to each thread's 'User-Agent' header parameter
    ...
        
        
Have fun and happy Scraping!


