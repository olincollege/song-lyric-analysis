import csv
from genius import csv_to_list


def title_in_lyrics_one_song(song):
    """
    Args: song is a list
    return:
    """
    title = song[0]
    lyrics = song[4]
    if '(' in title:
        title = title[0:title.find("(") - 1]
    return lyrics.lower().count(title.lower())


def title_in_lyrics_all_songs(path):
    """
    """
    song_list = csv_to_list(path)
    for song in song_list:
        song.append(title_in_lyrics_one_song(song))
    return song_list
