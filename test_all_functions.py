"""
Test functions that clean and organize data.
"""

from collections import Counter
import pytest

from genius import (
    csv_to_list,
    format_list_for_genius,

)

from finder import (
    title_in_lyrics_one_song,
    get_total_song_data,
)

# Testing genius.py

#@pytest.mark.parametrize("csvTest1.csv")
def test_csv_to_list():
    """
    Check that a csv_to_list takes a CSV file containing song information and 
    converts it to a list.
    """
    assert csv_to_list("csvTest1.csv") == [['Title One', ' Artist One', \
        ' Year One', ' Rank One'], ['Title Two', ' Artist Two', ' Year Two', \
        ' Rank Two'], ['Title Three', ' Artist Three', ' Year Three', \
        ' Rank Three']]

# Testing finder.py

def test_title_in_lyrics_one_song():
    """
    Takes a list of information on a song and counts how many times
    the songs title is in the lyrics.
    """
    song = ['Hi','Bob','1999','12','Hi how are you hi hello hi']
    assert title_in_lyrics_one_song(song) == 3