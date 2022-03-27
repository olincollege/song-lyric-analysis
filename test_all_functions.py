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
    # get_total_song_data,
)

# Testing genius.py

@pytest.mark.parametrize("song", csv_to_list)
def test_csv_to_list(song):
    """
    Test that a string representing a strand of DNA gets mapped to the rest of
    its open reading frame.

    Check that given a string representing a strand of DNA as defined above, the
    rest_of_orf function returns a string representing a strand of DNA for the
    rest of the given strand's open reading frame. This is the original strand
    until reading sets of three nucleotides results in a STOP codon, or the
    entire strand if no such codon appears when reading the strand.

    Args:
        strand: A string representing a strand of DNA.
        rest: A string representing the expected rest of the open reading frame
            of strand, or the entirety of strand if reading it does not result
            in a STOP codon at any point.
    """

    song = ["Hello","Bob","1000","23","Hello i miss you hello how are you ta da"]
    assert title_in_lyrics_one_song(song) == 2

# Testing finder.py

@pytest.mark.parametrize("song", title_in_lyrics_one_song)
def test_title_in_lyrics_one_song(song):
    """
    Test that a string representing a strand of DNA gets mapped to the rest of
    its open reading frame.

    Check that given a string representing a strand of DNA as defined above, the
    rest_of_orf function returns a string representing a strand of DNA for the
    rest of the given strand's open reading frame. This is the original strand
    until reading sets of three nucleotides results in a STOP codon, or the
    entire strand if no such codon appears when reading the strand.

    Args:
        strand: A string representing a strand of DNA.
        rest: A string representing the expected rest of the open reading frame
            of strand, or the entirety of strand if reading it does not result
            in a STOP codon at any point.
    """

    song = ["Hello","Bob","1000","23","Hello i miss you hello how are you ta da"]
    assert title_in_lyrics_one_song(song) == 2