# Name: lastfm_tags.py
# Date: ?? Sept/Oct 2025
# Description: un script muy inicial para probar la funcionalidad de las
# tags de lastfm
# Input: lastfm_api_account.json con las credenciales de la API de lastfm
# Output: sample_tag_search.json con los top artists, albums y tracks de cada 
# tag en la lista predefinida

import pylast
import json
import os

# In order to perform a write operation you need to authenticate yourself
out_path = os.path.join("../", "sample_tag_search.json")
account_path = os.path.join("../", "lastfm_api_account.json")

account_file = open(account_path, "r")
account_info = json.load(account_file)

password_hash = pylast.md5(account_info["password"])

network = pylast.LastFMNetwork(
    api_key=account_info["api_key"],
    api_secret=account_info["api_secret"],
    username=account_info["username"],
    password_hash=password_hash,
)

sample_tag_search = open(out_path, "w", encoding="utf-8")

tags = ["emotional", "reflective", "adventurous", "dark", "mysterious", "sad",
        "funny", "lighthearted", "challenging", "tense", "inspiring",
        "hopeful", "relaxing"]

sample_dict = dict()

limit = 30

for tag in tags:
    cur_tag = network.get_tag(tag).name
    sample_dict[cur_tag] = dict()

    cur_tag_artists = network.get_tag(tag).get_top_artists(limit=limit)
    cur_tag_albums = network.get_tag(tag).get_top_albums(limit=limit)
    cur_tag_tracks = network.get_tag(tag).get_top_tracks(limit=limit)

    # tt = network.get_tag(tag)
    
    # methods_list = [method for method in dir(tt) if callable(getattr(tt, method)) and not method.startswith("__")]

    # print("Methods using dir(): ", methods_list)

    artist_list = []
    albums_list = []
    tracks_list = []

    for artist in cur_tag_artists:
        artist_name = artist.item.get_name()
        artist_list.append(artist_name)

    sample_dict[cur_tag]["top_artists"] = artist_list

    for album in cur_tag_albums:
        album_name = album.item.get_name()
        albums_list.append(album_name)

    sample_dict[cur_tag]["top_albums"] = albums_list

    for track in cur_tag_tracks:
        track_name = track.item.get_name()
        tracks_list.append(track_name)

    sample_dict[cur_tag]["top_tracks"] = tracks_list

sample_tag_search.write(json.dumps(sample_dict, indent=4, ensure_ascii=False))
sample_tag_search.close()
