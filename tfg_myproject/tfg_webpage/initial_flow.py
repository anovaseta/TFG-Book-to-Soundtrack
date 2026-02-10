# Name: initial_flow.py
# Date: Feb 02 2026
# Description: retratar un flujo inicial y rudimentario desde meter un libro (ISBN) hasta obtener una lista de canciones.

import os
import sys
import django
import json
import pylast
from PyMultiDictionary import MultiDictionary, DICT_SYNONYMCOM, DICT_THESAURUS

sys.path.append('/home/manuloseta/TFG/tfg_myproject')
from project_misc.scripts.storygraph_scraper import book_info, book_search
from project_misc.scripts.dictionary_scraper import thesaurus

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

    isbn = sys.argv[1]
    print(isbn)

    book_id = book_search(isbn)
    book_data = book_info(book_id)

    print([b for b in book_data.items() if b[0] != 'description'])

    proceed = False
    while(proceed == False):
        ans = input(f'\nProceed? [y/n]\n')
        if ans == 'y' or ans == 'Y':
            proceed = True
        elif ans == 'n' or ans == 'N':
            print('System exit')
            sys.exit(0)
        else:
            print('invalid answer')


    # Step 2: compile an initial list of keywords associated to the book

    tags = book_data['tags']
    print(tags)

    dict = MultiDictionary(*tags)
    dict.set_words_lang('en')

    keywords = []

    for tag in tags:
        syn_list = dict.get_synonyms(DICT_SYNONYMCOM)
        keywords += [s for s in syn_list] + [tag]
    
    print(keywords)

    proceed = False
    while(proceed == False):
        ans = input(f'\nProceed? [y/n]\n')
        if ans == 'y' or ans == 'Y':
            proceed = True
        elif ans == 'n' or ans == 'N':
            print('System exit')
            sys.exit(0)
        else:
            print('invalid answer')







