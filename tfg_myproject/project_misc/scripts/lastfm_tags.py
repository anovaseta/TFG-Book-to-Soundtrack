# Name: lastfm_tags.py
# Date: ?? Sept/Oct 2025
# Description: un script muy inicial para probar la funcionalidad de las
# tags de lastfm. Usado en feb 2026 para investigar los métodos de pylast

import pylast
import json
import os

# In order to perform a write operation you need to authenticate yourself

# out_path = os.path.join("../", "sample_tag_search.json")
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

# sample_tag_search = open(out_path, "w", encoding="utf-8")

# tags = ["emotional", "reflective", "adventurous", "dark", "mysterious", "sad",
#         "funny", "lighthearted", "challenging", "tense", "inspiring",
#         "hopeful", "relaxing"]

tags = ["emotional"]

sample_dict = dict()

limit = 1

for tag in tags:
    cur_tag = network.get_tag(tag).name
    sample_dict[cur_tag] = dict()

    cur_tag_artists = network.get_tag(tag).get_top_artists(limit=limit)
    cur_tag_albums = network.get_tag(tag).get_top_albums(limit=limit)
    cur_tag_tracks = network.get_tag(tag).get_top_tracks(limit=limit)

    tt = network.get_tag(tag)
    
    methods_list = [method for method in dir(tt) if not method.startswith("__")]

    print(tt.get_name())
    print(methods_list)
    # print(tt.get_wiki_content()._get_params())
    print("----------------------------------------------------------")

    # print("Methods using dir(): ", methods_list)

    # artist_list = []
    # albums_list = []
    # tracks_list = []

    for artist in cur_tag_artists:
        print(artist.item)
        print([method for method in dir(artist.item) if not method.startswith("__")])
        print("top tags:", [t.item.get_name() for t in artist.item.get_top_tags()])
        print("top tracks:", [tr.item.get_name() for tr in artist.item.get_top_tracks(limit=10)])
        print("top albums:", [tr.item.get_name() for tr in artist.item.get_top_albums(limit=10)])
        print("similar artists:", [a.item.get_name() for a in artist.item.get_similar(limit=10)])
        print("----------------------------------------------------------")
        # artist_name = artist.item.get_name()
    #     artist_list.append(artist_name)

    # sample_dict[cur_tag]["top_artists"] = artist_list

    for album in cur_tag_albums:
        print(album.item)
        print(album.item.get_title(), "|", album.item.get_artist())
        print([method for method in dir(album.item) if not method.startswith("__")])
        print("top tags:", [t.item.get_name() for t in album.item.get_top_tags()])
        print("tracks:", [tr.get_name() for tr in album.item.get_tracks()])
        print("----------------------------------------------------------")
        # album_name = album.item.get_name()
    #     albums_list.append(album_name)

    # sample_dict[cur_tag]["top_albums"] = albums_list

    for track in cur_tag_tracks:
        print(track.item)
        print(track.item.get_title(), "|", track.item.get_artist(), "|", track.item.get_album().get_title())
        print([method for method in dir(track.item) if not method.startswith("__")])
        print("top tags:", [t.item.get_name() for t in track.item.get_top_tags()])
        print("similar tracks:", [tr.item.get_name() for tr in track.item.get_similar(limit=10)])
        # track_name = track.item.get_name()
    #     tracks_list.append(track_name)

    # sample_dict[cur_tag]["top_tracks"] = tracks_list

# sample_tag_search.write(json.dumps(sample_dict, indent=4, ensure_ascii=False))
# sample_tag_search.close()
