# Name: initial_flow.py
# Date: Feb 02 2026
# Description: retratar un flujo inicial y rudimentario desde meter un libro (ISBN) hasta obtener una lista de canciones.

import os
import sys
import django
import json
import pylast
from django.utils.html import strip_tags
from PyMultiDictionary import MultiDictionary
from storygraph_api import Book

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tfg_webpage.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from webapp.models import Storygraph_Book, Storygraph_Tag, Tagged_Book, Synonym, Synonym_Relation, LastFM_Entity, Entity_Tag_Relation

django.setup()  

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Need to provide one argument with the script (an ISBN number of a book).")
        sys.exit(0)
    
    # Step 1: retrieve book info from ISBN from StoryGraph

    book = Book()
    isbn = sys.argv[1]
    print(isbn)
    print(book.book_info(isbn))
