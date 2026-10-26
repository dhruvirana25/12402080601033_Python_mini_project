"""
Quiz Management System
A beginner-friendly Python mini project using Lists, Dictionaries, Functions, and Tkinter.
Run: python main.py
"""

import tkinter as tk
from tkinter import messagebox

# Each question is a dictionary. The question bank itself is a list of dictionaries.
QUESTIONS = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    {
        "question": "Which data type stores items in an ordered, changeable collection?",
        "options": ["Tuple", "Set", "List", "Integer"],
        "answer": "List"
    },
    {
        "question": "Which Tkinter widget is commonly used to display text?",
        "options": ["Label", "Entry", "Button", "Canvas only"],
        "answer": "Label"
    },
    {
        "question": "Which brackets are used to create a Python dictionary?",
        "options": ["()", "[]", "{}", "<>"],
        "answer": "{}"
    },
    {
        "question": "Which function displays a pop-up message in Tkinter?",
        "options": ["print()", "messagebox.showinfo()", "input()", "alert()"],
        "answer": "messagebox.showinfo()"
    },
    {
        "question": "What does len(my_list) return?",
        "options": [
            "The last item",
            "The number of items",
            "The first item",
            "The list type"
        ],
        "answer": "The number of items"
    },
    {
        "question": "Which statement is used to make a decision in Python?",
        "options": ["repeat", "if", "define", "select"],
        "answer": "if"
    },
    {
        "question": "Which method starts the Tkinter event loop?",
        "options": ["start()", "run()", "mainloop()", "window()"],
        "answer": "mainloop()"
    },
    {
        "question": "Which symbol is used for a single-line comment in Python?",
        "options": ["//", "/*", "#", "--"],
        "answer": "#"
    },
    {
        "question": "What is the result of 3 * 4 in Python?",
        "options": ["7", "12", "34", "1"],
        "answer": "12"
    }
]


