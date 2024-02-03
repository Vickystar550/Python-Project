from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(0, 265)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        """This function update the screen with the score."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """This increase the score and clears the previous written score"""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """Displays the game over prompt at the center"""
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

