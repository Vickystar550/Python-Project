import math
from turtle import Turtle

GREEN = '#008000'
RED = '#880808'
YELLOW = '#8B8000'
BLUE = '#00008B'
THEME = '#4D4D4D'
TIMER_FONT = ('Arial', 25, 'bold')
SCORE_FONT = ('Courier', 25, 'bold')


class Scoreboard:
    def __init__(self):
        self.score = 0
        self.timer_object: Turtle = None
        self.player_one_score_object: Turtle = None
        self.player_two_score_object: Turtle = None

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
        self.timer_object.write(f'00:00', align='center', font=TIMER_FONT)

    def display_score(self, **kwargs):
        """initialize score display"""
        player: str = kwargs.get('player')

        score_turtle = Turtle()
        score_turtle.hideturtle()
        score_turtle.color(BLUE)
        score_turtle.penup()

        if player.lower() == 'one':
            self.player_one_score_object = score_turtle
            self.player_one_score_object.goto(-410, 410)
            align = 'left'
        else:
            self.player_two_score_object = score_turtle
            self.player_two_score_object.goto(410, 410)
            align = 'right'

        score_turtle.pendown()
        score_turtle.write(f'Player {player.title()}: {self.score}', align=align, font=SCORE_FONT)

    def update_timer(self, t_str: str):
        """update written time on the screen"""
        self.timer_object.clear()
        self.timer_object.goto(0, 410)
        self.timer_object.write(t_str, align='center', font=TIMER_FONT)

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

    def update_score(self, player: str):
        self.score += 1
        if player.lower() == 'one':
            self.player_one_score_object.clear()
            self.player_one_score_object.goto(-410, 410)
            self.player_one_score_object.write(f'Player One: {self.score}', align='left', font=SCORE_FONT)
        else:
            self.player_two_score_object.clear()
            self.player_two_score_object.goto(410, 410)
            self.player_two_score_object.write(f'Player Two: {self.score}', align='right', font=SCORE_FONT)
