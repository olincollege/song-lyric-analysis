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


def get_total_song_data(path):
    """
    Given a CSV file containing song information and lyrics, returns a list
    containing [Title, Artist, Year, Rank, Frequency of Title in Lyrics].

    Args:
        path: The relative path to the CSV file.

    Returns: 
        A list that contains lists of a song title, artist, year, ranking,
        and the number of times the title is mentioned in its lyrics.
    """
    total_song_data = []
    song_list = csv_to_list(path)
    for song in song_list:
        total_song_data.append([song[0], song[1], song[2], song[3], \
            title_in_lyrics_one_song(song)])
    return total_song_data
