class DesignTemplate:
    def __init__(self):
        self.placeholder1 = '-'
        self.placeholder2 = '-'
        self.placeholder3 = '-'
        self.placeholder4 = '-'
        self.placeholder5 = '-'
        self.placeholder6 = '-'
        self.placeholder7 = '-'
        self.placeholder8 = '-'
        self.placeholder9 = '-'
        self.line = """_______________________"""
        self.last_row = None
        self.last_col = None

    def display_board(self):
        """Display the game board"""
        print('\n')
        print(f"""   {self.placeholder1}   |   {self.placeholder2}   |   {self.placeholder3}   """)
        print(self.line)
        print(f"""   {self.placeholder4}   |   {self.placeholder5}   |   {self.placeholder6}   """)
        print(self.line)
        print(f"""   {self.placeholder7}   |   {self.placeholder8}   |   {self.placeholder9}   """)
        print('\n')

    def is_match(self, value: str):
        """Checks for a matching pattern"""
        # row checking
        if self.placeholder1 == self.placeholder2 == self.placeholder3 == value:
            return True
        elif self.placeholder4 == self.placeholder5 == self.placeholder6 == value:
            return True
        elif self.placeholder7 == self.placeholder8 == self.placeholder9 == value:
            return True

        # column checking
        elif self.placeholder1 == self.placeholder4 == self.placeholder7 == value:
            return True
        elif self.placeholder2 == self.placeholder5 == self.placeholder6 == value:
            return True
        elif self.placeholder7 == self.placeholder8 == self.placeholder9 == value:
            return True

        # diagonal check
        elif self.placeholder1 == self.placeholder5 == self.placeholder9 == value:
            return True
        elif self.placeholder3 == self.placeholder5 == self.placeholder7 == value:
            return True
        else:
            return False

    def is_occupied(self, row, col):
        """Checks if a placeholder variable has 'X' or 'O' as variable"""
        # row 1
        if row == 1 and col == 1:
            if self.placeholder1 == 'X' or self.placeholder1 == 'O':
                return True

        elif row == 1 and col == 2:
            if self.placeholder2 == 'X' or self.placeholder2 == 'O':
                return True

        elif row == 1 and col == 3:
            if self.placeholder3 == 'X' or self.placeholder3 == 'O':
                return True

        # row 2
        elif row == 2 and col == 1:
            if self.placeholder4 == 'X' or self.placeholder4 == 'O':
                return True

        elif row == 2 and col == 2:
            if self.placeholder5 == 'X' or self.placeholder5 == 'O':
                return True

        elif row == 2 and col == 3:
            if self.placeholder6 == 'X' or self.placeholder6 == 'O':
                return True

        # row 3
        elif row == 3 and col == 1:
            if self.placeholder7 == 'X' or self.placeholder7 == 'O':
                return True

        elif row == 3 and col == 2:
            if self.placeholder8 == 'X' or self.placeholder8 == 'O':
                return True

        elif row == 3 and col == 3:
            if self.placeholder9 == 'X' or self.placeholder9 == 'O':
                return True

        # if no place is preoccupied
        else:
            return False

    def which_placeholder(self):
        row = self.last_row
        col = self.last_col
        if row == 1:
            if col == 1:
                return self.placeholder1
            elif col == 2:
                return self.placeholder2
            elif col == 3:
                return self.placeholder3
        elif row == 2:
            if col == 1:
                return self.placeholder4
            elif col == 2:
                return self.placeholder5
            elif col == 3:
                return self.placeholder6
        elif row == 3:
            if col == 1:
                return self.placeholder7
            elif col == 2:
                return self.placeholder8
            elif col == 3:
                return self.placeholder9
        else:
            return None

    def insert_values(self, row_: int, col_: int, value: str):
        """Insert a value to the specified variable"""
        if row_ == 1:
            if col_ == 1:
                self.placeholder1 = value
            elif col_ == 2:
                self.placeholder2 = value
            elif col_ == 3:
                self.placeholder3 = value
        elif row_ == 2:
            if col_ == 1:
                self.placeholder4 = value
            elif col_ == 2:
                self.placeholder5 = value
            elif col_ == 3:
                self.placeholder6 = value
        elif row_ == 3:
            if col_ == 1:
                self.placeholder7 = value
            elif col_ == 2:
                self.placeholder8 = value
            elif col_ == 3:
                self.placeholder9 = value

