import tkinter as tk
import html

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    """ Create the game interface with tkinter"""

    def __init__(self, quiz_object: QuizBrain):
        # initialize the quiz object from the QuizBrain class <-- check QuizBrain class documentation
        self.quiz = quiz_object

        # the first question when class is initialized
        self.first_ask = (f"Q.{self.quiz.question_number + 1}: "
                          f"{html.unescape(self.quiz.current_question.text)} (True/False): ")

        # creating the tkinter screen with an initialized color
        self.window = tk.Tk()
        self.window.title("Quizler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        # creating the score label widget
        self.score_label = tk.Label(width=10, text="Score: 0")
        self.score_label.config(bg=THEME_COLOR, fg="white", pady=10, padx=5, font=("Courier", 16, "bold"))
        self.score_label.grid(row=0, column=1)

        # creating the canvas widget with a white background when initialized
        self.canvas = tk.Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas_text = self.canvas.create_text(150, 125,
                                                   text=self.first_ask,
                                                   fill=THEME_COLOR,
                                                   font=("Times New Roman", 20, "normal"),
                                                   width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # create the image object with the image files
        self.false_image = tk.PhotoImage(file="images/false.png")
        self.true_image = tk.PhotoImage(file="images/true.png")

        # create the buttons
        self.false_button = tk.Button(image=self.false_image,
                                      highlightthickness=0,
                                      command=lambda: self.click("false"))
        self.false_button.grid(row=2, column=0)

        self.true_button = tk.Button(image=self.true_image,
                                     highlightthickness=0,
                                     command=lambda: self.click("true"))
        self.true_button.grid(row=2, column=1)

        # initialize the tkinter screen loop
        self.window.mainloop()

    def click(self, ans):
        """A click function for both buttons. It takes a bool string argument"""
        self.score_manager(score_ans=ans)
        self.window.after(ms=2000, func=self.bring_next_question)

    def bring_next_question(self):
        """Get the next quiz question from the .next_question() method in the QuizBrain class"""

        # set the canvas background color to white for every new question
        self.canvas.config(bg="white")

        # get the next question text
        next_ask = self.quiz.next_question()

        # check if the returned question text is indeed a question:
        if next_ask == "No Question":
            # if not, display the canvas with the below message and disable the buttons
            self.canvas.itemconfig(self.canvas_text, text="You've completed the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        else:
            # if yes, ask
            # change the html character encoding to a readable human text
            ask_string = html.unescape(f"Q.{self.quiz.question_number + 1}: {next_ask} (True/False): ")
            self.canvas.itemconfig(self.canvas_text, text=ask_string)

    def score_manager(self, score_ans):
        """Manage the score label and the canvas widget color notification of the answer status"""
        # get the score tuple from the check_answer() method of the QuizBrain class
        score_tuple = self.quiz.check_answer(score_ans)
        # with the tuple, unpack the score text part
        score_quote = score_tuple[0]
        # unpack the status part <- check the check_answer method in the QuizBrain for more clarification
        score_status = score_tuple[-1]

        # displaying the color confirmation on the canvas:
        if score_status == "correct":
            # change the canvas widget background color to green is the answer was actually correct
            self.canvas.config(bg="green")
        elif score_status == "incorrect":
            # make the canvas widget background color to be red
            self.canvas.config(bg="red")

        # update the score label with the actual score
        self.score_label.config(text=score_quote)
