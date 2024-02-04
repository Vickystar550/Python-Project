from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 25, 'bold')


class ScoreBoard(Turtle):
    """ this class create the scoreboard object """
    def __init__(self):
        super().__init__()
        self.count = 0
        self.highest_count = 0
        self.color('green')
        self.penup()
        self.goto(0, 310)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """ write the score """
        self.write(arg=f'[ score:   {self.count} ]', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """ increase the scoreboard and write """
        self.count += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """ this method displays 'GAME OVER' when triggered """
        self.home()
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.count > self.highest_count:
            self.highest_count = self.count
            self.count = 0
        self.clear()
        self.write(f"Score: {self.count}\tHighest Score: {self.highest_count}", align=ALIGNMENT, font=FONT)

