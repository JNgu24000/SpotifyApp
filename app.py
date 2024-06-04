from artist import getArtistInfo
from genius import getSongLyrics
import flask
import random

import os

app = flask.Flask(__name__)

artistID=['53XhwfbYqKCa1cC15pYq2q','4UXqAaa6dQYAk18Lv7PEgX','3FUY2gzHeIiaesXtOAdB7A','4gzpq5DPGxSnKTe4SA8HAU','0du5cEVh5yTK9QJze8zA0C','7EQ0qTo7fWT7DPxmxtSYEc'] # input list of Spotify artists IDs


@app.route("/")
def main():
    id=random.choice(artistID) # selects a random artist ID from the list
    artist_data=getArtistInfo(id) # retrieves data from artist.py file
    songLyric=getSongLyrics(artist_data[0],artist_data[1]) # utilizes data from artist.py in genius.py
    return flask.render_template("index.html",songName=artist_data[0],artistName=artist_data[1],albumImage=artist_data[2],previewURL=artist_data[3],songLyric=songLyric)

app.run(
    debug=True,
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
)