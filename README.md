In particular, your submission repository should have a file called README.md written in Markdown. This file should briefly summarize your project and explain how to use your code to obtain and/or analyze your data. By following the instructions in the README, anyone else should be able to clone your project code to their machine and perform a similar analysis to your work.

#SUMMARY:

Our project takes the top 100 songs on the billboards each year from the past 52 years. The songs range from different languages, genres, and artists. We then find the lyrics for each of the songs and count how many times the title appears in the lyrics. We then use visuals to see if there are any correlations between the rankings of the songs and how many times the title appears in the lyrics. We split the coding sections of this project into three files: wiki_data.py, genius.py, and finder.py.

#WIKIPEDIA SCRAPING:

wiki_data.py scraps data from wikipedia to find all the top 100 songs each year. This file contains mutliple functions to scrap wikipedia for the songs we want and to put that data into a csv file. The first function called create_song_list takes in an input of a year and finds the song and artist of the top 100 songs. The data is put into a csv file labeled songs.csv. We also created a file labeled songs_copy.csv which is a copy of of the songs.csv as a backup just in case songs.csv changed in any way. 

#GENIUS LYRICS SCRAPING:

genius.py scraps data from genius to find the lyrics to each of the songs in the top 100 every year. The data is put into a csv file labeled songs_with_lyrics.csv. We also created a file labeled songs_with_lyrics_copy.csv which is a copy of of the songs_with_lyrics.csv as a backup just in case songs_with_lyrics.csv changed in any way.

#ANALYSIS ON THE SONGS:

finder.py uses the songs_with_lyrics.csv file to count how many times the song title is in it's lyrics. This file splits the task up into multiple functions. The first function counts the number of times the song title is in the lyrics for one song. The second function calls the first function and runs through all 5200 through that function. Then the second function creates a list containing [Title,Artist,Year,Rank,count] for each song, where count is the number of times the song title is in the lyrics. 

#DATA:


#VISUALS:

(Visuals section)

#COMPUTATIONAL ESSAY:

(computatational essay section)