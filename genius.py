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
    with open(path, newline="") as f:
        reader = csv.reader(f)
        song_list = list(reader)
    return song_list[1:]


def format_list_for_genius():
    """
    Takes a list containing song information and formats the title and artist
    so that it can be turned into a URL to request from genius.com.

    Special characters are stripped or replaced, spaces are turned into
    hyphens, everything is turned into lower case, and special add-ons like
    accents are removed.

    Returns:
        A list of titles and artists for each song, formatted to become parts
        of URLs.
    """
    original_song_list = csv_to_list("songs.csv")
    new_song_list = []

    for song in original_song_list:
        title = song[0]
        artist = song[1]

        if "&" in title:
            title = title.replace("&", "and")
        if "&" in artist:
            artist = artist.replace("&", "and")

        if "'" in title:
            title = title.replace("'", "")
        if "'" in artist:
            artist = artist.replace("'", "")

        if '"' in title:
            title = title.replace('"', '')

        if "(" in title:
            title = title.replace("(", "")
            title = title.replace(")", "")
        
        if "+" in title:
            title = title.replace("+", "")
        if "+" in artist:
            artist = artist.replace("+", "")

        if "." in title:
            title = title.replace(".", "")
        if "." in artist:
            artist = artist.replace(".", "")

        if "," in title:
            title = title.replace(",", "")
        if "," in artist:
            artist = artist.replace(",", "")

        if "/" in title:
            title = title.replace("/", " ")
        
        if "?" in title:
            title = title.replace("?", "")
        
        if "!" in title:
            title = title.replace("!", "")
        
        if ":" in title:
            title = title.replace(":", "")
        
        if "%" in title:
            title = title.replace("%", "")
        
        if "$" in title:
            title = title.replace("$", "s")
        
        # en dashes, not hyphens
        if "–" in title:
            title = title.replace("–", " ")
        if "–" in artist:
            artist = artist.replace("–", " ")

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
    url = "https://genius.com/"+ song[1] + "-" + song[0] + "-" + "lyrics"
    page = requests.get(url)
    html = BeautifulSoup(page.text, "html.parser")
    lyrics = html.find("div", class_="Lyrics__Container-sc-1ynbvzw-6 jYfhrf")

    if lyrics:
        lyrics = lyrics.get_text()
    else:
        lyrics = html.find("div", class_="lyrics")
        if lyrics:
            lyrics = lyrics.get_text()
        else:
            lyrics = html.find("div", \
                class_="Lyrics__Container-sc-1ynbvzw-2 jgQsqn")
            if lyrics:
                lyrics = lyrics.get_text()
    return lyrics


def get_all_lyrics():
    """
    Fetches lyrics for all songs in a list.

    Returns:
        A list containing the lyrics of all songs from the list.
    """
    #currently takes the last 20 songs
    songs = format_list_for_genius()[-20:]
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
    # currently takes the last 20 songs
    song_list = csv_to_list("songs.csv")[-20:]
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
    with open("songs_with_lyrics.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Artist", "Year", "Rank", "Lyrics"])
        for song in song_list:
            writer.writerow(song)