# Name: lastfm_scraper.py
# Date: Jan 11 2026
# Description: un script que recoge los top artists, albums y tracks para cada tag de la bbdd

import sys
import json
import pylast
import django


def get_lastfm_credentials():

    # manage LastFM credentials and connect to network
    account_file = open("json_files/lastfm_api_account.json", "r")
    account_info = json.load(account_file)
    password_hash = pylast.md5(account_info["password"])
    network = pylast.LastFMNetwork(
        api_key=account_info["api_key"],
        api_secret=account_info["api_secret"],
        username=account_info["username"],
        password_hash=password_hash,
    )
    return network


def get_lastfm_music(tag_list, network, n):

    final_dict = {}

    a_count = 0
    a_total = len(tag_list)
    print(f"Processing {a_total} tags")

    for kw in tag_list:
        # use lastfm api to get tracks, albums and artists from each keyword 'kw'
        # questionable findings, no matches with spotify later
        final_dict[kw] = {'TRACK': {'n': 0, 'items': []}, 'FROM_ARTISTS': {'n': 0, 'items': []}, 'FROM_ALBUMS': {'n': 0, 'items': []}}
        a_count += 1
        print(f"{kw} (tag {a_count} of {a_total})")
        try:
            tracks = [(tr.item.get_name(), tr.item.get_artist().get_name(), kw) for tr in network.get_tag(kw).get_top_tracks(limit=10*n)]
            print(f"Got {len(tracks)} tracks")
            final_dict[kw]['TRACK']['n'] += len(tracks)
            final_dict[kw]['TRACK']['items'] += tracks
            # print(tracks)
        except Exception as e:
            print(e)
            print(f"Something went wrong with tracks of {kw}")

        try:
            albums = network.get_tag(kw).get_top_albums(limit=n)
            a_tracks = []
            print(f"Got {len(albums)} albums")
            counter = 0
            for album in albums:
                counter += 1
                if counter < len(albums):
                    print(f"\rGathering album {counter}", end = "")
                else:
                    print(f"\rGathering album {counter}")
                a_tracks += [(tr.get_name(), tr.get_artist().get_name(), kw) for tr in album.item.get_tracks()]
                # print(a_tracks)
            # print(a_tracks)
            final_dict[kw]['FROM_ALBUMS']['n'] += len(a_tracks)
            final_dict[kw]['FROM_ALBUMS']['items'] += a_tracks
        except Exception as e:
            print(e)
            print(f"Something went wrong with albums of {kw}")

        try:
            artists = network.get_tag(kw).get_top_artists(limit=n)
            ar_tracks = []
            print(f"Got {len(artists)} artists")
            counter = 0
            for artist in artists:
                counter += 1
                ar_tracks += [(tr.item.get_name(), tr.item.get_artist().get_name(), kw) for tr in artist.item.get_top_tracks(limit=10)]
                if counter < len(artists):
                    print(f"\rGathering artist {counter}", end = "")
                else:
                    print(f"\rGathering artist {counter}")
                # print(ar_tracks)
            # print(ar_tracks)
            final_dict[kw]['FROM_ARTISTS']['n'] += len(ar_tracks)
            final_dict[kw]['FROM_ARTISTS']['items'] += ar_tracks
        except Exception as e:
            print(e)
            print(f"Something went wrong with artists of {kw}")

    # print(final_dict)

    return final_dict


if __name__ == "__main__":

    f = open("json_files/synonym_list.json", "r")
    tag_list = json.loads(f.read())
    clean_tag_list = [t[0] for t in tag_list]
    print(clean_tag_list)
    # print(len(clean_tag_list))

    music_dict = get_lastfm_music(clean_tag_list, get_lastfm_credentials(), 5)
    print(music_dict)

    f = open("json_files/lastfm_entities.json", "w", encoding='utf-8')
    f.write(json.dumps(music_dict, indent=4, ensure_ascii=False))
    f.close()

    sys.exit(0)

    