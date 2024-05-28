import math
from turtle import Turtle

GREEN = '#008000'
RED = '#880808'
YELLOW = '#8B8000'
BLUE = '#00008B'
THEME = '#4D4D4D'


class Scoreboard:
    def __init__(self):
        self.timer_object = None
        self.player_one_score = None
        self.player_two_score = None

        self.display_timer()
        self.display_score(player='one')
        self.display_score(player='two')

    def display_timer(self):
        """initialize timer display on screen"""
        self.timer_object = Turtle()
        self.timer_object.hideturtle()
        self.timer_object.color('white')
        self.timer_object.penup()
        self.timer_object.goto(0, 410)
        self.timer_object.pendown()
        self.timer_object.write(f'00:00', align='center', font=('Arial', 25, 'bold'))

    def display_score(self, **kwargs):
        """initialize score display"""
        player: str = kwargs.get('player')

        score = Turtle()
        score.hideturtle()

        score.color(BLUE)
        score.penup()

        if player.lower() == 'one':
            self.player_one_score = score
            score.goto(-410, 410)
            align = 'left'
        else:
            self.player_two_score = score
            score.goto(410, 410)
            align = 'right'

        score.pendown()
        score.write(f'Player {player.title()}', align=align, font=('Courier', 25, 'bold'))

    def update_timer(self, t_str: str):
        """update written time on the screen"""
        self.timer_object.clear()
        self.timer_object.goto(0, 410)
        self.timer_object.write(t_str, align='center', font=('Arial', 25, 'bold'))

    def countdown(self, sec):
        """act like a stopwatch"""
        if sec >= 0:
            minutes = math.floor(sec / 60)
            actual_sec = math.floor(sec % 60)

            if actual_sec < 10:
                actual_sec = f'0{actual_sec}'

            if minutes < 10:
                minutes = f'0{minutes}'

            self.update_timer(t_str=f'{minutes}:{actual_sec}')
        else:
            self.update_timer(t_str='00:00')
