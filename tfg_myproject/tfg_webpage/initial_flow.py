# Name: initial_flow.py
# Date: Feb 02 2026
# Description: retratar un flujo inicial y rudimentario desde meter un libro (ISBN) hasta obtener una lista de canciones.

import os
import sys
import django
import json
import pylast
import random, secrets

sys.path.append('/home/manuloseta/TFG/tfg_myproject')
from project_misc.scripts.storygraph_scraper import book_info, book_search
from project_misc.scripts.dictionary_scraper import thesaurus

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tfg_webpage.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from webapp.models import Storygraph_Book, Storygraph_Tag, Tagged_Book, Synonym, Synonym_Relation, LastFM_Entity, Entity_Tag_Relation

django.setup()  

def inputt():
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


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Need to provide one argument with the script (an ISBN number of a book).")
        sys.exit(0)
    
    # Step 1: retrieve book info from ISBN from StoryGraph

    print('Step 1: retrieve book info from ISBN from StoryGraph')

    isbn = sys.argv[1]
    print(isbn)

    book_id = book_search(isbn)
    book_data = book_info(book_id)

    print([b for b in book_data.items() if b[0] != 'description'])

    inputt()

    # Step 2: compile and classify the initial list of tags

    print('Step 2: compile and classify the initial list of tags')

    tags = book_data['tags']
    # print(tags)
    dict_t = {'MOOD': [], 'GENRE': [], 'PACE': [], 'OTHER': []}

    db_tags = Storygraph_Tag.objects.all()
    # print(db_tags)
    for dbt in db_tags:
        for t in tags:
            if t == dbt.tag_name:
                dict_t[dbt.tag_type] += [t]

    print(dict_t)

    inputt()


    # Step 3: extend MOOD tags into a synonym/related words list

    print('Step 3: extend MOOD tags into a synonym/related words list')

    keywords = []

    for mood in dict_t['MOOD']:
        try:
            print(mood)
            syn_list = thesaurus(mood)
        except Exception as e:
            print(e)

        keywords += [s for s in syn_list[0]] + [mood]
    
    print(keywords)

    inputt()

    # Step 4: use synonym/related words to extract a playlist of songs from lastfm

    account_path = os.path.join("../", "project_misc/json_files/lastfm_api_account.json")

    account_file = open(account_path, "r")
    account_info = json.load(account_file)

    password_hash = pylast.md5(account_info["password"])

    network = pylast.LastFMNetwork(
        api_key=account_info["api_key"],
        api_secret=account_info["api_secret"],
        username=account_info["username"],
        password_hash=password_hash,
    )


    for kw in [keywords[9]]:
        print(kw)

        tracks = [(tr.item.get_name(), tr.item.get_artist().get_name()) for tr in network.get_tag(kw).get_top_tracks(limit=15)]
        print(tracks)

        albums = network.get_tag(kw).get_top_albums(limit=15)
        print(f'{len(albums)} albums recovered')
        a_tracks = []
        for album in albums:
            print(album.item.get_name())
            var = []
            random.seed(secrets.randbits(12))
            n = random.randint(0,2)
            print(f'{n} tracks to gather')
            if n == 0:
                continue
            try:
                var = random.sample(album.item.get_tracks(), n)
            except Exception as e:
                print(e)
            a_tracks += [(tr.get_name(), tr.get_artist().get_name()) for tr in var]
        print(a_tracks)

        artists = network.get_tag(kw).get_top_artists(limit=15)
        print(f'{len(artists)} artists recovered')
        ar_tracks = []
        for ar in artists:
            print(ar.item.get_name())
            var = []
            random.seed(secrets.randbits(12))
            n = random.randint(0,2)
            print(f'{n} tracks to gather')
            if n == 0:
                continue
            try:
                var = random.sample(ar.item.get_top_tracks(limit=30), n)
            except Exception as e:
                print(e)
            ar_tracks += [(tr.item.get_name(), tr.item.get_artist().get_name()) for tr in var]
        print(ar_tracks)

    final_list = tracks + a_tracks + ar_tracks
    random.shuffle(final_list)
    print(final_list)

    inputt()

    # Step 5: Connect to Spotify API to create the playlist

    

    









