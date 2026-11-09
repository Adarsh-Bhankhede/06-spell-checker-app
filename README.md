# 📝 Spell Checker App

**Project - Spell Checker App**

## 📌 Description

Build a Python-based **Spell Checker App** that identifies and corrects spelling mistakes in user-provided text.

The program takes text from the user, checks each word for spelling errors, and automatically replaces incorrect words with their most likely correct spellings. It also displays the corrections made and allows the user to check multiple texts.

## ✨ Features

- Check spelling mistakes in user-provided text.
- Automatically correct misspelled words.
- Display each correction made by the program.
- Support custom names and words by adding them to the dictionary.
- Preserve punctuation while correcting text.
- Handle multiple text inputs in a single session.
- Display a message when no corrections are needed.

## 🔄 Program Flow

1. Create the `SpellCheckerApp` class.
2. Initialize the `SpellChecker` object.
3. Add custom names and words to the spell checker's dictionary.
4. Ask the user to enter text for spell checking.
5. Extract words and punctuation using regular expressions.
6. Check each word and find its correct spelling.
7. Display the corrections and generate the corrected text.
8. Ask the user whether they want to check another text.
9. Continue or exit the application based on the user's choice.

## 🛠️ Technologies Used

- Python
- `re` module
- `pyspellchecker` library

## 📦 Installation

Install the required library using the following command:

```bash
python -m pip install pyspellchecker
```

## ▶️ How to Run

1. Save the program as `spell_checker.py`.
2. Open a terminal in the project folder.
3. Run the following command:

```bash
python spell_checker.py
```

4. Enter the text you want to spell-check.
5. View the corrected text and choose whether to check another text.

## 🧠 Concepts Used

- Classes and Objects
- Constructors (`__init__`)
- Functions and Methods
- Regular Expressions (`re`)
- Lists
- `for` and `while` loops
- `if-else` statements
- String methods
- Exception and `None` handling
- Third-party Python libraries

---

**Part of my 12 Weeks → 12+ Projects challenge.** 🚀