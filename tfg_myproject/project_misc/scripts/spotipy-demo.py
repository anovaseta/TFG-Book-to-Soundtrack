import spotipy
import sys
import json
from spotipy.oauth2 import SpotifyClientCredentials

spotify_file = open("json_files/spotify_api_account.json", "r")
spotify_credentials = json.load(spotify_file)
access_token = spotify_credentials["access_token"]
client_id = spotify_credentials['client_id']
client_secret = spotify_credentials['client_secret']

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Radiohead'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])