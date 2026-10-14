# HW1 notes

## Part 4: Predict, run, explain

**Prediction for `predict.py` (written BEFORE running it):**

```text
0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
10
11
```

**What it actually printed:**

```text
0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
10
11
```

**Explain:**

The prediction matched the output. The loop uses positions 0, 1, and 2 because `range(3)` stops before 3.
Each line prints the position, the title at that position, and its year plus
100.And The last two lines measure different things: `len(titles)` counts the
10 items in the list, while `len(titles[0])` counts the 11 characters in
"The Bedroom", including the space.

## Part 5: Reflection (about 100 words)

Looking back at my Day 1 screenshot, I can connect the perspective controls
to lists, loops, and decisions. The app shows buttons for the figures, the
artist, and the era. Those choices could be stored in a list, with a loop
creating a button for each one. An `if` could check which perspective is
selected and decide which text to display. The selected woman has a dark
button and a highlighted outline, so a condition could control those styles.
