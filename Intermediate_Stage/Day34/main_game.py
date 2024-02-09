import tkinter as tk
import html

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# making the question from question_data a Question class object
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

THEME_COLOR = "#375362"

# make a QuizBrain class with the list containing the question object i.e question_bank
quiz = QuizBrain(question_bank)

# ask the first question
first_ask = f"Q.{quiz.question_number + 1}: {html.unescape(quiz.current_question.text)} (True/False): "


# button function:
def click(ans):
    """A click function for both buttons. It takes a bool string argument"""
    # checking answer first:
    score_quote = quiz.check_answer(ans)[0]
    score_label.config(text=score_quote)

    next_ask = quiz.next_question()

    if next_ask == "No Question":
        canvas.itemconfig(canvas_text, text="You've completed the quiz")
    else:
        # ask the next question
        ask_string = html.unescape(f"Q.{quiz.question_number}: {next_ask} (True/False): ")
        canvas.itemconfig(canvas_text, text=ask_string)

# ----------------- UI -----------------


# creating a tkinter screen:
window = tk.Tk()
window.title("Quizler")
window.config(padx=50, pady=50, bg=THEME_COLOR)

# canvas:
canvas = tk.Canvas(width=300, height=250, highlightthickness=0, bg="white")
canvas_text = canvas.create_text(150, 125, width=280, text=first_ask, fill=THEME_COLOR, font=("Arial", 20, "italic"))
canvas.grid(row=1, column=0, columnspan=2, pady=50)


# images:
false_image = tk.PhotoImage(file="images/false.png")
true_image = tk.PhotoImage(file="images/true.png")

# buttons:
false_button = tk.Button(image=false_image, highlightthickness=0, command=lambda: click("false"))
false_button.grid(row=2, column=0)

true_button = tk.Button(image=true_image, highlightthickness=0, command=lambda: click("true"))
true_button.grid(row=2, column=1)

# label:
score_label = tk.Label(width=10, text="Score: 0")
score_label.config(bg=THEME_COLOR, fg="white", pady=10, padx=5, font=("Courier", 16, "bold"))
score_label.grid(row=0, column=1)

window.mainloop()
