# Name: dictionary_scraper.py
# Date: 10 Feb 2026
# Description: un script para hacer scraping para conseguir sinónimos/palabras relacionadas

import sys
import os
import re
import json
from bs4 import BeautifulSoup as bs
import re
from urllib.request import Request, urlopen

def thesaurus(word, include='strongest'):

    assert include in ['weak', 'strong', 'strongest'], '\'include\' parameter must have one of these values: [\'weak\', \'strong\', \'strongest\']'


    word = re.sub(" ", "%20", word) # useful parsing for urls
    url = f'https://www.thesaurus.com/browse/{word}?noredirect=true'

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
    # print(response.status, response.reason)

    soup = bs(response.read(), 'html.parser')

    s_list = []

    synonyms = soup.find('section', class_="synonym-antonym-panel")

    # always include strongest synonyms
    strongest = synonyms.find_all('a', class_="word-chip synonym-antonym-word-chip similarity-100")
    for a in strongest:
        parsed_text = re.sub(r"  +", "", a.text)
        parsed_text = re.sub("\n", "", parsed_text)
        s_list.append(parsed_text)

    if include == 'strong':
        strong = synonyms.find_all('a', class_="word-chip synonym-antonym-word-chip similarity-50")
        for a in strong:
            parsed_text = re.sub(r"  +", "", a.text)
            parsed_text = re.sub("\n", "", parsed_text)
            s_list.append(parsed_text)

    if include == 'weak':
        strong = synonyms.find_all('a', class_="word-chip synonym-antonym-word-chip similarity-50")
        for a in strong:
            parsed_text = re.sub(r"  +", "", a.text)
            parsed_text = re.sub("\n", "", parsed_text)
            s_list.append(parsed_text)

        weak = synonyms.find_all('a', class_="word-chip synonym-antonym-word-chip similarity-10")
        for a in weak:
            parsed_text = re.sub(r"  +", "", a.text)
            parsed_text = re.sub("\n", "", parsed_text)
            s_list.append(parsed_text)

    # file = open("x.html", "w+")
    # file.write(soup.prettify())

    return [s_list, len(s_list)]

if __name__ == '__main__':
    word = sys.argv[1]
    print(thesaurus(word))