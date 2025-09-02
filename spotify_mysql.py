from spotipy.oauth2 import SpotifyClientCredentials
import  spotipy 
import pandas as pd 
import  matplotlib.pyplot as plt 
import mysql.connector
import re

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='b80535da9b6c4f2795b0c947274cde57',
    client_secret='56cf97888ab6494e9146554725790343'
))

db_config = {
    'host' : 'localhost',
    'user' : 'root',
    'password' :  'root',
    'database' : 'spotify_db'
} 
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

file_path = "track_urls.txt"
with open(file_path, 'r')as file:
    track_urls = file.readlines()

for  track_url in track_urls:
    track_url = track_url.strip()
    try:
       track_id = re.search(r"track/([a-zA-Z0-9]+)",track_url).group(1)

       track = sp.track(track_id)

       track_data = {
           'Track Name' : track['name'],
           'Artist' : track['artists'][0]['name'],
           'Album' : track['album']['name'],
           'Popularity' : track['popularity'],
           'Duration (minutes)' : track['duration_ms'] / 60000
    } 
 
       insert_query = """
       INSERT INTO spotify_track(track_name, artist, album, popularity, duration_minutes)
       VALUES (%s, %s, %s, %s, %s)
       """
       cursor.execute(insert_query,(
            track_data['Track Name'],
            track_data['Artist'],
            track_data['Album'],
            track_data['Popularity'],
            track_data['Duration (minutes)']
        ))

       connection.commit()

       print(f"Track '{track_data['Track Name']}' by {track_data['Artist']} inserted into the database.")

    except Exception as e:
       print(f"Error processing URL: {track_url},Error:{e}")

cursor.close()
connection.close()

print("ALL TRACKS HAVE BEEN PROCESSED AND INSERT INTO THE DATBASE")