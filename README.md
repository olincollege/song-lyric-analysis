# Song Lyric Analysis

## SUMMARY:

Our project takes the Billboard year-end top 100 singles from the past 52 years and analyzes trends in how often a song title is mentioned in its lyrics. The project involves scraping data from Wikipedia to get a list of top songs, scraping data from Genius to get their lyrics, and finally analyzing this information to make graphical representations of the trends we found in the data. The coding sections of this project are split into three files: wiki_data.py, genius.py, and finder.py.

## WIKIPEDIA SCRAPING:

wiki_data.py scrapes data from Wikipedia to find all the top 100 songs in a range of years. This file contains mutliple functions to scrape Wikipedia for the songs we want and to put that data into a CSV file. In order to achieve this, we installed and imported the csv and wikipedia packages so we could utilize functions from their libraries.

To use this file to get a list of songs from Wikipedia, the user should call the function get_all_top_songs to generate a list of top 100 songs for a range of years. Then, the user should call write_songs_to_file with that list of songs to write the information to a CSV file. For this project, we chose the year range 1970 to 2021 for the list of songs.

## GENIUS LYRICS SCRAPING:

genius.py scrapes data from Genius to find the lyrics to each of the songs from the CSV file generated by wiki_data.py, and generates a new CSV file that appens the lyrics of each song. The packages used in this file were csv, requests, the function unidecode from unidecode, and the function BeautifulSoup from bs4. BeautifulSoup is an HTML parser which allows us to get the parts of the page we want, and requests gives us access to the page. 

To use this file to get the lyrics for a list of songs, the user should call the function write_lyrics_to_file to generate a new CSV file with the lyrics attached to each song. WARNING: This may take a long time depending on the number of songs (It takes 2+ hours for 5200 songs).

## ANALYSIS ON THE SONGS:

finder.py uses the CSV file with lyrics generated by genius.py to count how many times the song title is in its lyrics, and creates a list with relevant data about all of the songs. To use this file to get a list of song data, the user should call the function get_total_song_data to get a list of lists containing the title, artist, year, rank, and frequency of title mentioned in lyrics for each song. This list of lists can be organized so that each song's data is a list item in the larger list, or so that each category of data is a list item in the larger list.

## DATA:

The data we have is stored in two main CSV files. The first is songs.csv and this stores all the data we scraped from Wikipedia. This stores the songs title, artist, year, and ranking. The seconds is songs_with_lyrics.csv and this stores all the same data as well as the lyrics of the song. We have also included copies of those files to allow us to have a back-up in case we change the data in any way accidentally. 

## COMPUTATIONAL ESSAY AND VISUALS

The visuals that represent the trends we found in the data are all in the computational essay lyric_analysis.ipynb. The essay uses two additional packages: matplotlib.pyplot and the function profanity from better_profanity. The matplotlib allowed us to visualize our code and the better_profanity package helped keep the song titles clean when we displayed them.

### List of all packages used in this project:

#### wiki_data.py

- csv
- wikipedia

#### genius.py

- csv
- unidecode (from unidecode)
- BeautifulSoup (from bs4)
- requests

#### lyric_analysis.ipynb

- matplotlib.pyplot
- profanity (from better_profanity)
