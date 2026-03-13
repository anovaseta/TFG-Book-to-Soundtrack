# Name: download_db.py
# Date: Jan 11 2026
# Description: una libreria para obtener objetos de la bbdd

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
    all_synonyms = [(syn.synonym, syn.source) for syn in Synonym.objects.all()]

    file_path = os.path.join("../", "project_misc/json_files/synonym_list.json")
    syn_file = open(file_path, "w")
    
    syn_file.write(json.dumps(all_synonyms, indent=4, ensure_ascii=False))

    syn_file.close()

    print(len(all_synonyms))


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


def get_json_books():
    f = open('db_json/all_books_extended.json', 'r')
    all_books = json.loads(f.read())
    return all_books


def get_json_thesaurus_synonyms():
    f = open('db_json/all_thesaurus_synonyms.json', 'r')
    all_syn = json.loads(f.read())
    return all_syn


def get_json_lastfm_entities():
    f = open('db_json/all_lastfm_entities.json', 'r')
    all_entities = json.loads(f.read())
    return all_entities

        

if __name__ == '__main__':
    # get_synonyms()
    # get_storygraph_books()

    # all_books = get_json_books()
    # print(list(all_books.values())[0])

    # get_synonyms()
    all_entities = get_json_lastfm_entities()

    g = open(os.path.join("../", "project_misc/json_files/synonym_list.json"), "r")
    all_tags = json.loads(g.read())
    all_tags = [t[0] for t in all_tags]

    all_synonyms = [x.synonym for x in Synonym.objects.all()]

    counter = 0
    for tt in all_entities.values():
        for tracks in tt.values():
            counter += len(tracks['items'])

    all_keys = list(all_entities.keys())
    print(counter, len(all_keys), len(all_tags), len(all_synonyms))

    # left_tags = []
    # for i in range(189,412):
    #     print(all_keys[i], all_tags[i])

    # counter = 0
    # for x in all_tags:
    #     counter += 1
    #     print(counter, x, x in all_keys)

    print([x for x in all_keys if x not in all_tags])
    print([x for x in all_keys if x not in all_synonyms])



