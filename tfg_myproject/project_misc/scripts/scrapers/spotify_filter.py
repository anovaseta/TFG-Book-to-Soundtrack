# Name: spotify_filter.py
# Date: 13 Mar 2026
# Description: un script para conseguir el objeto musical de spotify, a partir de la información de LastFM.

import os
import re
import json
import requests
import time

def spotify_get_access_token():
    spotify_file = open("json_files/spotify_api_account.json", "r")
    spotify_credentials = json.load(spotify_file)
    access_token = spotify_credentials["access_token"]
    return access_token

def spotify_bulk_search(track_dict, tag_list, access_token):
    #if tag_list is None then the argument is ignored
    
    api = "https://api.spotify.com/v1"
    search_url = f'{api}/search'
    headers = {"Authorization": "Bearer {}".format(access_token),
               "Content-Type": "application/json"}

    found_tracks = {}
    slp_strd = 0
    slp = slp_strd

    for keyword,types in track_dict.items():
        if tag_list is not None:
            if keyword not in tag_list:
                continue
        
        # n_tracks = 0
        # counter = 0
        # for type,tracks in types.items():
        #     n_tracks += len(tracks['items'])
        # print(f'About to process a total of {n_tracks} tracks, estimate time of completion is {n_tracks*slp_strd}')

        found_tracks[keyword] = {'TRACK': {'n': 0, 'items': []}, 'FROM_ARTISTS': {'n': 0, 'items': []}, 'FROM_ALBUMS': {'n': 0, 'items': []}}
        print('--------------------------------------------------------------------')
        print(keyword)

        for type,tracks in types.items():
            if type != 'FROM_ARTISTS':
                continue

            print(type)
            n_tracks = len(tracks['items'])
            print(f'About to process a total of {n_tracks} tracks, estimate time of completion is {n_tracks*slp_strd}')

            counter = 0
            for track,artist,kw in tracks['items']:
                # print(keyword,type,n,track,artist,kw)
                # para ver si hace una buena search
                counter += 1
                print(f'Track {counter} of {n_tracks}')
                response = spotify_search(search_url, track, artist, kw, headers, slp)
                if response['match_found']:
                    track_item = response['track_item']
                    found_tracks[keyword][type]['n'] += 1
                    found_tracks[keyword][type]['items'].append([track,artist,kw,track_item])
                    print(track_item)
                else:
                    print('Not found')
                
                if response['rate_limit']:
                    slp = response['timeout']
                    if slp > 3600:
                        f = open("json_files/spotify_filtered_tracks.json", 'w', encoding='utf-8')
                        f.write(json.dumps(found_tracks, indent=4, ensure_ascii=False))
                        f.close()
                        print(slp)
                        t = time.time() + slp # get current time and add slp
                        tt = time.strftime("%H:%M:%S", time.localtime(t)) # convert time to a readable format
                        print(f"API resets at {tt}")
                        return
                else:
                    slp = slp_strd

    f = open("json_files/spotify_filtered_tracks.json", 'w', encoding='utf-8')
    f.write(json.dumps(found_tracks, indent=4, ensure_ascii=False))
    f.close()


def spotify_search(search_url, track, artist, kw, headers, time_to_sleep):

    match_found = False
    rate_limit = False

    print("--------------------")
    print(f"({track}, {artist}, {kw})")
    parsed_track = re.sub(' ', '%20', track)
    parsed_artist = re.sub(' ', '%20', artist)
    search_query = f'{search_url}?q={parsed_track}%20{parsed_artist}%20track%3A{parsed_track}%20artist%3A{parsed_artist}&type=track&market=US&limit=10'
    print(search_query)
    try:
        print(time_to_sleep)
        time.sleep(time_to_sleep)
        response = requests.get(search_query, headers=headers)
        print(response.status_code, response.reason)
        if response.status_code == 429:
            rate_limit = True
            print(response.headers)
            timeout = int(response.headers['Retry-After'])
            return {'match_found': match_found,
                    'rate_limit': rate_limit,
                    'timeout': timeout}

        items = response.json()

        for item in items['tracks']['items']:
            track_name = item['name']
            artists = []
            for a in item['artists']:
                artists.append(a['name'])
            # url_spotify = item['external_urls']['spotify']
            if track == track_name:
                if artist in artists:
                    match_found = True
                    spotify_item = item
                    break
    except Exception as e:
        print('An exception ocurred')
        print(e)
        print(response.raw)
    
    if match_found:
        return {'match_found': match_found,
                'rate_limit': rate_limit,
                'track_item': spotify_item}
    else:
        return {'match_found': match_found,
                'rate_limit': rate_limit}


if __name__ == '__main__':

    f = open(os.path.join('../', 'tfg_webpage/db_json/all_lastfm_entities_refined.json'), 'r')
    all_tracks = json.loads(f.read())
    f.close()

    f = open(os.path.join('../', 'tfg_webpage/db_json/all_updated_tags.json'), 'r')
    all_tags = json.loads(f.read())
    f.close()

    index = 94

    print(all_tags[index:])

    # spotify_bulk_search(all_tracks, all_tags[index:], spotify_get_access_token())
    # print('DO NOT FORGET TO SAVE THE PROGRESS')