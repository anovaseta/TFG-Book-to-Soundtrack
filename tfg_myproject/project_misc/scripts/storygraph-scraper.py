# Name: storygraph-scraper.py
# Date: 03 Feb 2026
# Description: un script para intentar hacer web scraping de storygraph (la API usada hasta ahora parece no responder)

import requests
from bs4 import BeautifulSoup


def scrape():
    
    # url = 'https://www.example.com'
    url = "https://httpbin.io/headers"
    print(url)

    headers = {
        "authority": "www.google.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        # add more headers as needed
    }

    response = requests.get(url, headers=headers)

    response.raise_for_status()

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())
    else:
        print("failed")

    # soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)



if __name__ == '__main__':
    scrape()






# import requests
# from bs4 import BeautifulSoup

# # URL of the webpage to scrape
# books_page_url = "https://books.toscrape.com/"

# # Fetch the webpage content
# response = requests.get(books_page_url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content of the page
#     soup_parser = BeautifulSoup(response.text, 'html.parser')

#     # Find all articles that contain book information
#     book_articles = soup_parser.find_all('article', class_='product_pod')

#     # Loop through each book article and extract its title and price
#     for book_article in book_articles:
#         # Extract the title of the book
#         book_name = book_article.h3.a['title']

#         # Extract the price of the book
#         book_cost = book_article.find('p', class_='price_color').text

#         # Print the title and price of the book
#         print(f"Title: {book_name}, Price: {book_cost}")
# else:
#     # Print an error message if the page could not be retrieved
#     print("Failed to retrieve the webpage")