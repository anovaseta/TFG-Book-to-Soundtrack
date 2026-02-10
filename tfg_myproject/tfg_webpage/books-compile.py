# Name: db_final.py
# Date: Feb 10, 2026
# Description: compila todos los libros de la database (model Storygraph_Book)

import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tfg_webpage.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from webapp.models import Storygraph_Book

django.setup()

if __name__ == '__main__':

    # get books from db
    all_books = [f'{b.title} | {b.authors[0]}' for b in Storygraph_Book.objects.all()]

    file_path = os.path.join("../", "project_misc/json_files/book-db-compile.json")
    syn_file = open(file_path, "w+", encoding='utf-8')
    
    syn_file.write(json.dumps(all_books, indent=4, ensure_ascii=False))

    syn_file.close()