import time
from template import DesignTemplate
from gamers import AiPlayer, ExternalPlayer

# initializing objects:
design_template = DesignTemplate()
ai = AiPlayer()
external_player = ExternalPlayer()


def external():
    """The external player's function

    Manages the game play for an external player
    """
    e_row, e_col = external_player.ask_player()

    # storing position variable
    design_template.last_row = e_row
    design_template.last_col = e_col

    # check if position is already occupied
    if design_template.is_occupied(row=e_row, col=e_col):
        print('Position already occupied.')
        design_template.display_board()
        # repeat the process
        external()
    else:
        # insert X to the specified placeholder
        design_template.insert_values(row_=e_row, col_=e_col, value='X')
        # print the game board
        design_template.display_board()


def computer():
    """The Ai player's function

    Manages the game play for the Computer or Ai"""
    a_row, a_col = ai.ask_computer()

    # check if position is already occupied
    if design_template.is_occupied(row=a_row, col=a_col):
        computer()
    else:
        design_template.insert_values(row_=a_row, col_=a_col, value='O')
        design_template.display_board()


# print the welcome message with the board template:
print('\nWelcome to the tic tac toe game')
design_template.display_board()

# start the game:
counter = 9

while counter > 0:
    counter -= 1

    if counter % 2 == 0:  # the external player takes an even turn
        if design_template.is_match(value='X'):
            print('\nRESULT:\texternal player wins')
            break
        elif design_template.is_match(value='O'):
            print('\nRESULT:\tcomputer wins')
            break
        else:
            external()
    else:
        print('\tPLEASE WAIT')
        # slow down after each play
        time.sleep(1)
        if design_template.is_match(value='X'):
            print('\nRESULT:\texternal player wins')
            break
        elif design_template.is_match(value='O'):
            print('\nRESULT:\tcomputer wins')
            break
        else:
            computer()


# if no winner emerges:
print('\nRESULT:\tDraw!!!')
