# HW3 Part 2 + Part 3 + Part 4
#
# Instructions: README.md in this folder (same as the assignment on Canvas).

import requests

FIELDS = "id,title,artist_title,artist_display,date_display"

# add 3 fields I chose in part 1
three_more_fields = ["date_display", "artist_display", "_score"]
FIELDS_LIST = FIELDS.split(",")
for field in three_more_fields:
    duplicated = False
    for Field in FIELDS_LIST:
        if field == Field:
            duplicated = True
    if duplicated == False:
        FIELDS_LIST.append(field)

FIELDS = (",".join(FIELDS_LIST))

# Functions go here (above the code that runs)

term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"      # TODO: the search URL from step 2
params = {"q": term, "fields": FIELDS}   # TODO: q (the search term) and fields (FIELDS)
extra_header = {"User-Agent": "HCDE310-coursework/1.0", "AIC-User-Agent": "HCDE310 Project"}
response = requests.get(url, params=params, headers=extra_header)


# TODO step 3: check response.status_code before you use the data

if response.status_code == 200:
    data = response.json()
else:
    print(response.status_code, response.reason)

# TODO steps 4-5: loop over the results and print each one (reuse your HW2 printing code),
#                 print a default for null fields, and print a helpful message if there are no results

if response.status_code == 200: 
    if len(data["data"]) == 0:
        print("The List Is Empty!")
    else:
        for artwork in data["data"]:
            for field in FIELDS_LIST:
                if artwork.get(field) == None:
                    print(f"{field} is Unknown")
                else:
                    print(artwork.get(field, f"{field} is Unknown"))
            print()



# Part 3 – Count by artist
# Bring your count_by_artist function from HW2 into fetch.py, and print the counts after the results.
# The API's field names aren't the same as HW2's.
# What does the function need to look up now? Where does the call go?
# Check: the counts show up when you search, and nothing breaks when there are no results or an error. 

def count_by_artist(artworks):
    """Takes a list of artworks and returns a dictionary counting the works by each artist."""
    artist_counts = {}

    for artwork in artworks:
        if artwork.get("artist_title") == None:
            if "Unknown" in artist_counts:
                artist_counts["Unknown"] += 1
            else:
                artist_counts["Unknown"] = 1
        else:
            artist = artwork.get("artist_title", "Unknown")

            if artist in artist_counts:
                artist_counts[artist] += 1
            else:
                artist_counts[artist] = 1

    return artist_counts


if response.status_code == 200 and len(data["data"]) != 0:
    print(count_by_artist(data["data"]))


# Part 4 – Save the results
# Write a new function, save_results(artworks, filename), that writes one line per artwork (title, artist, date) to a .txt file.
# Call it so every search saves its results. Then run fetch.py for real once, with a search you pick, 
# and commit the .txt file it made: that's your proof the live call works.


def save_results(artworks, filename):
    with open(filename, "w", encoding="utf-8") as note:
        for artwork in artworks:
            # write a line (title,artist_title,date_display)
            note.write(f"{artwork["date_display"]} {artwork["title"]} {artwork["artist_title"]}\n")
        return

if response.status_code == 200: 
    save_results(data["data"], "results_saved.txt")