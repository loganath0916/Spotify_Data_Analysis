#SPOTIFY DATA PIPELINE PROJECT 

This project demonstrates how to build an end-to-end ETL pipeline using the Spotify API, Python, and MySQL.
The pipeline extracts track metadata from Spotify, transforms it into structured data, and loads it into a MySQL database for analysis and visualization.

------

##FEATURES:
-Extract track details (Track name, Artist, Album, Popularity, Duration) using Spotify API.
-Store processed data in MySQL database.
-Perform ETL (Extract, Transform, Load) operations with Python.
-Generate simple data visualizations (e.g., popularity, track length). 

-----

##TECH STACK:
-Python (Spotipy, Pandas, Matplotlib, MySQL Connector, Regex)
-Spotify Web API
-MySQL (Database for storage and queries)

-----

##HOW IT WORKS:
Extract → Read track URLs from a file (track_urls.txt) and fetch metadata using Spotify API.
Transform → Process and clean metadata (e.g., converting track duration from ms → minutes).
Load → Insert the transformed data into MySQL (spotify_track table).
Analyze → Use Pandas and Matplotlib to explore and visualize insights.

-----

##SCREENSHOT
![Mysql_db](db.png)
![1. Top 5 Most Popular Tracks](usecase1.png) 
![2. Longest Songs (by duration) & 3. Average Popularity Across All Tracks](usecase2&3.png)


