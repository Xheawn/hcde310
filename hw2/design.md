# HW2 Part 1 – Model first (in `design.md`, no code)

---

## 1. Why is `artworks` a list of dictionaries and not one big dictionary? What would you lose or gain the other way?
Because each dictionary represents one artwork, while the list represents the entire collection of artworks. This structure keeps each artwork’s fields grouped together and makes it easy to loop through the collection. Using one large dictionary could allow direct lookup if every artwork had a unique key, but it would make the records less clearly separated and could cause problems when titles are duplicated or missing.

## 2. Which fields are sometimes missing? What should the app show when they are?
The fields `artist`, `year`, and `medium` are sometimes missing, while every artwork has a `title`. When a field is missing, the app should display a clear placeholder such as “Unknown artist,” “Unknown year,” or “Medium unavailable” instead of showing an error or leaving the information unclear.