# Name: storygraph-scraper.py
# Date: 03 Feb 2026
# Description: un script para intentar hacer web scraping de storygraph (la API usada hasta ahora parece no responder)

import requests
from bs4 import BeautifulSoup


def scrape():
    
    # url = 'https://www.example.com'
    url = 'https://app.thestorygraph.com/robots.txt'
    print(url)

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)
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