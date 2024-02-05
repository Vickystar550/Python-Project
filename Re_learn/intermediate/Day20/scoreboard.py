from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("black")
        self.penup()
        self.goto(0, 265)
        self.update_scoreboard()
        self.hideturtle()
        self.end = False

    def update_scoreboard(self):
        """This function update the screen with the score."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """This increase the score and clears the previous written score"""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Displays the game over prompt at the center"""
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        """Reset the score and assign value if high score"""
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def end_game(self):
        """Set the end attribute to true"""
        self.end = True


