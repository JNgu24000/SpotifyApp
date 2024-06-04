import requests
import os
from dotenv import find_dotenv, load_dotenv
import base64
import json
import random

load_dotenv(find_dotenv())

CLIENT_ID=os.getenv('CLIENT_ID')
CLIENTSECRET_ID=os.getenv('CLIENTSECRET_ID')

AUTH_URL = 'https://accounts.spotify.com/api/token'

def getArtistInfo(id):
    auth_response=requests.post(AUTH_URL,{
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENTSECRET_ID,
})

    auth_response_data=auth_response.json()
    access_token=auth_response_data['access_token']

    headers={'Authorization': 'Bearer {token}'.format(token=access_token)}
    params={'q':id,'market':'US'}

    BASE_URL='https://api.spotify.com/v1/artists/'

    response=requests.get(BASE_URL + id + '/top-tracks',headers=headers,params=params)
    response_json = response.json()
    random_index=random.randint(0,4)
    release=response_json['tracks'][random_index]

    def getName(release):
        return release['name']
    def getArtistName(release):
        return release['artists'][0]['name']
    def getAlbumImage(release):
        return release['album']['images'][0]['url']
    def getPreviewURL(release):
        return release['preview_url']

    name=getName(release)
    artistName=getArtistName(release)
    albumImage=getAlbumImage(release)
    previewURL=getPreviewURL(release)

    list=[name,artistName,albumImage,previewURL]
    return list

