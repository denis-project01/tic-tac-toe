import random



"""
TicTacToe contain the logic necessary to play the game known as tic tac toe
"""
class TicTacToe:

    def __init__(self):
        self.winning_combo = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
        # (0, 4, 8), (2, 4, 6) -- diagonal off
        ]

        self.board = []
        self.create_board()
        self.round = 0

    '''
    The method will print the board of the current game
    '''
    def display_board(self):
        print('|---|---|---|')
        print(f'| {self.board[0]} | {self.board[1]} | {self.board[2]} |')
        print('|-----------|')
        print(f'| {self.board[3]} | {self.board[4]} | {self.board[5]} |')
        print('|-----------|')
        print(f'| {self.board[6]} | {self.board[7]} | {self.board[8]} |')
        print('|---|---|---|')

    '''
    The function will create a new game board that can be used by the functions we currently have.
    The board is made of string variable to define the solution.
    '''
    def create_board(self):
        new_board = []
        # populate the board with string
        for i in range(9):
            new_board.append(str(i + 1))
        self.board = new_board

    '''
    Return True if the token was placed else False
    '''
    def place_token(self, position, given_token):
        # The position is the number on the board.
        position -= 1
        # If the array return a digit it means it is free
        if self.board[position].isdigit():
            self.board[position] = given_token
            self.round += 1
            return True
        return False

    '''
    The logic of the AI is here to make possible changes easier
    '''
    def place_token_computer(self, token):
        temp = False
        #The requirement is that the computer place the token randomly
        while not temp:
            temp = self.place_token(random.randint(1, 10) - 1, token)

        return True


    '''
    Check a winner 
    '''
    def check_win(self):

        for combo in self.winning_combo:
            a, b, c = combo
            line = self.board[a] + self.board[b] + self.board[c]

            if line == "XXX":
                return line[0]
            elif line == "OOO":
                return line[0]
        # default return meaning we found no winning possibility
        return ""

    '''
    Reset the board and round 
    '''
    def reset_game(self):
        self.create_board()
        self.round = 0