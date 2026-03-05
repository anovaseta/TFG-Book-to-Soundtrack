# Name: spotify_demo.py
# Date: 25 Feb 2026
# Description: un script para renovar credenciales para usar la API de Spotify

import json
import requests
import time

def client_credentials():
    # unscoped authorization

    spotify_file = open("json_files/spotify_api_account.json", "r+")
    spotify_credentials = json.load(spotify_file)

    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data={"grant_type": "client_credentials",
            "client_id": spotify_credentials["client_id"],
            "client_secret": spotify_credentials["client_secret"]
        }

    response = requests.post(url, data=data, headers=headers)
    print(response.status_code, response.reason)

    token = response.json()
    access_token = token["access_token"]
    token_type = token["token_type"]
    expires_in = token["expires_in"]

    print(token)

    spotify_credentials["access_token"] = access_token

    spotify_file.close()
    spotify_file = open("json_files/spotify_api_account.json", "w")
    spotify_file.write(json.dumps(spotify_credentials, indent=4))
    spotify_file.close()

    t = time.time() + expires_in # get current time and add expires_in
    tt = time.strftime("%H:%M:%S", time.localtime(t)) # convert time to a readable format
    print(f"Token expires in {tt}")
    

def authorization_code_flow():
    # scoped authorization (NOT USED)

    spotify_file = open("json_files/spotify_api_account.json", "r+")
    spotify_credentials = json.load(spotify_file)

    url = "https://accounts.spotify.com/authorize"
    redirect_uri = "http://127.0.0.1:8000"
    params = {
        "client_id": spotify_credentials["client_id"],
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": "playlist-modify-public playlist-modify-private"
    }

    auth_code = requests.get(url=url, params=params)
    print(auth_code.status_code, auth_code.reason)
    print(auth_code.text)



if __name__ == '__main__':
    client_credentials()
    # authorization_code_flow()

    

