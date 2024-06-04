import math
from turtle import Turtle
from itertools import cycle
from typing import NamedTuple


ACTIVE_THEME = '#808080'
INACTIVE_THEME = '#2d2d2d'

TIMER_FONT = ('Arial', 30, 'bold')
SCORE_FONT = ('San Serif', 15, 'bold')
LABEL_FONT = ('San Serif', 18, 'bold')
THIRD_LINE_FONT = ('San Serif', 15, 'bold')

SECONDS = 60
LIVE = 150


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
    def __init__(self, scores_dict: dict):
        self.players = cycle(DEFAULT_PLAYERS)

        if scores_dict.get('last player') == 'first':
            self.current_player = Player(order='second')
        elif scores_dict.get('last player') == 'second':
            self.current_player = Player(order='first')
        else:
            # that is 'last player' was None
            self.current_player = next(self.players)

        self.score_one = scores_dict['player one'][0]
        self.score_two = scores_dict['player two'][0]

        self.fixed_seconds = SECONDS
        self.chances = LIVE
        self.reset_screen = False

        self.timer_object: Turtle = None
        self.chance_object: Turtle = None

        self.player_one_label: Turtle = None
        self.player_two_label: Turtle = None

        self.player_one_score_object: Turtle = None
        self.player_two_score_object: Turtle = None

        self.display_timer()
        self.display_chance()
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
        self.timer_object.goto(0, 410)
        self.timer_object.pendown()
        self.timer_object.write(f'00:00', align='center', font=TIMER_FONT)

    def display_chance(self):
        """initialize timer display on screen"""
        self.chance_object = Turtle()
        self.chance_object.hideturtle()
        self.chance_object.color(ACTIVE_THEME)
        self.chance_object.penup()
        self.chance_object.goto(0, 360)
        self.chance_object.pendown()
        self.chance_object.write(f'live remains: {self.chances}/{LIVE}', align='center',
                                 font=THIRD_LINE_FONT)

    def display_label(self, **kwargs):
        """initialize player label"""
        label: str = kwargs.get('label')

        label_turtle = Turtle()
        label_turtle.hideturtle()
        label_turtle.color(ACTIVE_THEME)
        label_turtle.penup()

        if label.lower() == 'one':
            self.player_one_label = label_turtle
            self.player_one_label.goto(-410, 410)
            align = 'left'

        else:
            self.player_two_label = label_turtle
            self.player_two_label.goto(410, 410)
            align = 'right'

        label_turtle.pendown()
        label_turtle.write(f'PLAYER {label.upper()}', align=align, font=LABEL_FONT)

    def display_score(self, **kwargs):
        """initialize score display"""
        player: str = kwargs.get('player')

        score_turtle = Turtle()
        score_turtle.hideturtle()
        score_turtle.color(ACTIVE_THEME)
        score_turtle.penup()

        if player.lower() == 'one':
            score_ = self.score_one
            self.player_one_score_object = score_turtle
            self.player_one_score_object.goto(-410, 360)
            align = 'left'
        else:
            score_ = self.score_two
            self.player_two_score_object = score_turtle
            self.player_two_score_object.goto(410, 360)
            align = 'right'

        score_turtle.pendown()
        score_turtle.write(f'score: {score_}', align=align, font=SCORE_FONT)

    def update_timer(self, t_str: str):
        """update written time on the screen"""
        self.timer_object.clear()
        self.timer_object.goto(0, 410)
        self.timer_object.write(t_str, align='center', font=TIMER_FONT)

    def update_chance(self):
        """update remaining chances on the screen"""
        self.chances -= 1
        self.chance_object.clear()
        self.chance_object.goto(0, 360)
        if self.chances > 0:
            c = self.chances
        else:
            c = 0
        self.chance_object.write(f'live remains: {c}/{LIVE}', align='center',
                                 font=THIRD_LINE_FONT)

    def countdown(self):
        """act like a stopwatch"""
        # reset screen if player current chances are zero
        if self.chances == 0:
            self.reset_screen = True
        else:
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
        self.chances = LIVE
        self.update_chance()
        self.current_player = next(self.players)
        self.fixed_seconds = SECONDS + 0.9
        self.countdown()
        self.reset_screen = False

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

    def get_scores(self):
        return {'player one': [self.score_one],
                'player two': [self.score_two],
                'last player': self.current_player.order}
