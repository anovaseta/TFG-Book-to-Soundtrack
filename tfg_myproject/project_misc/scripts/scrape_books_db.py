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


def signal_handler(sig, frame):
    print('\nYou pressed Ctrl+C!')
    print("\nManaged to scrape", len(book_db), "books")
    db_output.write(json.dumps(book_db, indent=4))  # dump dict in a json file
    db.close()
    db_output.close()
    rejects.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

db = open("./text_files/book_db.txt", "r")
rejects = open("./text_files/rejects.txt", "w+")
db_output = open("./json_files/db_output.json", "w")
book_db = dict()


for line in db:
    try:
        cur_line = line[:-1]  # remove newline character
        print("\n", cur_line)  # check progress
        book = Book()
        str_result = book.search(cur_line)
        print(str_result)
        result = json.loads(str_result)
        book_id = result[0]["book_id"]  # obtain book_id from the result

        book = Book()
        book_info = json.loads(book.book_info(book_id))
        book_info.pop("warnings", None)
        book_db[cur_line] = book_info  # load information of book into dict

    except Exception as e:
        print("\nError with:", cur_line)
        print(e)
        rejects.write(cur_line + "\n")  # log rejected books

print("\nManaged to scrape", len(book_db), "books")
db_output.write(json.dumps(book_db, indent=4))  # dump dict in a json file
db.close()
db_output.close()
rejects.close()
