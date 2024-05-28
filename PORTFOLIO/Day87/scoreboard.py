from turtle import Turtle


GREEN = '#008000'
RED = '#880808'
YELLOW = '#8B8000'
BLUE = '#00008B'
THEME = '#4D4D4D'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.display_timer()
        self.display_score(player='one')
        self.display_score(player='two')

    def display_timer(self):
        self.color('white')
        self.penup()
        self.goto(0, 410)
        self.pendown()
        self.write(f'00:00:00', align='center', font=('Arial', 25, 'bold'))

    def display_score(self, **kwargs):
        player: str = kwargs.get('player')

        self.color(BLUE)
        self.penup()
        if player.lower() == 'one':
            self.goto(-410, 410)
            align = 'left'
        else:
            self.goto(410, 410)
            align = 'right'

        self.pendown()
        self.write(f'Player {player.title()}', align=align, font=('Courier', 25, 'bold'))
