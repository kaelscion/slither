# slither
A simple, easy to use framework for adding randomized, anonymous IP addresses and user-agents to web scrapers, crawlers, and penetration testing solutions

Slither is designed to add randomized User-Agent strings and Anonymous IP addresses from proxy sources around the web for use in your web scraping, penetration testing, or data aggregation projects. Please respect the owners and hardware of the data you are scraping. **I BEAR NO RESPONIBILITY IF YOU USE THIS SOFTWARE WITHOUT PERMISSION OR TO DO HARM TO WEB ASSETS. RESPECT THE DATA AND PLATFORMS. BE ETHICAL WITH YOUR SCRAPING AND UNDERSTAND THAT ALL ASSETS HAVE FINITE RESOURCES. DONT DDOS THINGS. ITS BAD.**

**SLITHER IS ONYL COMPATIBLE WITH PYTHON 3. NO SUPPORT FOR PYTHON 2 IS PLANNED**. That being said, to install on a machine with only Python 3 installed:

`pip install slitherlib`

On a machine with both Python 2 and 3 installed:

`pip3 install slitherlib`

From there, simply from slitherlib.slither import Snake to add the package to the project file that contains your scraping code.

Each instance of the Slither class has two variables, ip and ua for IP Address and User-Agent respectively. The IPs are pulled, in real time, from web proxy sources every time you declare and instance of the Slither class so no need to worry about IPs going stale. The majority of the addresses are less than 20 minutes old when pulled down and many are less than 10. An example of anonymizing your scraper with the Requests library looks like this:

```python
import requests

from random import choice
from slitherlib.slither import Snake

s = requests.Session()
snake = Snake()
ip_addresses = snake.ips
user_agents = snake.uas
headers = {
    "User-Agent" : choice(user_agents)
    }
try:
    ip = ip_addresses.pop()
    r = s.get('https://www.google.com', proxies={'https' : ip, 'http' : ip} , headers=headers)
    print(r.status_code)
except requests.exceptions.ProxyError:
    print('Proxy Timed Out. Removing and Retrying')
    ip = ip_addresses.pop()
    r = s.get('https://www.google.com', proxies={'https' : ip, 'http' : ip} , headers=headers)
except IndexError:
    print("We've run out of IPs and/or User-Agents! Re-run your script to get more!")
```

This method also supports concurrency and adding an individual IP and/or UA to each thread or process that is spawned by your project! Accomplishing this is done as follows:

```python
import requests

from slither import Slither
from concurrent.futures import ThreadPoolExecutor, wait, as_completed

# specify the number of threads your scraper will use as the "thread count".
# By default, thread_count is set to "all", meaning that you will pull down all available IP addresses and user agents. To specify a specific number, pass the number of desired items as an int to the named `thread_count` argument

num_of_threads = 7
futures = list_of_urls_to_scrape
new_slither = Slither(thread_count=num_of_threads)
#returns a list of dictionaries of IPs and User-Agents
for i in new_slither.masks:
    #spawn your threads here assigning i['address'] to your thread's proxy parameter and 
    #i['user-agent'] to each thread's 'User-Agent' header parameter
    ...
```

Have fun and happy Scraping!
