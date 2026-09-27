import json
import random
from datetime import datetime
from pathlib import Path

RESULTS_FILE = Path(__file__).with_name("quiz_results.json")

QUESTIONS = [
    {
        "question": "Which keyword defines a function in Python?",
        "options": {"A": "func", "B": "def", "C": "function", "D": "make"},
        "answer": "B",
    },
    {
        "question": "Which data type stores whole numbers?",
        "options": {"A": "str", "B": "list", "C": "int", "D": "bool"},
        "answer": "C",
    },
    {
        "question": "What does len([4, 8, 12]) return?",
        "options": {"A": "2", "B": "3", "C": "4", "D": "24"},
        "answer": "B",
    },
    {
        "question": "Which symbol begins a comment in Python?",
        "options": {"A": "//", "B": "<!--", "C": "#", "D": "**"},
        "answer": "C",
    },
    {
        "question": "Which loop can go through each item in a list?",
        "options": {"A": "for", "B": "switch", "C": "repeat", "D": "case"},
        "answer": "A",
    },
    {
        "question": "What is the result of 7 // 2?",
        "options": {"A": "3.5", "B": "4", "C": "3", "D": "1"},
        "answer": "C",
    },
]


def ask_question(question, number, total):
    print(f"\nQuestion {number}/{total}: {question['question']}")
    for letter, text in question["options"].items():
        print(f"  {letter}. {text}")

    while True:
        answer = input("Your answer (A-D): ").strip().upper()
        if answer in question["options"]:
            break
        print("Please enter one of the displayed letters.")

    if answer == question["answer"]:
        print("Correct!")
        return 1

    print(f"Incorrect. The correct answer is {question['answer']}.")
    return 0


def save_result(name, score, total):
    results = []

    if RESULTS_FILE.exists():
        try:
            with RESULTS_FILE.open("r", encoding="utf-8") as file:
                results = json.load(file)
            if not isinstance(results, list):
                results = []
        except (json.JSONDecodeError, OSError):
            results = []

    results.append({
        "name": name,
        "score": score,
        "total": total,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })

    with RESULTS_FILE.open("w", encoding="utf-8") as file:
        json.dump(results, file, indent=2)


def show_results():
    if not RESULTS_FILE.exists():
        print("No saved results yet.")
        return

    try:
        with RESULTS_FILE.open("r", encoding="utf-8") as file:
            results = json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read saved results.")
        return

    if not results:
        print("No saved results yet.")
        return

    print("\n=== Previous Results ===")
    for result in results[-10:]:
        print(
            f"{result['date']} — {result['name']}: "
            f"{result['score']}/{result['total']}"
        )


def play_quiz():
    name = input("Enter your name: ").strip() or "Player"
    quiz_questions = QUESTIONS.copy()
    random.shuffle(quiz_questions)
    score = 0

    print(f"\nWelcome, {name}! Answer with A, B, C, or D.")
    for number, question in enumerate(quiz_questions, start=1):
        score += ask_question(question, number, len(quiz_questions))

    print(f"\nQuiz finished! {name}, your score is {score}/{len(quiz_questions)}.")
    save_result(name, score, len(quiz_questions))


def main():
    while True:
        print("\n=== Python Essentials Quiz ===")
        print("1. Play quiz")
        print("2. View previous results")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            play_quiz()
        elif choice == "2":
            show_results()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()  