class QuizManagementSystem:
    """Controls quiz navigation, answer selection, scoring, and result display."""

    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Management System")
        self.root.geometry("720x500")
        self.root.minsize(620, 450)
        self.root.configure(bg="#f2f5fb")

        self.current_index = 0
        self.score = 0
        self.user_answers = []
        self.selected_answer = tk.StringVar(value="")

        self.show_welcome_screen()

    def clear_window(self):
        """Remove the current screen's widgets before showing another screen."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_welcome_screen(self):
        """Display the introduction and start button."""
        self.clear_window()

        container = tk.Frame(self.root, bg="#f2f5fb", padx=35, pady=35)
        container.pack(expand=True, fill="both")

        tk.Label(
            container, text="QUIZ MANAGEMENT SYSTEM",
            font=("Arial", 22, "bold"), fg="#173b70", bg="#f2f5fb"
        ).pack(pady=(45, 15))

        tk.Label(
            container,
            text="Test your Python basics with a short multiple-choice quiz.",
            font=("Arial", 12), fg="#344054", bg="#f2f5fb",
            wraplength=520
        ).pack(pady=8)

        tk.Label(
            container, text=f"Total Questions: {len(QUESTIONS)}",
            font=("Arial", 11), fg="#344054", bg="#f2f5fb"
        ).pack(pady=8)

        tk.Button(
            container, text="Start Quiz", command=self.start_quiz,
            font=("Arial", 12, "bold"), bg="#2463eb", fg="white",
            activebackground="#1749b8", activeforeground="white",
            relief="flat", padx=28, pady=10, cursor="hand2"
        ).pack(pady=25)

        tk.Label(
            container, text="Built with Python and Tkinter",
            font=("Arial", 9), fg="#667085", bg="#f2f5fb"
        ).pack(side="bottom", pady=8)

    def start_quiz(self):
        """Initialize quiz state and show the first question."""
        self.current_index = 0
        self.score = 0
        self.user_answers = [""] * len(QUESTIONS)
        self.show_question()

    def show_question(self):
        """Render the current question and its answer options."""
        self.clear_window()
        self.selected_answer = tk.StringVar(
            value=self.user_answers[self.current_index]
        )

        container = tk.Frame(self.root, bg="#f2f5fb", padx=30, pady=25)
        container.pack(expand=True, fill="both")

        tk.Label(
            container, text="QUIZ MANAGEMENT SYSTEM",
            font=("Arial", 17, "bold"), fg="#173b70", bg="#f2f5fb"
        ).pack(anchor="w", pady=(0, 10))

        progress = f"Question {self.current_index + 1} of {len(QUESTIONS)}"
        tk.Label(
            container, text=progress, font=("Arial", 10, "bold"),
            fg="#2463eb", bg="#f2f5fb"
        ).pack(anchor="w", pady=(0, 14))

        question_data = QUESTIONS[self.current_index]
        tk.Label(
            container, text=question_data["question"],
            font=("Arial", 14, "bold"), fg="#101828", bg="#f2f5fb",
            wraplength=630, justify="left", anchor="w"
        ).pack(fill="x", pady=(0, 18))

        for option in question_data["options"]:
            tk.Radiobutton(
                container, text=option, variable=self.selected_answer,
                value=option, font=("Arial", 11), fg="#344054",
                bg="#f2f5fb", activebackground="#f2f5fb",
                selectcolor="#dbeafe", anchor="w", padx=8, pady=5
            ).pack(fill="x", anchor="w")

        button_row = tk.Frame(container, bg="#f2f5fb")
        button_row.pack(side="bottom", fill="x", pady=(20, 0))

        if self.current_index > 0:
            tk.Button(
                button_row, text="Previous", command=self.previous_question,
                font=("Arial", 10), padx=15, pady=8
            ).pack(side="left")

        if self.current_index < len(QUESTIONS) - 1:
            tk.Button(
                button_row, text="Next Question", command=self.next_question,
                font=("Arial", 10, "bold"), bg="#2463eb", fg="white",
                padx=15, pady=8, relief="flat"
            ).pack(side="right")
        else:
            tk.Button(
                button_row, text="Submit Quiz", command=self.submit_quiz,
                font=("Arial", 10, "bold"), bg="#16803c", fg="white",
                padx=15, pady=8, relief="flat"
            ).pack(side="right")

    def save_current_answer(self):
        """Save the selected option for the current question."""
        self.user_answers[self.current_index] = self.selected_answer.get()

    def next_question(self):
        """Save the answer and move to the next question."""
        self.save_current_answer()
        if self.current_index < len(QUESTIONS) - 1:
            self.current_index += 1
            self.show_question()

    def previous_question(self):
        """Save the answer and return to the previous question."""
        self.save_current_answer()
        if self.current_index > 0:
            self.current_index -= 1
            self.show_question()

    def calculate_score(self):
        """Compare saved answers with correct answers and return the score."""
        total_score = 0
        for index, question_data in enumerate(QUESTIONS):
            if self.user_answers[index] == question_data["answer"]:
                total_score += 1
        return total_score

    def submit_quiz(self):
        """Confirm submission, calculate the result, and display it."""
        self.save_current_answer()
        unanswered = sum(1 for answer in self.user_answers if not answer)

        if unanswered:
            confirm = messagebox.askyesno(
                "Unanswered Questions",
                f"You have {unanswered} unanswered question(s). Submit anyway?"
            )
            if not confirm:
                return

        self.score = self.calculate_score()
        self.show_result_screen()

    def show_result_screen(self):
        """Display the final score, percentage, and restart option."""
        self.clear_window()
        total = len(QUESTIONS)
        percentage = (self.score / total) * 100 if total else 0

        container = tk.Frame(self.root, bg="#f2f5fb", padx=35, pady=35)
        container.pack(expand=True, fill="both")

        tk.Label(
            container, text="QUIZ COMPLETED!",
            font=("Arial", 22, "bold"), fg="#173b70", bg="#f2f5fb"
        ).pack(pady=(35, 15))

        tk.Label(
            container, text=f"Your Score: {self.score} / {total}",
            font=("Arial", 18, "bold"), fg="#16803c", bg="#f2f5fb"
        ).pack(pady=8)

        tk.Label(
            container, text=f"Percentage: {percentage:.1f}%",
            font=("Arial", 14), fg="#344054", bg="#f2f5fb"
        ).pack(pady=5)

        if percentage >= 80:
            message = "Excellent work! You have a strong understanding."
        elif percentage >= 50:
            message = "Good effort! Review a few topics and try again."
        else:
            message = "Keep practising. You can improve with another attempt."

        tk.Label(
            container, text=message, font=("Arial", 11),
            fg="#344054", bg="#f2f5fb", wraplength=520
        ).pack(pady=12)

        tk.Button(
            container, text="Retake Quiz", command=self.start_quiz,
            font=("Arial", 11, "bold"), bg="#2463eb", fg="white",
            padx=20, pady=9, relief="flat"
        ).pack(pady=12)

        tk.Button(
            container, text="Exit", command=self.root.destroy,
            font=("Arial", 10), padx=20, pady=7
        ).pack()


def main():
    """Create the Tkinter window and start the application."""
    root = tk.Tk()
    QuizManagementSystem(root)
    root.mainloop()


if __name__ == "__main__":
    main()
