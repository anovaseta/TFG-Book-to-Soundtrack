# Name: scrape_books_db.py
# Date: Sep 16, 2025
# Description: un script que utiliza la API de la app de libros StoryGraph para
# conseguir las etiquetas de 'mood' de un número determinado de libros.
# Input: book_db.txt con una lista de títulos de libros a buscar
# Output: db_output.json con la información de los libros scrapeados.

from storygraph_api import Book
import json
import signal
import sys
from storygraph_scraper import book_search, book_info
import urllib


def signal_handler(sig, frame):
    print('\nYou pressed Ctrl+C!')
    print("\nManaged to scrape", len(book_db), "books")
    db_output.write(json.dumps(book_db, indent=4, ensure_ascii=False))  # dump dict in a json file
    db.close()
    db_output.close()
    compiled_list.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

db = open("./json_files/book_db.json", "r")
new_books = json.loads(db.read())

compiled_list = open("./json_files/book-db-compile.json", "r")
old_books = json.loads(compiled_list.read())

db_output = open("./json_files/db_output.json", "w")
book_db = dict()
n_line = 0


for s_book in new_books:
    try:
        n_line +=1  # remove newline character
        print(f'\nLine {n_line}: {s_book}')  # check progress
        if s_book in old_books:
            print("ALREADY IN DB")
            continue

        url_string = urllib.parse.quote_plus(s_book)
        # print(url_string)

        book_id = book_search(url_string)
        print(book_id)

        book_data = book_info(book_id)
        # print(book_data)

        book_db[s_book] = book_data

        # this is is using storygraph_api, deprecated for now

        # book = Book()
        # str_result = book.search(cur_line)
        # print(str_result)
        # result = json.loads(str_result)
        # book_id = result[0]["book_id"]  # obtain book_id from the result

        # book = Book()
        # book_info = json.loads(book.book_info(book_id))
        # book_info.pop("warnings", None)
        # book_db[cur_line] = book_info  # load information of book into dict

    except Exception as e:
        print("\nError with:", s_book)
        print(e)

print("\nManaged to scrape", len(book_db), "books")
db_output.write(json.dumps(book_db, indent=4, ensure_ascii=False))  # dump dict in a json file
db.close()
db_output.close()
compiled_list.close()
