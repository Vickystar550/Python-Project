import math
from turtle import Turtle
from itertools import cycle
from typing import NamedTuple

# GREEN = '#008000'
# RED = '#880808'
# YELLOW = '#8B8000'
# BLUE = '#00008B'
# THEME = '#4D4D4D'
ACTIVE_THEME = '#808080'
INACTIVE_THEME = '#2d2d2d'

TIMER_FONT = ('Arial', 30, 'bold')
SCORE_FONT = ('San Serif', 20, 'bold')
LABEL_FONT = ('San Serif', 18, 'bold')

SECONDS = 5


class Theme(NamedTuple):
    active: str
    inactive: str


class Player:
    """define players by order"""
    def __init__(self, order):
        self.order: str = order
        self.theme: tuple = Theme(active=ACTIVE_THEME, inactive=INACTIVE_THEME)


DEFAULT_PLAYERS = (
    (Player(order='first'), Player(order='second'))
)


class Scoreboard:
    def __init__(self):
        self.players = cycle(DEFAULT_PLAYERS)
        self.current_player = next(self.players)
        self.board_themes = cycle(self.current_player.theme)
        self.current_color = next(self.board_themes)

        self.score_one = 0
        self.score_two = 0
        self.fixed_seconds = SECONDS

        self.reset_screen = False

        self.timer_object: Turtle = None

        self.player_one_label: Turtle = None
        self.player_two_label: Turtle = None

        self.player_one_score_object: Turtle = None
        self.player_two_score_object: Turtle = None

        self.display_timer()
        self.display_label(label='one')
        self.display_label(label='two')
        self.display_score(player='one')
        self.display_score(player='two')

    def display_timer(self):
        """initialize timer display on screen"""
        self.timer_object = Turtle()
        self.timer_object.hideturtle()
        self.timer_object.color('white')
        self.timer_object.penup()
        self.timer_object.goto(0, 385)
        self.timer_object.pendown()
        self.timer_object.write(f'00:00', align='center', font=TIMER_FONT)

    def display_label(self, **kwargs):
        """initialize player label"""
        label: str = kwargs.get('label')

        label_turtle = Turtle()
        label_turtle.hideturtle()
        label_turtle.penup()

        if label.lower() == 'one':
            self.player_one_label = label_turtle
            self.player_one_label.goto(-410, 410)
            align = 'left'
            self.player_one_label.color(ACTIVE_THEME)  # at the start, player one is active

        else:
            self.player_two_label = label_turtle
            self.player_two_label.goto(410, 410)
            align = 'right'
            self.player_two_label.color(INACTIVE_THEME)

        label_turtle.pendown()
        label_turtle.write(f'PLAYER {label.upper()}', align=align, font=LABEL_FONT)

    def display_score(self, **kwargs):
        """initialize score display"""
        player: str = kwargs.get('player')

        score_turtle = Turtle()
        score_turtle.hideturtle()
        score_turtle.penup()

        if player.lower() == 'one':
            self.player_one_score_object = score_turtle
            self.player_one_score_object.goto(-410, 360)
            align = 'left'
            self.player_one_score_object.color(ACTIVE_THEME)  # at the start, player one is active
        else:
            self.player_two_score_object = score_turtle
            self.player_two_score_object.goto(410, 360)
            align = 'right'
            self.player_two_score_object.color(INACTIVE_THEME)

        score_turtle.pendown()
        score_turtle.write(f'score: 0', align=align, font=SCORE_FONT)

    def update_timer(self, t_str: str):
        """update written time on the screen"""
        self.timer_object.clear()
        self.timer_object.goto(0, 385)
        self.timer_object.write(t_str, align='center', font=TIMER_FONT)

    def countdown(self):
        """act like a stopwatch"""
        if self.fixed_seconds >= 0:
            minutes = math.floor(self.fixed_seconds / 60)
            actual_sec = math.floor(self.fixed_seconds % 60)

            if actual_sec < 10:
                actual_sec = f'0{actual_sec}'

            if minutes < 10:
                minutes = f'0{minutes}'

            self.update_timer(t_str=f'{minutes}:{actual_sec}')
            self.fixed_seconds -= 1
        else:
            self.reset_screen = True

    def toggle(self):
        """toggle player's turn"""
        self.current_player = next(self.players)

        # toggle active color for player scoreboard

        if self.current_player.order == 'first':
            print('first')
            # make player one color active
            self.player_one_label.color(ACTIVE_THEME)
            self.player_one_score_object.color(ACTIVE_THEME)

            # make player two color inactive
            self.player_two_label.color(INACTIVE_THEME)
            self.player_two_score_object.color(INACTIVE_THEME)

        if self.current_player.order == 'second':
            # make player one color inactive
            self.player_one_label.color(INACTIVE_THEME)
            self.player_one_score_object.color(INACTIVE_THEME)

            # make player two color inactive
            self.player_two_label.color(ACTIVE_THEME)
            self.player_two_score_object.color(ACTIVE_THEME)

        self.fixed_seconds = SECONDS + 0.9
        self.countdown()

    def update_score(self, score):
        """update each player's score"""

        if self.current_player.order == 'first':
            self.score_one += score
            self.player_one_score_object.clear()
            self.player_one_score_object.goto(-410, 360)
            self.player_one_score_object.write(f'score: {self.score_one}', align='left', font=SCORE_FONT)

        if self.current_player.order == 'second':
            self.score_two += score
            self.player_two_score_object.clear()
            self.player_two_score_object.goto(410, 360)
            self.player_two_score_object.write(f'score: {self.score_two}', align='right', font=SCORE_FONT)
