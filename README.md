# Summary
The purpose of this project is to utilize the Spotify Search API and Genius API to fetch various pieces of data regarding a song such as the name, artist, album image, preview URL, and lyrics. This information is passed through a Flask framework onto an HTML page, which is stylized by a CSS file. This app is available through a remote repository on Github and also on Heroku.

# Technology
## APIs
* Spotify API: The Artists API of the Spotify Developers Tools was utilized to fetch information about an artist's top ten tracks, specifically the name of it, album artwork associated with it, and a preview URL if available.
* Genius API: The Search API of Genius was utilized to find the lyrics of an associated song based on the name and artist given.

## Libraries
* Flask: Python-based framework that provides the main load for converting the information available from the APIs into data to be displayed on the HTML page.
* JSON: Converts the HTTP response of APIs in Python for easy readability
* Random: Utilize a single function that randomizes selection in a certain list
* Requests: sends HTTP requests to a web server in order to retrive information

# Installation
This project featuers many facets to work efficiently (hopefully) and requires certain things for setup:
## .env
This project uses an .env file that contains the client key and secret client key required for authorization to use the Spotify API. This file is not pushed to github for the sake of protecting those keys, so a new one must be created when forking (.gitignore ensures that the file is not pushed to github) in addition to using new keys.

1. Go to https://developer.spotify.com/dashboard/ and create a new account
2. Create a new application to generate a Client ID and Secret ID. These are the keys utilized for the program
3. Create a new file called ".env".
4. Write "export" and the identifier for your token equal to the key from the Spotify application. For example, in the .env file there will be "export CLIENT_ID = 'ClIENT_ID_NUMBER'" where CLIENT_ID_NUMBER is the key from Spotify.

## Library Installation
You will have to run some commands in the terminal in order to install the proper library into Python:
* `pip install python-dotenv`: this will install the necesary functions to pull data from the .env file you've created
* `pip install requests`: this will install the functions required to create a request in Python
* `pip install flask`: this will establish the framework needed to create an app in Python

# Technical Issues
The first problem I had when starting this project was how to juggle two separate authentication processes for two separate APIs, as well as the data retrived from both. I ultimately decided on creating two separate .py files to run each API separately, and reference their data in app.py in order to have a central location for the project to use the information.

Another major problem I grappled with was how to have the data from the Spotify API be available for use for app.py, since I had to return multiple fields at once. To alleviate this, I put the elements into a list and had app.py pull from each element on the list (since each index refers to a certain piece of information).

One of the major flaws of the project actually comes from utilizing the Genius Search API; no matter how many fields I closely enter into the function to return the lyrics, it will always return the incorrect URL, and this will persist even when utilizing parameters from the Spotify API. As of this writing I possess no idea how to make the result more accurate considering I always input the name of the song and the artist every time and only become successful less than half the time.

If there was one way I would do to improve this project in general was probably take more time, since due to physical health reason I was unable to work on this project for as long as I would've been comfortable with, but am hopeful to apply this improvement on more projects.