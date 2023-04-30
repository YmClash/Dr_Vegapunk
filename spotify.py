import os

import spotipy
from dotenv import load_dotenv
from spotipy import SpotifyClientCredentials
load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET)

spoti = spotipy.Spotify(client_credentials_manager=auth_manager)



uri = '5PXa57bB4y0vrQqeZX7A2S'



result = spoti.artist_albums(uri, album_type='album')
albums = result['items']


while result['next']:
    result = spoti.next(result)
    albums.extend(result['items'])

for album in albums:
    print(album['name'])


