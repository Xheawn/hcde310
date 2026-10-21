# HW2 Part 5 – Debug log (`debug_log.md`)

Record **at least 2 errors** you hit. No errors? Break something on purpose and log it. For each error, write:

---

## Entry 1

### 1. Error message
*copy it exactly*
Traceback (most recent call last):
  File "/Users/xiongyin/Desktop/HCDE310/hcde310/hw2/part2.py", line 8, in <module>
    title = artwork.get["title"]
            ~~~~~~~~~~~^^^^^^^^^
TypeError: 'builtin_function_or_method' object is not subscriptable

### 2. What I thought it meant
I thought Python could not access the title because there was a problem with the artwork dictionary.

### 3. What it actually meant
Initially, I used square brackets after .get, which is a method. Square brackets try to access an item, but .get needs parentheses to call it.

### 4. The fix
I changed title = artwork.get["title"] to title = artwork.get("title", "Unknown"). This calls the method correctly and provides a fallback if the title is missing.

## Entry 2

### 1. Error message
*copy it exactly*
Traceback (most recent call last):
  File "/Users/xiongyin/Desktop/HCDE310/hcde310/hw2/part4.py", line 43, in <module>
    print(works_by("Claude Monet", artworks))
          ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/xiongyin/Desktop/HCDE310/hcde310/hw2/part4.py", line 23, in works_by
    titles = titles.append(artwork.get("title", "Unknown"))
             ^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'append'

### 2. What I thought it meant
I thought one of the artworks had a missing title, causing Python to use None instead.

### 3. What it actually meant
The .append() method changes the list but returns None. By writing titles = titles.append(...), I replaced the list with None after the first matching artwork. When the second matching artwork was found, Python tried to call .append() on None, causing the exception.

### 4. The fix
I changed the line to titles.append(artwork.get("title", "Unknown")). Removing the assignment keeps titles as a list while adding each matching title.