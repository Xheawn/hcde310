# In-class 6 notes

## What happens with a wrong key? What status code?

A request with an invalid key returned HTTP status
403 and the error code `API_KEY_INVALID`. The API rejected the request
instead of returning photos. My program checks the status code before
trying to use the photo data.

## Where does your key live, and why isn't it in earth.py?

My key lives in the local `in-class-6/.env` file as `NASA_API_KEY`.
`load_dotenv()` loads it, and `os.getenv("NASA_API_KEY")` reads it in Python.
The repository's `.gitignore` includes `.env`, and `git check-ignore`
confirmed that this file is ignored. It is also not tracked by Git.
Keeping the key out of `earth.py` lets me share the code without sharing
my private key on GitHub.

## Stuck? Where?

Stuck on some grammar issues, AI helped finding the correct grammar for what I intended to do.
