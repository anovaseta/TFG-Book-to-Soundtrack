# Name: script1.py
# Date: Aug 25, 2025
# Description: primera toma de contacto probando la API de StoryGraph

from storygraph_api import Book
id = "28386517-30cc-4ce4-bb90-9336c370a9dd"
book = Book()
try:
    result = book.book_info(id)
    print(result)
except Exception as e:
    print(e)
result = book.search("The Orphan Master's Son, Adam Johnson")
print(result)
