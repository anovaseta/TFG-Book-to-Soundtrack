# Name: storygraph-scraper-demo.py
# Date: 03 Feb 2026
# Description: un script para intentar hacer web scraping de storygraph (la API usada hasta ahora parece no responder)

import sys
import os
import json
from bs4 import BeautifulSoup as bs
import re



def scrape():

    import requests
    
    # url = 'https://www.example.com'
    # url = "https://httpbin.io/headers"
    url = "https://app.thestorygraph.com/books/7e661a0d-089c-4eff-ba80-15cb6a54c05d"
    print(url)

    headers = {
        "authority": "www.google.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "referer": "www.google.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        # add more headers as needed
    }

    response = requests.get(url)

    # response.raise_for_status()

    # if response.status_code == 200:
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     print(soup.prettify())
    # else:
    #     print("failed")
    print(response.status_code, response.reason)
    soup = bs(response.text, 'html.parser')
    print(soup.prettify())
    # f = open('./html_files/x.html', 'w+')
    # f.write(soup.prettify())

def scrape2():

    # Source - https://stackoverflow.com/a/31758803
    # Posted by zeta
    # Retrieved 2026-02-06, License - CC BY-SA 3.0

    # Source - https://stackoverflow.com/a/16627277
    # Posted by Stefano Sanfilippo, modified by community. See post 'Timeline' for change history
    # Retrieved 2026-02-06, License - CC BY-SA 4.0

    from urllib.request import Request, urlopen

    loveless_alice = 'https://app.thestorygraph.com/books/7e661a0d-089c-4eff-ba80-15cb6a54c05d'
    convenience_sayaka = 'https://app.thestorygraph.com/books/62a675b0-1825-402c-9bd7-faa0667ccf91'

    # request for the webpage of a certain book
    req = Request(
        url=loveless_alice, 
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
    # print(response.getheaders())

    webpage = urlopen(req).read()
    soup = bs(webpage, 'html.parser')
    # # print(soup.prettify())

    # parsing the title with regex
    title = soup.find('h3',class_="font-semibold text-2xl md:w-11/12 inline items-center").text
    title = re.sub('  +', '', title)
    title = re.sub('\n', '', title)
    print(title)

    # parsing authors
    authors = []
    auths = soup.find('p', class_='font-body font-medium mb-1 text-base md:text-lg md:w-11/12').find_all('a', href=True)
    for a in auths:
        authors.append(a.text)
    print(authors)
    
    # parsing pages and first year of publication
    pages_first_pub = soup.find('p', class_='text-sm font-light text-darkestGrey dark:text-grey mt-1').find_all('span')
    print([sp.text for sp in pages_first_pub])

    pages = pages_first_pub[0].text.split(' ')[0]
    print(pages)

    first_pub = pages_first_pub[1].text.split(' ')[6]
    print(first_pub)

    # parsing tags
    tags = []
    tag_div = soup.find('div',class_="book-page-tag-section relative").find_all('span')
    for tag in tag_div:
        tags.append(tag.text)
    print(tags)

    desc = soup.find_all('script')[5].text
    print(desc)
    pattern = re.compile(r'<div>\\n<em>(.*?)<\/div>') # regex expression for getting the description text out of the script
    match = pattern.search(desc)
    print(match.group(1))
    # pattern = re.compile(r"Description<\/h4><div class=\"trix-content mt-3\">(.*?)<\/div>", re.DOTALL)
    # match = pattern.search(desc)
    # description = match.group(1).strip()

    # data = {
    #         'title':title,
    #         'authors': authors,
    #         'pages': pages,
    #         'first_pub': first_pub,
    #         'tags': tags,
    #         'description':description,
    #     }
    
    # dir_name = f'{title}, {authors}'
    # os.mkdir(dir_name)
    
    # f = open(f'./books/{dir_name}/{dir_name}.html', 'w+')
    # f.write(soup.prettify())
    # f.close()

    # f = open(f'./books/{dir_name}/{dir_name}.json', 'w+')
    # f.write(json.dump(data))
    # f.close


if __name__ == '__main__':
    arg = sys.argv[1]
    # print(arg)
    if arg == '1':
        scrape()
    elif arg == '2':
        scrape2()
    else:
        print("?")