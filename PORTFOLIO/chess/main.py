from game_board import GameBoard
from game_logic import GameLogic


def main():
    logic = GameLogic()
    game = GameBoard(game_logic=logic)
    game.mainloop()


if __name__ == '__main__':
    main()
