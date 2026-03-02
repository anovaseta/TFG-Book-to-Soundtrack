# Name: lastfm_complete_scraping.py
# Date: Jan 11 2026
# Description: un script que recoge los top artists, albums y tracks para cada tag de la bbdd
# Input: synonym_list.json con la lista de tags
# Output: complete_tag_search.json con los top artists, albums y tracks de cada 
# tag en la lista predefinida

import pylast
import json
import os

in_path = os.path.join("json_files", "synonym_list.json")
out_path = os.path.join("json_files", "complete_tag_search.json")
account_path = os.path.join("json_files", "lastfm_api_account.json")

in_file = open(in_path, "r")
out_file = open(out_path, "w", encoding="utf-8")
account_file = open(account_path, "r")

# manage LastFM credentials and connect to network
account_info = json.load(account_file)
password_hash = pylast.md5(account_info["password"])
network = pylast.LastFMNetwork(
    api_key=account_info["api_key"],
    api_secret=account_info["api_secret"],
    username=account_info["username"],
    password_hash=password_hash,
)

# load 450 tags from file
tags = json.load(in_file)
total = len(tags)
count = 1

sample_dict = dict()

limit = 30

failed_tags = []

for tag in tags:
    try:
        cur_tag = network.get_tag(tag).name
        sample_dict[cur_tag] = dict()

        print("Obtaining tag:", cur_tag, "(", count, "/" , total,")")

        cur_tag_artists = network.get_tag(cur_tag).get_top_artists(limit=limit)
        cur_tag_albums = network.get_tag(cur_tag).get_top_albums(limit=limit)
        cur_tag_tracks = network.get_tag(cur_tag).get_top_tracks(limit=limit)

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

        print("Tag", cur_tag, "done")
        count += 1

    except Exception as e:
        failed_tags += [cur_tag]
        print(e)
        print("Continue to next tag")
        continue

print(failed_tags)
out_file.write(json.dumps(sample_dict, indent=4, ensure_ascii=False))
out_file.close()
