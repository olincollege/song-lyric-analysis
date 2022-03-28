"""
Test functions that clean and organize data.
"""

import pytest

from genius import (
    csv_to_list,
    format_list_for_genius,

)

from finder import (
    title_in_lyrics_one_song,
    get_total_song_data,
)



format_list_cases = [
    # Checking that spaces get turned into dashes "-"
    ([[' ', ' ']], [['-', '-']]),

    # Checking "&" is replaced by "and".
    ([['&', '&']], [['and', 'and']]),

    # Checking "..." is replaced by " ".
    ([['...', '...']], [['-', '-']]),

    # Checking "'" is replaced by "".
    ([["'", "'"]], [["", ""]]),

    # Checking '"' is replaced by ''.
    ([['"', '"']], [['', '']]),

    # Checking "(" is replaced by "".
    ([["(", "("]], [["", ""]]),

    # Checking ")" is replaced by "".
    ([[")", ")"]], [["", ""]]),

    # Checking "." is replaced by "".
    ([['.', '.']], [['', '']]),

    # Checking "," is replaced by "".
    ([[',', ',']], [['', '']]),

    # Checking "/" is replaced by " ".
    ([['/', '/']], [['-', '-']]),

    # Checking "?" is replaced by "".
    ([['?', '?']], [['', '']]),

    # Checking "!" is replaced by "".
    ([['!', '!']], [['', '']]),

    # Checking ":" is replaced by "".
    ([[':', ':']], [['', '']]),

    # Checking "%" is replaced by "".
    ([['%', '%']], [['', '']]),

    # Checking "$" is replaced by "s".
    ([['$', '$']], [['s', 's']]),

    # Checking "–" is replaced by " ".
    ([['–', '–']], [['-', '-']]),

    # Checking "+" is replaced by "" in title and " " in artist.
    ([['+', '+']], [["", "-"]]),

    # Checking "  " is replaced by " ".
    ([["  ", "  "]], [["-", "-"]]),

    # Checking that multiple cases of characters are properly replaced.
    ([["(& ! & $)", "(& ! & $)"]], [["and-and-s", "and-and-s"]]),

    # Checking that two symbols that translate into a dash will only create one
    # dash if they are positioned next to one another.
    ([[".../", ".../"]], [["-", "-"]])
]

# Testing genius.py

def test_csv_to_list():
    """
    Check that a csv_to_list takes a CSV file containing song information and
    converts it to a list.
    """
    assert csv_to_list("test_csv_to_list.csv") == [['Title One', ' Artist One', \
        ' Year One', ' Rank One'], ['Title Two', ' Artist Two', ' Year Two', \
        ' Rank Two'], ['Title Three', ' Artist Three', ' Year Three', \
        ' Rank Three']]



@pytest.mark.parametrize("original_song_list,new_song_list", format_list_cases)
def test_format_list_for_genius(original_song_list, new_song_list):
    """
    Checks that format_list_for_genious properly takes a list containing
    song information and formats the title and artist so that it can be turned
    into a URL to request from genius.com.

    Args:
        original_song_list: A list containing titles and artists of songs to
            format.
        new_song_list: A list containing titles and artists that have been
            formatted so they can fit into a URL.
    """
    assert format_list_for_genius(original_song_list) == new_song_list



# Testing finder.py

def test_title_in_lyrics_one_song():
    """
    Takes a list of information on a song and counts how many times
    the songs title is in the lyrics.
    """
    song = ['Hi','Bob','1999','12','Hi how are you hi hello hi']
    assert title_in_lyrics_one_song(song) == 3


def test_get_total_song_data1():
    """
    Test that given a CSV file containing song information and lyrics, returns a list
    containing [Title, Artist, Year, Rank, Frequency of Title in Lyrics].

    This test checks that the by_song parameter is True.
    """
    assert get_total_song_data("test_get_total_song_data.csv",by_song=True) ==\
    [['Title One', ' Artist One', ' Year One', ' Rank One', 1], ['Title Two',\
    ' Artist Two', ' Year Two', ' Rank Two', 2], ['Title Three',\
    ' Artist Three', ' Year Three', ' Rank Three', 3]]

def test_get_total_song_data2():
    """
    Test that given a CSV file containing song information and lyrics, returns a list
    containing [Title, Artist, Year, Rank, Frequency of Title in Lyrics].

    This test checks that the by_song parameter is False.
    """
    assert get_total_song_data("test_get_total_song_data.csv",by_song=False) ==\
    [['Title One', 'Title Two', 'Title Three'], [' Artist One', ' Artist Two',\
    ' Artist Three'], [' Year One', ' Year Two', ' Year Three'], [' Rank One',\
    ' Rank Two', ' Rank Three'], [1, 2, 3]]
