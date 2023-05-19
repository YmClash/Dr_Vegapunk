import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
# SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

scope = 'user-modify-playback-state'
auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)

spoti = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                  client_secret=SPOTIPY_CLIENT_SECRET,
                                                  scope=scope))


#
# spoti = spotipy.Spotify(client_credentials_manager=auth_manager)
#

def add_song_to_queue(song_uri: str) :
    try :
        spoti.add_to_queue(song_uri)
        return "Add Track to queue Successfully!!"
    except :
        return "Error adding track to queue"


def find_song_by_name(name: str) :
    results = spoti.search(q=name, type='track')
    if results :
        song_uri = results['tracks']['items'][0]['uri']
        return song_uri


def find_song_by_lyrics(lyrics: str) :
    results = spoti.search(q=f"lyrics:{lyrics}", type='track')
    if results :
        if len(results['track']['items']) > 0 :
            song_uri = results['tracks']['items'][0]['uri']
            return song_uri
        else :
            return ("no matching Tracks Found")


def add_song_to_queue_by_song_name(song_name: str) :
    song_uri = find_song_by_lyrics(song_name)
    if (song_uri) :
        add_song_to_queue(song_uri)
        return "Successfully added song to queue"
    else :
        return "No matching tracks found"


def add_song_to_quue_by_lyrics(lyrics: str) :
    song_uri = find_song_by_lyrics(lyrics)
    if (song_uri) :
        return add_song_to_queue_by_song_name(song_uri)
    else :
        return "No matching tracks found"


def start_playing_song_by_name(song_name: str) :
    song_uri = find_song_by_name(song_name)
    if (song_uri) :
        spoti.start_playback(uris=[song_uri])
        return f"Starteed Playing song {song_name}"
    else :
        return "No matching tracks found"


def start_music() :
    try :
        spoti.start_playback()
        return "Plaxing started!"
    except :
        return "error stating playback"

#
#
#
#
# birdy_uri = '5MbNzCW3qokGyoo9giHA3V'
#
#
# results = spoti.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spoti.next(results)
#     albums.extend(results['items'])
#
# for album in albums:
#     print(album['name'])
#
#
# #
# # uri = '4d26k6BPR9MhZyTj3g5yEM'
# #
# #
# #
# # result = spoti.artist_albums(uri, album_type='album')
# # albums = result['items']
# #
# # print(result)
# # #
# # # while result['next']:
# # #     result = spoti.next(result)
# # #     albums.extend(result['items'])
# # #
# # # for album in albums:
# # #     print(album['name'])
# # #
# #
