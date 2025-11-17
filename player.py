"""
The Player class contain information about the player.
More comprehensive data can be used or capture.
"""
class Player:
    #Set the data about a player: token for tictactoe, computer or human and score
    def __init__(self, token, ai = False):
        self.token = token
        self.ai = ai
        self.score = 0

    def increase_score(self):
        self.score += 1