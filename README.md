In particular, your submission repository should have a file called README.md written in Markdown. This file should briefly summarize your project and explain how to use your code to obtain and/or analyze your data. By following the instructions in the README, anyone else should be able to clone your project code to their machine and perform a similar analysis to your work.

# SUMMARY:

Our project takes the top 100 songs on the billboards each year from the past 52 years. The songs range from different languages, genres, and artists. We then find the lyrics for each of the songs and count how many times the title appears in the lyrics. We then use visuals to see if there are any correlations between the rankings of the songs and how many times the title appears in the lyrics. We split the coding sections of this project into three files: wiki_data.py, genius.py, and finder.py.

# WIKIPEDIA SCRAPING:

wiki_data.py scrapes data from wikipedia to find all the top 100 songs each year. This file contains mutliple functions to scrape wikipedia for the songs we want and to put that data into a CSV file. In order to achieve this we needed to include the packages import csv and import wikipedia. The first function called create_song_list takes in an input of a year and finds the song and artist of the top 100 songs. In this file, we specifically searched for the wikipedia pages "Billboard Year-End Hot 100 singles of" + (the year we want). We then took the list of top 100 songs on the page with all the data to each song (Title,Artist,Year,Rank,) and put the data into a CSV file labeled songs.csv. We also created a file labeled songs_copy.csv which is a copy of of the songs.csv as a backup just in case songs.csv changed in any way. 

# GENIUS LYRICS SCRAPING:

genius.py scrapes data from genius to find the lyrics to each of the songs in the top 100 every year. In order to do this we needed to include the packages: import csv, from unidecode import unidecode, from bs4 import BeautifulSoup, import requests. unidecode formats special characters. BeautifulSoup is an HTML parser which allows us to get the parts of the page we want. Requests gives us access to the page. We search for the lyrics by using the unique genius URL for each song. We then pick the lyrics from the page and put that data into a CSV file labeled songs_with_lyrics.csv. We also created a file labeled songs_with_lyrics_copy.csv which is a copy of of the songs_with_lyrics.csv as a backup just in case songs_with_lyrics.csv changed in any way. 

# ANALYSIS ON THE SONGS:

finder.py uses the songs_with_lyrics.csv file to count how many times the song title is in its lyrics. This file splits the task up into multiple functions. The first function counts the number of times the song title is in the lyrics for one song. The second function calls the first function and runs through all 5200 through that function. Then the second function creates a list containing [Title,Artist,Year,Rank,count] for each song, where count is the number of times the song title is in the lyrics. 

# DATA:

The data we have is stored in 2 main CSV files. The first is songs.csv and this stores all the data we scraped from Wikipedia. This stores the songs title, artist, year, and ranking. The seconds is songs_with_lyrics.csv and this stores all the same data as well as the lyrics of the song. We have also included copies of those files to allow us to have a back-up in case we change the data in any way accidentally. 

# VISUALS:

The visuals are all in the computational essay and need a few packages to run them. The packages include from better_profanity we imported profanity and we imported matplotlib.pyplot as plt. Also from our file finder.py we imported get_total_song_data into the visuals. The matplotlib allowed us to visualize our code and the profanity package help keep the song titles clean. The list get_total_song_data has all the data we needed to visualize our code.


# COMPUTATIONAL ESSAY:

The file essay.ipynb contains our computational essay, which describes how we used our code and what we wanted to get out of it. This also describes the results we came up with from analyzing the data we scrape. 

# All packages

#wiki_data.py#

import csv
import wikipedia

#genius.py#

import csv
from unidecode import unidecode
from bs4 import BeautifulSoup
import requests

#finder.py#

from genius import csv_to_list

#essay.ipynb#

import matplotlib.pyplot as plt
from finder import get_total_song_data
from better_profanity import profanity
