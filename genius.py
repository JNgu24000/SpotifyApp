import requests
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

access_token=os.getenv('TOKEN')

def getSongLyrics(songname,artist):
    BASE_URL='https://api.genius.com/search'
    headers={'Authorization': 'Bearer ' + access_token}
    data={'q': songname + ' ' + artist}

    response=requests.get(BASE_URL,data=data,headers=headers)
    response_json=response.json()
    lyrics=response_json['response']['hits'][0]['result']['url']

    return lyrics

