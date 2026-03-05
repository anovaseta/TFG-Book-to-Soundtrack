# Name: download_db.py
# Date: Jan 11 2026
# Description: un script para obtener objetos de la bbdd
# Output: synonym_list.json con la lista

import os
import django
import json
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tfg_webpage.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from webapp.models import Synonym, Storygraph_Book

django.setup()

def get_synonyms():
    # get synonyms from db
    all_synonyms = [syn.synonym for syn in Synonym.objects.all()]

    # LastFM authentication credentials
    file_path = os.path.join("../", "project_misc/json_files/synonym_list.json")
    syn_file = open(file_path, "w")
    
    syn_file.write(json.dumps(all_synonyms, indent=4, ensure_ascii=False))

    syn_file.close()


def get_storygraph_books():
    # returns a list of tuples with title and author (deprecated db version)
    all_books = [(b.title, b.authors[0]) for b in Storygraph_Book.objects.all()]
    print(len(all_books))

    # LastFM authentication credentials
    d = date.today().strftime("%d-%m-%y")
    file_path = os.path.join("../", f"project_misc/json_files/all_db_books_{d}.json")
    syn_file = open(file_path, "w")
    
    syn_file.write(json.dumps(all_books, indent=4, ensure_ascii=False))

    syn_file.close()



if __name__ == '__main__':
    # get_synonyms()
    get_storygraph_books()