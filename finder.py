"""
finder.py uses the songs_with_lyrics.csv file to count how many
times the song title is in it's lyrics. This file splits the
task up into multiple functions. The first function counts
the number of times the song title is in the lyrics for one
song. The second function calls the first function and runs
through all 5200 through that function. Then the second
function creates a list containing [Title,Artist,Year,Rank,count]
for each song, where count is the number of times the song title
is in the lyrics.
"""
from genius import csv_to_list


def title_in_lyrics_one_song(song):
    """
    Takes a list of information on a song and counts how many times
    the songs title is in the lyrics.

    Args:
        song: a list containing [Title, Artist, Year, Rank, Lyrics].

    Returns:
        The number of times the song title is in the lyrics.

    """
    title = song[0]
    lyrics = song[4]
    if '(' in title:
        title = title[0:title.find("(") - 1]
    if len(lyrics) == 0:
        return -1
    return lyrics.lower().count(title.lower())


def get_total_song_data(path, by_song=False):
    """
    Given a CSV file containing song information and lyrics, returns a list
    containing [Title, Artist, Year, Rank, Frequency of Title in Lyrics].

    Args:
        path: The relative path to the CSV file.
        by_song: A boolean that represents whether the returned list will be
            by song or by category. If by_song is false it returns by category,
            and if it is true it returns by song.

    Returns:
        A list that contains lists of a song title, artist, year, ranking,
        and the number of times the title is mentioned in its lyrics.
    """
    total_song_data = []
    song_list = csv_to_list(path)
    if by_song:
        for song in song_list:
            total_song_data.append([song[0], song[1], song[2], song[3],
                                    title_in_lyrics_one_song(song)])
    else:
        titles = []
        artists = []
        years = []
        ranks = []
        frequencies = []
        for song in song_list:
            titles.append(song[0])
            artists.append(song[1])
            years.append(song[2])
            ranks.append(song[3])
            frequencies.append(title_in_lyrics_one_song(song))
        total_song_data = [titles, artists, years, ranks, frequencies]

    return total_song_data
