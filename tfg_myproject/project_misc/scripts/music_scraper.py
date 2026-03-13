import sys
import os
import json
from bs4 import BeautifulSoup as bs
import re
import time
from urllib.request import Request, urlopen

url = 'https://music.youtube.com'
type = 'search'
query = '?q=dtmf'

# request for the webpage of a certain book
req = Request(
    url=f'{url}/{type}{query}', 
    headers={"authority": "www.google.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "referer": "www.google.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",}
    # headers={"authority": "www.google.com",
    # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",}
)


response = urlopen(req)
time.sleep(0.1)
print(response.status, response.reason)

webpage = response.read()
soup = bs(webpage, 'html.parser')

f = open(f"music/{type}_{query}.json", "w")
f.write(soup.prettify())
f.close()