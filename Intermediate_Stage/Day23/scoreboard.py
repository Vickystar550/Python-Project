from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.goto((-200, 250))
        self.update_score()

    def update_score(self):
        """Update the screen with the score"""
        self.clear()
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def increase_level(self):
        """Increase the score and call the update_score method"""
        self.level += 1
        self.update_score()

    def game_over(self):
        """Displays the game over prompt when game is over"""
        self.goto((0, 0))
        self.write("GAME OVER", align="center", font=FONT)
