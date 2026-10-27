import requests
import json

url = "https://api.artic.edu/api/v1/artworks/search"

all_artworks = []

for page in [1, 2]:
    params = {
        "q": "food",
        "limit": 50,
        "page": page,
        "fields": "id,title,artist_title,date_display,medium_display,image_id"
    }
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, params=params, headers=headers)
    
    data = response.json()

    all_artworks.extend(data["data"])

with open("group_d.json", "w") as file:
    json.dump(all_artworks, file, indent=2)

print("Saved", len(all_artworks), "artworks")

FIELDS = "title,date_display,artist_title"


print(len(all_artworks))

    
# part 2 - clean data
FIELDS = "title,date_display,artist_title"

with open("group_d.json", "r", encoding="utf-8") as file:
    all_artworks = json.load(file)

artworks_cleaned = []

for artwork in all_artworks[:5]:
    cleaned = {field: artwork.get(field) for field in FIELDS.split(",")}
    artworks_cleaned.append(cleaned)

with open("artworks_cleaned.json", "w", encoding="utf-8") as file:
    json.dump(artworks_cleaned, file, indent=2, ensure_ascii=False)

# part 3 - Page Maker

# ToDo:

