# group_words_by_first_letter.py
Python script that reads words from a text file and organizes them into a dictionary grouped by first letter. Each key is a lowercase letter, and each value is a list of words beginning with that letter.

## What It Does

Given any plain text file, `dict.py` parses all the words and builds a dictionary where:
- Each **key** is a lowercase letter (`a` through `z`)
- Each **value** is a list of all words from the file that start with that letter

**Example output:**
```python
{
    'a': ['apple', 'and', 'around'],
    'b': ['banana', 'bright'],
    'c': ['cat', 'city', 'cool'],
    ...
}
```

---

## Usage

```python
from dict import build_dict

result = build_dict("sample.txt")
print(result)
```

Or to look up all words starting with a specific letter:

```python
result = build_dict("sample.txt")
print(result['a'])   # ['apple', 'and', 'around']
```

---

## How It Works

1. Opens the file and reads its entire contents as a string
2. Splits the string into individual words
3. Lowercases each word for consistent grouping
4. Iterates through the words, placing each one into the dictionary under its first letter
5. Returns the completed dictionary

---

## Requirements

- Python 3.x
- A plain `.txt` file to process — no external libraries needed

---

## Limitations

- Words are lowercased before grouping, so `Apple` and `apple` are treated as the same
- Punctuation attached to words (e.g. `word,` or `word.`) is not stripped — the first character is still a letter so grouping works, but the word retains its punctuation in the list
- Words starting with numbers or special characters will be grouped under that character as a key
