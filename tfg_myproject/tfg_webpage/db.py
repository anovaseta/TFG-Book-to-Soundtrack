# Name: download_db.py
# Date: Jan 11 2026
# Description: una libreria para obtener objetos de la bbdd

import os
import sys
import django
import json
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tfg_webpage.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from webapp.models import Synonym, Storygraph_Book, Spotify_Track, Spotify_Tag_Relation

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

def get_json_spotify_entities():
    f = open('db_json/all_spotify_filtered_tracks_FROM_ARTISTS.json', 'r')
    all_entities = json.loads(f.read())
    f.close()
    return all_entities

def get_spotify_tracks():
    all_tracks = Spotify_Track.objects.all()
    relations = Spotify_Tag_Relation.objects.all()

    return (all_tracks, relations)

def json_enmesh_files():
    all_entities = get_json_spotify_entities()
    f = open(os.path.join("../", "project_misc/json_files/spotify_filtered_tracks.json"), 'r')
    temp_entities = json.loads(f.read())
    f.close()
    for tag,t in temp_entities.items():
        print(f'Processing tag {tag}')
        all_entities[tag]['FROM_ARTISTS'] = temp_entities[tag]['FROM_ARTISTS']

    # return all_entities
    # f = open('db_json/all_spotify_filtered_tracks.json', 'w')
    # all_entities = json.loads(f.read())
    # f.close()



        

if __name__ == '__main__':


    # all_entities = json_enmesh_files()
    all_entities = get_json_spotify_entities()
    # f = open(os.path.join("../", "project_misc/json_files/spotify_filtered_tracks.json"), 'r')
    # all_entities = json.loads(f.read())

    f = open("db_json/all_updated_tags.json", "r")
    all_tags = json.loads(f.read())
    print(len(all_tags))
    print(len(all_entities.keys()))

    for i in range(0,11):
        if list(all_entities.keys())[i] != all_tags[i]:
            print(i)

    total = 0
    # populated_syn = []
    for tag,t in all_entities.items():
        # print('---------------------------------------------------------------')
        # print(tag)
        for src,v in t.items():
            
            total += v['n']
            # if v['n'] > 0 and src == 'TRACK':
            #     populated_syn.append(tag)
            # print(src,v['n'])
            # for track in v['items']:
            #     spotify_track = track[3]
            #     # print(spotify_track)
            #     print(spotify_track['name'], spotify_track['artists'][0]['name'], spotify_track['external_urls']['spotify'])
    print(total, len(all_entities.keys()))

    # all_synonyms = Synonym.objects.all()
    # all_tracks = Spotify_Track.objects.all()

    # populated_syn = []

    # for syn in all_synonyms:
    #     query = all_tracks.filter(tag=syn.synonym)
    #     # print(query)
    #     if len(query) != 0:
    #         populated_syn.append(syn.synonym)

    # print(len(populated_syn))

    sys.exit(0)