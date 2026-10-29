# HW3 Part 1 – Read the response first

AI Use: Stage 2 (Tutor)

Open `sample_response.json` (a saved Art Institute of Chicago search). In `notes.md`:

---

## 1. The total number of results is at `data["pagination"]["total"]`. What's the path to the first artwork's title?
The total number of result at `data["pagination"]["total"]`is 133170. And the path to the first artwork's title is `data["data"][0]["title"]`.

## 2. Find 3 more fields you'd want to show a user, and their paths
I'd like to show:
"date_display": `data["data"][0]["date_display"]`
"artist_display": `data["data"][0]["artist_display"]`
"_score": `data["data"][0]["_score"]`

## 3. Which fields are `null` for some works?
I found that at there is a null at `data["data"][2]["artist_title"]` and another one at `data["preference"]`.

## 4. Predict
*open `fetch.py` and read it, but don't change anything yet. What do you think will happen when you run it?*
I think when I run fetch.py, it will cause an error because the request needs a valid URL, so an empty one causes an error before a response is returned.

## 5. Run it
*run `python3 fetch.py`. When it asks for a search term, type a word (like `cat`) and press Enter. What actually happened? Read the traceback bottom line first: what went wrong, and which line of your file caused it?*

Bottom line shows "requests.exceptions.MissingSchema: Invalid URL '': No scheme supplied. Perhaps you meant https://?". MissingSchema means the URL is missing a scheme—the beginning such as https://. Here, Invalid URL '' shows that the entire URL is empty.Line 16 "response = requests.get(url, params=params)" caused this error. the program stop before it could receive a response because the url used to access the website is empty and requests wouldn't work. Requests can make requests, but this call fails because the empty URL gives it no destination.


Error message:
(.venv)MacBook-Pro hw3 % python3 fetch.py
Search the Art Institute for: cat
Traceback (most recent call last):
  File "/Users/xiongyin/Desktop/HCDE310/hcde310/hw3/fetch.py", line 16, in <module>
    response = requests.get(url, params=params)
  File "/Users/xiongyin/Desktop/HCDE310/hcde310/.venv/lib/python3.14/site-packages/requests/api.py", line 87, in get
    return request("get", url, params=params, **kwargs)
  File "/Users/xiongyin/Desktop/HCDE310/hcde310/.venv/lib/python3.14/site-packages/requests/api.py", line 71, in request
    return session.request(method=method, url=url, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/xiongyin/Desktop/HCDE310/hcde310/.venv/lib/python3.14/site-packages/requests/sessions.py", line 635, in request
    prep = self.prepare_request(req)
  File "/Users/xiongyin/Desktop/HCDE310/hcde310/.venv/lib/python3.14/site-packages/requests/sessions.py", line 541, in prepare_request
    p.prepare(
    ~~~~~~~~~^
        method=method.upper(),
        ^^^^^^^^^^^^^^^^^^^^^^
    ...<10 lines>...
        hooks=merge_hooks(request.hooks, self.hooks),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Users/xiongyin/Desktop/HCDE310/hcde310/.venv/lib/python3.14/site-packages/requests/models.py", line 439, in prepare
    self.prepare_url(url, params)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/Users/xiongyin/Desktop/HCDE310/hcde310/.venv/lib/python3.14/site-packages/requests/models.py", line 514, in prepare_url
    raise MissingSchema(
    ...<2 lines>...
    )
requests.exceptions.MissingSchema: Invalid URL '': No scheme supplied. Perhaps you meant https://?