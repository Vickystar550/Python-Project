from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Write to the screen the scores for each paddles"""
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """Increase and displays the left paddle new score"""
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        """Increase and displays the right paddle new score"""
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
