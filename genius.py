"""
genius.py scrapes data from genius.com to find the lyrics to each of the songs
in the top 100 every year. The data is put into a CSV file labeled
songs_with_lyrics.csv.
"""
import csv
from unidecode import unidecode
from bs4 import BeautifulSoup
import requests


def csv_to_list(path):
    """
    Takes a CSV file containing song information and converts it to a list.

    Args:
        path: The file path of the CSV file (string).

    Returns:
        A list of lists containing song information.
    """
    with open(path, newline="") as my_file:
        reader = csv.reader(my_file)
        song_list = list(reader)
    return song_list[1:]


def format_list_for_genius(original_song_list):
    """
    Takes a list containing song information and formats the title and artist
    so that it can be turned into a URL to request from genius.com.

    Special characters are stripped or replaced, spaces are turned into
    hyphens, everything is turned into lower case, and special add-ons like
    accents are removed.

    Args:
        original_song_list: A list containing titles and artists of songs to
            format.

    Returns:
        A list of titles and artists for each song, formatted to become parts
        of URLs.
    """
    new_song_list = []

    for song in original_song_list:
        title = song[0]
        artist = song[1]

        char_replacements = {"&": "and", "...": " ", "'": "", '"': '',
                             "(": "", ")": "", ".": "", ",": "", "/": " ", "?": "", "!": "",
                             ":": "", "%": "", "$": "s", "–": " "}

        for character, replacement in char_replacements.items():
            if character in title:
                title = title.replace(character, replacement)
            if character in artist:
                artist = artist.replace(character, replacement)

        if "+" in title:
            title = title.replace("+", "")
        if "+" in artist:
            artist = artist.replace("+", " ")

        while "  " in title:
            title = title.replace("  ", " ")
        while "  " in artist:
            artist = artist.replace("  ", " ")

        title = title.replace(" ", "-")
        artist = artist.replace(" ", "-")
        title = title.lower()
        artist = artist.lower()

        new_song_list.append([unidecode(title), unidecode(artist)])

    return new_song_list


def get_lyrics(song):
    """
    Given a song, access the lyrics for that song from genius.com, fetch the
    HTML, and parse the HTML to get just the lyrics.

    Args:
        song: A list containing the title and artist of the song in a form
            that can be pasted in as part of a URL.

    Returns:
        A string that is the lyrics of the song.
    """
    url = "https://genius.com/" + song[1] + "-" + song[0] + "-" + "lyrics"
    page = requests.get(url)
    if str(page) == "<Response [404]>":
        alt_artist = song[1][0:song[1].find("-")]
        page = requests.get("https://genius.com/" + alt_artist + "-" +
                            song[0] + "-" + "lyrics")
    html = BeautifulSoup(page.text, "html.parser")
    lyrics = html.find_all("div",
                           class_="Lyrics__Container-sc-1ynbvzw-6 jYfhrf")
    if not lyrics:
        lyrics = html.find_all("div", class_="lyrics")
    if not lyrics:
        lyrics = html.find("div",
                           class_="Lyrics__Container-sc-1ynbvzw-2 jgQsqn")

    final_lyrics = ""
    if lyrics:
        for item in lyrics:
            final_lyrics += " ".join(item.strings)

    return final_lyrics


def get_all_lyrics():
    """
    Fetches lyrics for all songs in a list.

    Returns:
        A list containing the lyrics of all songs from the list.
    """
    song_list = csv_to_list("songs.csv")
    songs = format_list_for_genius(song_list)
    lyrics = []
    for song in songs:
        lyrics.append(get_lyrics(song))
    return lyrics


def song_list_with_lyrics():
    """
    Appends lyrics to songs contained in a list.

    Returns:
        A list of lists containing song information and lyrics.
    """
    song_list = csv_to_list("songs.csv")
    lyric_list = get_all_lyrics()
    for index, song in enumerate(song_list):
        song.append(lyric_list[index])
    return song_list


def write_lyrics_to_file():
    """
    Takes a list containing song information and lyrics and writes it to a
    CSV file.
    """
    song_list = song_list_with_lyrics()
    with open("songs_with_lyrics.csv", "w") as my_file:
        writer = csv.writer(my_file)
        writer.writerow(["Title", "Artist", "Year", "Rank", "Lyrics"])
        for song in song_list:
            writer.writerow(song)
