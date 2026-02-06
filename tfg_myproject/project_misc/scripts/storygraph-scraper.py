# Name: storygraph-scraper-demo.py
# Date: 06 Feb 2026
# Description: un script para recopilar información completa de un libro a partir de atributos iniciales (título y autor, ISBN)

import sys
import os
import json
from bs4 import BeautifulSoup as bs
import re
from urllib.request import Request, urlopen

def book_search(ISBN):

    url = f'https://app.thestorygraph.com/browse?search_term={ISBN}'

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
    # print(response.getheaders())

    webpage = urlopen(req).read()
    soup = bs(webpage, 'html.parser')
    # print(soup.prettify())
    # f = open(f'z.html', 'w+')
    # f.write(soup.prettify())
    # f.close()

    id = soup.find('div', class_='max-w-3xl mb-4 md:mb-6 text-darkestGrey dark:text-grey book-pane break-words').get_attribute_list('data-book-id')[0]

    return id

def book_info(id):
    # loveless_alice = 'https://app.thestorygraph.com/books/7e661a0d-089c-4eff-ba80-15cb6a54c05d'
    # convenience_sayaka = 'https://app.thestorygraph.com/books/62a675b0-1825-402c-9bd7-faa0667ccf91'
    # conversations_sally = 'https://app.thestorygraph.com/books/d4ccf1dc-2c6a-4d9a-8f49-4a9422e43977'

    url = f'https://app.thestorygraph.com/books/{id}'

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
    # print(response.getheaders())

    webpage = urlopen(req).read()
    soup = bs(webpage, 'html.parser')
    # # print(soup.prettify())

    # parsing the title with regex
    title = soup.find('h3',class_="font-semibold text-2xl md:w-11/12 inline items-center").text
    title = re.sub('  +', '', title)
    title = re.sub('\n', '', title)
    # print(title)

    # parsing authors
    authors = []
    auths = soup.find('p', class_='font-body font-medium mb-1 text-base md:text-lg md:w-11/12').find_all('a', href=True)
    for a in auths:
        authors.append(a.text)
    # print(authors)
    
    # parsing pages and first year of publication
    pages_first_pub = soup.find('p', class_='text-sm font-light text-darkestGrey dark:text-grey mt-1').find_all('span')
    # print([sp.text for sp in pages_first_pub])

    pages = pages_first_pub[0].text.split(' ')[0]
    # print(pages)

    first_pub = pages_first_pub[1].text.split(' ')[6]
    # print(first_pub)

    # parsing tags
    tags = []
    tag_div = soup.find('div',class_="book-page-tag-section relative").find_all('span')
    for tag in tag_div:
        tags.append(tag.text)
    # print(tags)

    desc = soup.find_all('script')[5].text
    pattern = re.compile(r'Description<\/h4><div class=\"trix-content mt-3\">(.*?)<\/div>') # regex expression for getting the description text out of the script
    match = pattern.search(desc)
    description = match.group(1).strip()
    description = re.sub('<(.*?)>', '', description)
    # print(description)

    img = soup.find('div', class_='book-cover').find('img').get_attribute_list('src')[0]
    # print(img)

    data = {
            'title':title,
            'authors': authors,
            'pages': pages,
            'first_pub': first_pub,
            'tags': tags,
            'description': description,
            'cover-source': img
        }
    
    dir_name = f'{title}|{authors[0]}'
    try:
        os.mkdir(f'books/{dir_name}')
    except OSError as e:
        print(e)
    
    f = open(f'./books/{dir_name}/{dir_name}.html', 'w+')
    f.write(soup.prettify())
    f.close()

    f = open(f'./books/{dir_name}/{dir_name}.json', 'w+')
    f.write(json.dumps(data, indent=4))
    f.close

if __name__ == '__main__':

    isbn = sys.argv[1]
    print(isbn)

    id = book_search(ISBN=isbn)
    print(id)

    book_info(id)
    