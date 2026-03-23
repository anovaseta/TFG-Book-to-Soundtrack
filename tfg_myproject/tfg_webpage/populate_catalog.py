# Name: populate_catalog.py
# Date: Dec 23 2025
# Description: popular la database entera que será la base de este proyecto. 
# Requiere haber construido los modelos (el esquema de la database relacional) en models.py.
# Requiere tener la información ya recopilada, normalmente en formato json.
# Consiste en varias fases:
#   - Poblar los libros y sus tags the Storygraph
#   - Poblar los sinónimos a partir de los 'mood' tags
#   - Poblar artistas,álbumes,canciones a partir de todas las etiquetas en last.fm.

import os
import django
import json
import sys
from django.utils.html import strip_tags
from PyMultiDictionary import MultiDictionary

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tfg_webpage.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from webapp.models import Storygraph_Book, Storygraph_Tag, Tagged_Book, Synonym, Synonym_Relation, LastFM_Entity, Entity_Tag_Relation, Spotify_Track, Spotify_Tag_Relation

django.setup()


def populate_books_and_tags():
    # Load the scraped book database from Storygraph

    # book_db = pm.load_json("db_output_final.json")
    book_path = os.path.join("db_json", "all_books_extended.json") # load the ddbb in json format
    book_file = open(book_path, "r")
    book_db = json.load(book_file)

    tag_path = os.path.join("../project_misc", "json_files/tags_classification.json") # load json assigning a label type to each tag
    tag_file = open(tag_path, "r")
    tag_db = json.load(tag_file)

    count = 0

    failed_books = []

    for bookk in book_db.values():
        try:
            if bookk is None:
                continue

            count += 1
            title, tags = bookk['title'], bookk['tag_weights']

            print(f'Processing book {title}')
            
            # Create all the storygraph book instances in the db
            book, created = Storygraph_Book.objects.get_or_create(
                title=title,
                defaults={
                    'authors': bookk.get('authors', []),
                    'pages': bookk.get('pages', -1),
                    'first_published_year': bookk.get('first_pub', -1),
                    'description': bookk.get('description', ''),
                    'cover_source': bookk.get('cover-source', ''),
                    'storygraph_id': bookk.get('storygraph_id'),
                    'isbn_uid': bookk.get('ISBN/UID'),
                    'number_of_reviews': bookk.get('n_reviews'),
                    'tag_percentages': bookk.get('tag_percent'),
                    'pace_percentages': bookk.get('pace_percent'),
                    'tag_weights': bookk.get('tag_weights')
                }
            )

            # Process tags
            for tagg in tags:
                print(tagg[0], tagg[1])

                # first, associate each tag to its label type
                if tagg[0] in tag_db["mood"]:
                    tag_type = "MOOD"
                elif tagg in tag_db["genre"]:
                    tag_type = "GENRE"
                elif tagg in tag_db["pace"]:
                    tag_type = "PACE"
                elif tagg in tag_db["other"]:
                    tag_type = "OTHER"
                else:
                    print("Tag ", tagg[0], " does not have a type")

                # create the tag instances as we shift through the books
                tag, created = Storygraph_Tag.objects.get_or_create(
                    tag_name=tagg[0],
                    tag_type=tag_type
                )
                print(created)

                # create the relationship between books and its tags
                Tagged_Book.objects.get_or_create(
                    book=book,
                    tag=tag,
                    weight=tagg[1]
                )
        except Exception as e:
            print(e)
            failed_books.append(bookk['title'])

    print(failed_books)
    book_file.close()
    tag_file.close()


def populate_synonyms_from_tags():

    f = open("db_json/all_thesaurus_synonyms.json", "r")
    all_synonyms = json.loads(f.read())

    # save synonyms only for MOOD-type tags for now
    for tag,syn_dict in all_synonyms.items():

        print('----------------------------------------------------------------')

        print("processing", tag, "tag")

        obj_tag = Storygraph_Tag.objects.get(tag_name=tag)
        # print(obj_tag, type(obj_tag))

        # print(syn_dict)
        
        # create synonym instances, and their relationship to the tag
        for affinity,synonyms in syn_dict.items():
            for syn in synonyms:
                if syn == tag:
                    src = 'SELF' # add tag itself 'as a synonym'
                else:
                    src = 'THESAURUS'

                obj_syn, created = Synonym.objects.get_or_create(
                    synonym=syn,
                    source=src
                )

                Synonym_Relation.objects.get_or_create(
                    tag=obj_tag,
                    synonym=obj_syn,
                    affinity=affinity
                )

                print(syn,affinity,obj_tag,src)


def populate_lastfm_entities_from_synonyms():

    in_path = os.path.join("db_json/all_lastfm_entities.json")
    in_file = open(in_path, "r")
    in_dict = json.load(in_file)

    # get synonyms from db
    all_synonyms = [syn.synonym for syn in Synonym.objects.all()]

    total = len(in_dict.keys())
    counter = 1

    for kw,v in in_dict.items():

        syn = Synonym.objects.get(synonym=kw)

        print("Completing tag", kw)
        print("Tag", counter, "in", total)

        for type,t in v.items():
            print(type)
            for track in t['items']:
                # print(track)

                obj_trk, created = LastFM_Entity.objects.get_or_create(
                    name=track[0],
                    artist=track[1],
                    tag=track[2]
                )

                Entity_Tag_Relation.objects.get_or_create(
                    entity=obj_trk,
                    tag=syn,
                    source=type
                )


        counter += 1


def populate_spotify_entities_from_synonyms():

    in_path = os.path.join("db_json/all_spotify_filtered_tracks_TRACK.json")
    in_file = open(in_path, "r")
    in_dict = json.load(in_file)

    # get synonyms from db
    all_synonyms = [syn.synonym for syn in Synonym.objects.all()]

    total = len(in_dict.keys())
    counter = 1

    for kw,v in in_dict.items():

        syn = Synonym.objects.get(synonym=kw)
        print(syn)

        print("Completing tag", kw)
        print("Tag", counter, "in", total)

        for type,t in v.items():
            print(type)
            for track in t['items']:
                # print(track[0], track[1], track[2])
                # print(track)

                obj_trk, created = Spotify_Track.objects.get_or_create(
                    name=track[0],
                    artist=track[1],
                    tag=track[2],
                    spotify_json = track[3]
                )

                if created:
                    print('!!')

                Spotify_Tag_Relation.objects.get_or_create(
                    track=obj_trk,
                    tag=syn,
                    source=type
                )


        counter += 1

        
def populate():
    # populate_books_and_tags()
    # populate_synonyms_from_tags()
    # populate_lastfm_entities_from_synonyms()
    populate_spotify_entities_from_synonyms()
    # erase_db()
    sys.exit(0)


def erase_db():
    # LastFM_Entity.objects.all().delete()
    # Synonym_Relation.objects.all().delete()
    return
    

if __name__ == '__main__':
    print("Starting catalog script...")
    populate()
    print("Done!")
