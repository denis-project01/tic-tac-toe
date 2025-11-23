#Denis Lebedev 40098355
#https://github.com/denis-project01/tic-tac-toe.git
import ticTacToe
import player


"""
Main Game will launch the game and alow the user to play by using the number 1 to 9.
"""

#Show the rules for the user
def rule_book():
    print("The rules of the Tic Tac Toe is a bit different from the original version")
    print("Rule 1: In order to win the user must place 3 of the same token either vertically or horizontally")
    print("\t\tIt is impossible to win by placing 3 tokens diagonally!")
    print("Rule 2: The user will always get to play the first move!")
    print("Rule 3: The user can choose between X or O, but it will not affect the order as stated in rule 2.")
    print("Rule 4: The user can choose to play against the computer or choose player vs player.")
    print("\t\tHowever, the second option will require the user to input for both players!")

'''
The function work as an infinite loop until the user gives the response that satisfy the requirement.
Return the given answer.
'''
def get_input(limit = 9):
    goodAnswer = True
    msg = ""
    while goodAnswer:
        msg = input("Please write a number: ")
        if msg.isdigit():
            msg = int(msg)
            #The number cannot be negative or exceed 9
            if 0 < msg <= limit:
                goodAnswer = False
            else:
                print(f'The input given is invalid or exceed the maximum value: {limit}.\nTry again')
        else:
            print("The input given is invalid.")
    #If we leave the while loop that mean we got our answer
    return msg

#Take an integer and return the token used by the player.
#Return empty string for validation purpose and safety.
def get_token(x):
    if x == 1:
        return "X"
    elif x == 2:
        return "O"
    else:
        return ""

#First login will show the rule book and let the user choose the options
def first_login():
    print('Welcome to TIC TAC TOE!!!')
    print('Since it is your first time launching the game please take a look at the rules!')
    rule_book()


#The function will simply let the user choose the token and return it
#The idea is to allow the user to change token while in the game so an independent function is needed
def choose_token():
    print('\n\nWhich token do you wish to use?\nPress 1 for X or 2 for O')
    return get_token(get_input(2))

#The function ask the user to play against itself or the computer
def vs_computer():
    print('Time to choose!\nDo you wish to play against the computer? Press 1\nElse Press 2 to play co-op locally!\n')
    if get_input(2) == 2:
        return False
    else:
        return True

#The function will ask a move from the user or the computer
def ask_move(player, game):
    #The first if check if it is a human
    if not player.ai:
        print(f'\nPlace the token: {player.token} on the board!')
        while not game.place_token(get_input(), player.token):
            print("Wrong the given number is already occupy\n")
            game.display_board()
        #return True to mention a round was done
        return True
    else:
        print("\nThe computer made a move!!!")
        #By default should always return True
        return game.place_token_computer(player.token)

#Ask the user if they want to continue/1, leave/2, change setting/3
def leave_or_continue(player1, player2):
    print('\nDo you wish to continue?!\nPress 1 to continue\nPress 2 to leave\nPress 3 to change the settings and the score will be reset')
    ans = get_input(3)
    #The user want to leave
    if ans == 2:
        return False
    #The user want to continue
    if ans == 1:
        return True
    #The user want to change the settings. The if is just for check
    if ans == 3:
        player1.reset_score()
        player2.reset_score()
        player1.set_token(choose_token())
        set_token_player2(player1, player2)
        return True

'''
Return True if a winner was selected else False to continue
'''
def check_winner(game, player1, player2):
    result = game.check_win()

    #The result is a draw and the maximum of round has been played
    if game.round == 9 and result == "":
        print('\nThe game ended in a draw!')
        game.display_board()
        game.reset_game()
        return True

    if result == player1.token:
        player1.increase_score()
        print(f'\nThe winning board for {player1.token}: ')
        game.display_board()
        game.reset_game()
        print(f'Player 1 won wow!!\nThe current score is player1: {player1.score} vs player2:{player2.score}')
        return True
    elif result == player2.token:
        player2.increase_score()
        print(f'\nThe winning board for {player2.token}: ')
        game.display_board()
        game.reset_game()
        print(f'Player 2 won wow!!\nThe current score is player1: {player1.score} vs player2:{player2.score}')
        return True

    #No winner yet
    return False

#Create the second player based on the user previous choice
def set_token_player2(player1, player2):
    if player1.token == "X":
        player2.set_token("O")
        player2.set_ai(vs_computer())
    else:
        player2.set_token("X")
        player2.set_ai(vs_computer())

#First message
first_login()

#Initialize necessary variable
game = ticTacToe.TicTacToe()
#By default, the first user is a human
player1 = player.Player(choose_token())
#Set with default token and ai, but will change
player2 = player.Player()

set_token_player2(player1, player2)

#Keep track if the user want to leave
gameState = True

while gameState:

    game.display_board()
    ask_move(player1, game)

    #At the 5th round you can check if there is a winner
    #The 10th move is always player2 so we do not need to consider it
    if game.round >= 5 and check_winner(game, player1, player2):
        gameState = leave_or_continue(player1, player2)
        #continue is required because the next move is for player2 which should not be
        continue

    game.display_board()
    ask_move(player2, game)

    if game.round >= 5 and check_winner(game, player1, player2):
        gameState = leave_or_continue(player1, player2)
        continue

