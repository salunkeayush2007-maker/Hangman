# 🎯 Hangman Game

A simple **Hangman game built with Python** as part of my Python learning journey.

The player has **6 lives** to guess the hidden word one letter at a time. Correct guesses reveal the letters, while incorrect guesses cost a life.

## 🎮 How to Play

1. Run `main.py`.
2. A random word is selected.
3. Guess the word by entering one letter at a time.
4. Correct guesses reveal the letter in the word.
5. Incorrect guesses reduce your lives by 1.
6. Guess the complete word before losing all 6 lives to win!

## ✨ Features

- Random word selection
- 6 lives per game
- Tracks correct guesses
- Tracks incorrect guesses
- Prevents guessing the same letter multiple times
- Displays Hangman stages based on remaining lives
- Win and lose conditions

## 📁 Project Structure

```text
Hangman/
│
├── main.py
├── hangman_art.py
├── hangman_words.py
├── README.md
└── .gitignore
```

### Files

- **`main.py`** — Contains the main game logic.
- **`hangman_art.py`** — Contains the Hangman logo and stages.
- **`hangman_words.py`** — Contains the list of possible words.
- **`README.md`** — Project documentation.
- **`.gitignore`** — Prevents unnecessary Python files such as `__pycache__` from being tracked.

## 🛠️ Technologies Used

- Python 3
- `random` module

## 📚 What I Learned

Through this project, I practiced:

- `while` loops
- `for` loops
- `if / elif / else`
- Lists
- String manipulation
- `break` and `continue`
- The `random` module
- User input
- Boolean conditions
- Basic game logic

## 🚀 Future Improvements

Possible improvements:

- Add difficulty levels
- Add a score system
- Add categories for words
- Validate user input
- Add more visual effects

---

**Built as part of my Python learning journey. 🐍**
