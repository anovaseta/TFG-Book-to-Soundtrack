# Name: dictionary_scraper.py
# Date: 10 Feb 2026
# Description: un script para hacer scraping para conseguir sinónimos/palabras relacionadas

import sys
import os
import json
from bs4 import BeautifulSoup as bs
import re
from urllib.request import Request, urlopen

def thesaurus(word):

    url = f'https://www.thesaurus.com/browse/{word}'

    # request for the webpage of a certain book
    req = Request(
        url=url, 
        headers={"authority": "www.google.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "referer": "www.google.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",}
        # headers={"authority": "www.google.com",
        # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",}
    )

    response = urlopen(req)
    print(response.status, response.reason)

    soup = bs(response.read(), 'html.parser')

    file = open("x.html", "w+")
    file.write(soup.prettify())

if __name__ == '__main__':
    word = sys.argv[1]
    thesaurus(word)