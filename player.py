"""
The Player class contain information about the player.
More comprehensive data can be used or capture.
"""
class Player:
    #Set the data about a player: token for tictactoe, computer or human and score
    def __init__(self, token ='X', ai = False):
        self.token = token
        self.ai = ai
        self.score = 0

    def increase_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

    #If the arg ai is a boolean the variable will change and return True else False meaning nothing changed
    def set_ai(self, ai):
        if isinstance(ai, bool):
            self.ai = ai
            return True
        else:
            return False

    #Allow to set a new token.
    def set_token(self, token):
        if token == 'X' or token == 'O':
            self.token = token
            return True
        return False