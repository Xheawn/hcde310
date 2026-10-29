# HW3 Part 4 – Save the results

AI Use: Stage 3 (Little helper)

Write a new function, `save_results(artworks, filename)`, that writes one line per artwork (title, artist, date) to a `.txt` file. Call it so every search saves its results. Then run `fetch.py` for real once, with a search you pick, and **commit the `.txt` file it made**: that's your proof the live call works.

You may have the AI write this function (about 10 lines) using the **[Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt)** (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in `ai_log.md` **as you go**:

Done early? Add `sort_by_date(artworks)` too (not graded).

---

## 1. Try
*paste your own attempt or plan for the function, even if it doesn't work*
def save_results(artworks, filename):
    for artwork in artworks:
        # write a line (title,artist_title,date_display)
        print(something)
    return

## 2. Chat (AI only)
*paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."*
**User:**

anyway, let's finish part 4 code first. check first what i have added for part 4. I am not sure the exact grammar or how exactly to writes one line to a `.txt` file

**Assistant:**

I’ll read your Part 4 attempt and log first, then guide you through the file-writing syntax without writing the function for you.

I read your attempt. The loop is a useful start. You still need to open a file, write each artwork’s text, choose a filename, and protect the call against failed requests. Also, the stray `'''` on **line 100** starts an unfinished multiline string—remove it before running.

Your **Try** section in `ai_log.md` is blank; save your current attempt there before revising it.

Here’s a tiny example for a **different task**, saving a reminder:

```python
with open("reminder.txt", "w", encoding="utf-8") as note:
    note.write("Water the plants\n")
```

What do you predict will be inside `reminder.txt` after this runs?

**User:**

it will write a line "Water the plants" and starts a new line? now can you check my code inspired by your code snipet

**Assistant:**

Your prediction is correct: it writes “Water the plants” followed by a newline. I’ll check how you adapted that pattern.

Your `.write()` line includes the required title, artist, date, and newline.

Three things need attention:

- **Line 100:** `filename` hasn’t been defined—choose a `.txt` filename for the call.
- **Line 100:** protect the call so it runs only after a successful response.
- **Line 96:** check whether opening the file belongs inside or outside the artwork loop.

Let’s focus on the third point: with the file opened in `"w"` mode **for every artwork**, do you predict the finished file contains **all artworks** or **only the last artwork**?

**User:**

go tackle one by one. for the first one can you check what I modified?

**Assistant:**

I’ll check only your filename change first.

You chose a filename, but **`results_saved.txt` needs quotation marks** when passed as literal text.

Without quotes, Python treats it as the name `results_saved` followed by an attribute named `txt`, rather than as a filename.

Should the filename argument here be a **string** or a **variable you’ve already defined**?

**User:**

I see, done. Next.

**Assistant:**

Next, protect the `save_results` call so it runs only when the request succeeds. Otherwise, a 403 response leaves `data` undefined.

Keep the function definition outside the condition; guard only the call.

Which condition already used in your file checks whether the request succeeded?

**User:**

I see, done. Next.

**Assistant:**

Next is **where you open the file**. Currently, `open(..., "w")` is inside your artwork loop, so the file opens again for each artwork.

Before changing it, do you predict the finished file will contain **all artworks** or **only the last artwork**?

**User:**

so "w" is overwrite? then we have to use the one stands for "add"

**Assistant:**

Yes—**`"w"` clears the file when it opens**, and **`"a"` appends to existing contents**.

But you can keep `"w"` here. Open the file **once**, then write every artwork while that same file stays open. Each `.write()` continues after the previous one; it doesn’t erase earlier writes.

Using `"a"` would also keep results from previous searches, which could create duplicates.

To open the file once per search, which should be the outer block: **`with open(...)`** or **`for artwork ...`**?

**User:**

okay i see. now check my code agagin

**Assistant:**

I’ll check the filename, the success condition, and whether the file opens just once.

Your **filename and success guard are correct**.

You changed the mode to `"a"`, so earlier lines will now be preserved. However, the file still opens once per artwork, and each new search adds to the previous search’s results.

For a file containing only the current search, open it **once in `"w"` mode**, with the artwork loop **inside** that file-opening block.

Before changing anything else: if your current code saves five artworks twice, how many artwork lines do you predict the file will contain, assuming it started empty?

**User:**

how about now?

**Assistant:**

I’ll check the updated file-opening mode and indentation.

Your file-writing structure is now correct: the file opens **once in `"w"` mode**, the loop writes each artwork inside that block, and the call is protected by the success condition.

Before testing, record your prediction in `ai_log.md`.

One detail to predict: when an artwork’s `artist_title` is `None`, what do you expect your current file-writing line to put in the file for its artist?

**User:**

still getting 403

```text
(.venv) xiongyin@Xiongs-MacBook-Pro hw3 % python3 fetch.py
Search the Art Institute for: cat
403 Forbidden
```

**Assistant:**

The live server is still refusing the request. Your success guard correctly prevents saving an error response as artwork results.

We can test Part 4 using **`python3 check.py`**. It uses your saved sample data and simulated responses, so Cloudflare won’t affect it. It creates temporary test files; you’ll still need a successful live search and its saved file for submission.

Before running the checker, what do you predict your function will save for the **five sample artworks**, including the one whose artist is `None`?

**User:**

```text
(.venv) xiongyin@Xiongs-MacBook-Pro hw3 % python3 check.py
✓ calls the search URL
✓ sends the search term as q
✓ asks for artist_title in fields
✓ prints all 5 titles
✓ prints the artists
✓ known artists aren't printed as Unknown
✓ never prints None (null fields get a default)
✓ no results: prints a message, no crash
✓ server error (500): prints a message, no crash
✓ server error: the message includes the code and the reason
✓ count_by_artist gives the right counts for the sample
✓ save_results writes all 5 titles to a .txt file

All checks pass. Now run fetch.py for real, too.
(.venv) xiongyin@Xiongs-MacBook-Pro hw3 %
```

what can I or you do to solve this 403 forbidden?

**Assistant:**

I’ll check the museum’s current API guidance and Cloudflare’s explanation of these challenges, then look for a supported way to restore live access.

**I found a promising fix and tested it:**

| Same search request | Result |
|---|---|
| With the museum’s `AIC-User-Agent` header | **200 OK** |
| Without that header | **403 Forbidden** |

The museum’s [official documentation](https://api.artic.edu/docs/#authentication) asks applications to send **`AIC-User-Agent`**, containing the project name and a contact email. Earlier, we added only the standard `User-Agent`; I missed this museum-specific header.

In your existing `extra_header` dictionary:

- Keep your current `User-Agent` entry.
- Add another entry whose key is **`"AIC-User-Agent"`**.
- Its value should be a string identifying your HCDE310 project and your contact email.

This worked in my comparison, though we still need to verify it with your Python request. Your assignment code and file-writing logic can stay as they are.

Can you add that second header entry and show me your updated dictionary before running it?

**User:**

check how I added that.

```text
(.venv) xiongyin@Xiongs-MacBook-Pro hw3 % cat
```

And I have been stucking on this command for a while

## 3. Predict, then compare
*before you run the function, write what you think the file will contain for the sample data (`check.py` uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)*
I didn’t write down my prediction before the first run, so this comparison is written afterward. I would expect one line per artwork with its title, artist, and date. The actual file had 10 lines. The artwork without an artist name showed None, even though the terminal showed an Unknown message.


## 4. What surprised me
*one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print `none`, but `.get` gave the fallback `unknown`."*
I thought putting this line "with open(filename, "w", encoding="utf-8") as note:" anywhere is fine, so I wrote it in the for loop, which did not work cuz it needs to be outside the for loop to be opened once and not overwrite stuff.

## 5. Change one thing yourself
*once the function works, change one thing about it by hand, no AI. For example: a different line format (date first), a filename based on the search term, or sorted lines. Write what you changed and why, in one or two sentences.*
I just did a different line format (date first). Now in the txt file, you can better see the date for each artwork more clear.
