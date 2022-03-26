import csv
import wikipedia


def create_song_list(year):
    """
    Creates a list of top 100 song titles and artists in a given year from a
    Wikipedia page containing a Billboard top 100 singles of the year list.

    Args:
        year: An int representing the year (between 1970 and 2021) to create
            the list for.

    Returns:
        A list of lists containing the top 100 song titles and artists in
            order.
    """
    page_title = "Billboard Year-End Hot 100 singles of " + str(year)
    page = wikipedia.page(title=(page_title), auto_suggest=False)
    full_html = page.html()

    table_start_index = full_html.find("wikitable sortable")
    table = full_html[table_start_index:]
    table_end_index = table.find("</tbody></table>")
    table = table[0:table_end_index]

    line_list = table.split("\n")

    for item in line_list:
        if len(item) < 9:
            line_list.remove(item)

    while len(line_list) > 400:
        del line_list[0]

    song_list = []

    for i in range(1, 400, 4):
        title_line = line_list[i]
        if "wiki" in title_line:
            title = title_line[title_line.find("title=") + 7:]
            title = title[0:title.find("\"")]
        else:
            title = title_line[title_line.find("\"") + 1:]
            title = title[0:title.find("\"")]

        artist_line = line_list[i+1]
        if "wiki" in artist_line:
            artist = artist_line[artist_line.find("title=") + 7:]
            artist = artist[0:artist.find("\"")]
        else:
            artist = artist_line[artist_line.find("<td>") + 4:]

        apostrophe = "&#39;"
        if apostrophe in title:
            title = title.replace(apostrophe, "'")
        if apostrophe in artist:
            artist = artist.replace(apostrophe, "'")

        ampersand = "&amp;"
        if ampersand in title:
            title = title.replace(ampersand, "&")
        if ampersand in artist:
            artist = artist.replace(ampersand, "&")

        if artist == "Perri &quot;Pebbles&quot; Reid":
            artist = "Pebbles"

        if artist == "Pussycat Dolls":
            artist = "The Pussycat Dolls"

        if artist == "Tupac Shakur":
            artist = "2Pac"

        if artist == "Sean Combs":
            artist = "Diddy"

        if artist == "Vanessa L. Williams":
            artist = "Vanessa Williams"

        if "song)" in title:
            title = title[0:title.find("(") - 1]
        if "(" in artist:
            artist = artist[0:artist.find("(") - 1]

        song_list.append([title, artist])

    return song_list


def get_all_top_songs(start, end):
    """
    Creates a list of top 100 songs and artists for a range of years.

    Args:
        start: An int representing the year to start at.
        end: An int representing the end for the year range.

    Returns:
        A list of top 100 songs and artists for all of the years in the range
        [start, end].
    """
    song_list = [str(start)]
    for i in range(start, end + 1):
        song_list.append(create_song_list(i))
    return song_list


def write_songs_to_file(song_list):
    """
    Takes a list of songs and writes the information to a CSV file.

    Args:
        song_list: A list containing song information.
    """
    with open("songs.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Artist", "Year", "Rank"])
        year_number = int(song_list[0])
        song_list = song_list[1:]
        for year in song_list:
            for index, song in enumerate(year):
                writer.writerow([song[0], song[1], year_number, index + 1])
            year_number += 1
