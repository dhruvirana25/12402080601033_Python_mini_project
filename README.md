# Quiz Management System

A beginner-friendly desktop quiz application built with Python and Tkinter. It demonstrates **Lists, Dictionaries, Functions, Conditional Statements, Loops, and GUI programming**.

## Features
- Welcome screen and quiz start button
- Multiple-choice questions
- Previous and Next navigation
- Saves selected answers while navigating
- Score and percentage calculation
- Result message and retake option
- Confirmation when unanswered questions remain

## Requirements
- Python 3.9 or later recommended
- Tkinter (included with most standard Python installations)
- No third-party packages required

## How to Run
1. Install Python from https://www.python.org/downloads/ if it is not already installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

   ```bash
   python main.py
   ```

   On some Windows systems, use `py main.py`.

## Project Structure
```text
Quiz-Management-System/
├── main.py
└── README.md
```

## Concepts Used
- **List:** `QUESTIONS` stores the full question bank.
- **Dictionary:** Each question stores the question text, options, and correct answer using keys.
- **Functions:** Methods handle screens, navigation, answer saving, scoring, and results.
- **Tkinter:** Provides the window, labels, radio buttons, and buttons.
- **Loops and conditionals:** Display options and calculate the final score.

## Customizing the Quiz
Edit the `QUESTIONS` list near the top of `main.py`. Each question must follow this structure:

```python
{
    "question": "Your question here?",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "answer": "Option B"
}
```

The value of `answer` must exactly match one of the strings in `options`.

## Limitations
This is a simple local demo. Questions and scores are not stored permanently in a database or file, and it does not include administrator login.

