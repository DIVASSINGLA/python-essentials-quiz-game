# Python Essentials Quiz Game

A terminal-based multiple-choice quiz about Python basics. The game shuffles questions, checks answers, displays the player's score, and saves completed results locally.

## Requirements

- Python 3.8 or newer
- A terminal or command prompt
- No additional packages

## Setup and run

1. Install Python from [python.org](https://www.python.org/downloads/) if it is not already installed. On Windows, enable **Add Python to PATH** during installation.
2. Download or clone this repository.
3. Open a terminal in the repository folder containing `main.py`.
4. Check Python is installed:

   ```bash
   python --version
   ```

   If your system uses `python3`, run `python3 --version` instead.

5. Start the game:

   ```bash
   python main.py
   ```

   Or use `python3 main.py` where required.

6. Choose **1** to play, **2** to view previous results, or **3** to exit. Enter A, B, C, or D for each answer.

## Project files

- `main.py` — quiz game source code.
- `README.md` — setup and usage instructions.
- `.gitignore` — tells Git to ignore generated files.
- `quiz_results.json` — created automatically after a completed quiz to store scores.

## How it works

Questions are stored in the program as a list of dictionaries. The order is shuffled for each game. The program checks each answer, calculates the score, and saves the player's name, score, and date in `quiz_results.json`. Choose **View previous results** from the menu to see saved scores.

## Python concepts used

Functions, lists, dictionaries, loops, conditionals, user input, input validation, exception handling, randomization, dates, and JSON file handling.
