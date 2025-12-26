# Name: populate_catalog.py
# Date: Dec 23 2025
# Description: popular la database entera que será la base de este proyecto. 
# Requiere haber construido los modelos (el esquema de la database relacional) en models.py.
# Consiste en varias fases:
#   - Poblar los libros y sus tags the Storygraph
#   - Poblar los sinónimos a partir de los 'mood' tags
#   - Poblar artistas,álbumes,canciones a partir de todas las etiquetas en last.fm.

import os
import django
import json
from django.utils.html import strip_tags
from PyMultiDictionary import MultiDictionary

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tfg_webpage.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from webapp.models import Storygraph_Book, Storygraph_Tag, Tagged_Book, Synonym, Synonym_Relation

django.setup()


def populate_books_and_tags():
    # Load the scraped book database from Storygraph

    # book_db = pm.load_json("db_output_final.json")
    book_path = os.path.join("../project_misc", "db_output_final.json") # load the ddbb in json format
    book_file = open(book_path, "r")
    book_db = json.load(book_file)

    tag_path = os.path.join("../project_misc", "tags_classification.json") # load json assigning a label type to each tag
    tag_file = open(tag_path, "r")
    tag_db = json.load(tag_file)

    for bookk in book_db.values():
        
        # Create all the storygraph book instances in the db
        description = strip_tags(bookk.get('description', ''))
        book, created = Storygraph_Book.objects.get_or_create(
            title=bookk.get('title', 'Unknown Title'),
            defaults={
                'authors': bookk.get('authors', []),
                'pages': bookk.get('pages', 0),
                'first_published_year': bookk.get('first_pub', 0),
                'average_rating': bookk.get('average_rating', 0.0),
                'description': description
            }
        )

        # Process tags
        tags = bookk.get('tags', [])
        for tagg in tags:

            # first, associate each tag to its label type
            if tagg in tag_db["mood"]:
                tag_type = "MOOD"
            elif tagg in tag_db["genre"]:
                tag_type = "GENRE"
            elif tagg in tag_db["pace"]:
                tag_type = "PACE"
            elif tagg in tag_db["other"]:
                tag_type = "OTHER"
            else:
                print("Tag ", tagg, " does not have a type")

            # create the tag instances as we shift through the books
            tag, created = Storygraph_Tag.objects.get_or_create(
                tag_name=tagg,
                tag_type=tag_type
            )

            # create the relationship between books and its tags
            Tagged_Book.objects.get_or_create(
                book=book,
                tag=tag
            )

    book_file.close()
    tag_file.close()


def populate_synonyms_from_tags():
    
    # gets all the names of MOOD tags from the current database
    all_tags = Storygraph_Tag.objects.all().filter(tag_type='MOOD')

    # initalize PyMultiDictionary
    dict = MultiDictionary()

    # save synonyms only for MOOD-type tags for now
    for obj_tag in all_tags:

        tag = obj_tag.tag_name
        syn_list = dict.synonym('en', tag)
        syn_list = syn_list + [tag] # add tag itself 'as a synonym'

        # print(tag, syn_list)
        # print('----------------------------------------------------------------')

        # create synonym instances, and their relationship to the tag
        for syn in syn_list:
            if syn == tag:
                type = 'SELF' # add tag itself 'as a synonym'
            else:
                type = 'PYMULTIDICTIONARY'

            # print(syn, type)

            obj_syn, created = Synonym.objects.get_or_create(
                synonym=syn,
                source=type
            )

            Synonym_Relation.objects.get_or_create(
                tag=obj_tag,
                synonym=obj_syn
            )




    

def populate():
    # populate_books_and_tags()
    populate_synonyms_from_tags()
    

if __name__ == '__main__':
    print("Starting catalog population script...")
    populate()
    print("Done!")
