import random
from template import DesignTemplate

# varying the random generating seed
random.seed(random.randint(1, 100))


class AiPlayer(DesignTemplate):
    def __init__(self):
        super().__init__()
        # diagonal pivots:
        self.holder1 = [2, 4, 5]
        self.holder3 = [2, 5, 6]
        self.holder7 = [4, 5, 8]
        self.holder9 = [5, 6, 8]
        # mid pivots:
        self.holder2 = [1, 3, 5]
        self.holder4 = [1, 5, 7]
        self.holder5 = [2, 4, 6, 8]
        self.holder6 = [3, 5, 9]
        self.holder8 = [7, 5, 9]

    def guess(self):
        """Make a guess of a placeholder numeric position based on the previously occupied
        position

        :return:
        The placeholder numeric position is there's a previously occupied position
        otherwise, -1"""
        # getting the last row and column
        row = self.last_row
        col = self.last_col

        # first row
        if row == 1 and col == 1:
            return random.choice(self.holder1)
        elif row == 1 and col == 2:
            return random.choice(self.holder2)
        elif row == 1 and col == 3:
            return random.choice(self.holder3)
        # second row
        elif row == 2 and col == 1:
            return random.choice(self.holder4)
        elif row == 2 and col == 2:
            return random.choice(self.holder5)
        elif row == 2 and col == 3:
            return random.choice(self.holder6)
        # third row
        elif row == 3 and col == 1:
            return random.choice(self.holder7)
        elif row == 3 and col == 2:
            return random.choice(self.holder8)
        elif row == 3 and col == 3:
            return random.choice(self.holder9)
        else:
            return -1

    def ask_computer(self):
        """
        Determine the placeholder position based on the returned value from 'guess'

        :return:
        1. "r" - the row value of the placeholder
        2. "c" - the column value of the placeholder
        """
        num = self.guess()
        if num == 1:
            r = 1
            c = 1
            return r, c
        elif num == 2:
            r = 1
            c = 2
            return r, c
        elif num == 3:
            r = 1
            c = 3
            return r, c
        elif num == 4:
            r = 2
            c = 1
            return r, c
        elif num == 5:
            r = 2
            c = 2
            return r, c
        elif num == 6:
            r = 2
            c = 3
            return r, c
        elif num == 7:
            r = 3
            c = 1
            return r, c
        elif num == 8:
            r = 3
            c = 2
            return r, c
        elif num == 9:
            r = 3
            c = 3
            return r, c
        else:
            r = random.randint(1, 3)
            c = random.randint(1, 3)
            return r, c


class ExternalPlayer:
    def __init__(self):
        self.last_row = None
        self.last_col = None

    def ask_player(self):
        r = int(input('Enter your row value. From 1 to 3 allowed:\n'))
        c = int(input('Enter your column value. From 1 to 3 allowed:\n'))
        self.last_row, self.last_col = r, c
        return r, c
