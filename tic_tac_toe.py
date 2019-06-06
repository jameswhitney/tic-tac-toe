######################################################################
# Create a simple tic tac toe game that takes user input, X or O.    #
# Each player takes a turn selecting a position on the board, 1 - 9. #
# Check for winning combination or if the combination is a draw.     #
# Regardless of a win or draw, ask the players if they want to       #
# play again.                                                        #
# ####################################################################

# Use random module to assign player order
import random


def create_board(board):

    # TODO: Create a blank tic tac toe board
    print('    |   |')
    print('  ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('    |   |')
    print('------------')
    print('    |   |')
    print('  ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('    |   |')
    print('------------')
    print('    |   |')
    print('  ' + board[3] + ' | ' + board[2] + ' | ' + board[1])
    print('    |   |')


def user_input():

    # TODO: Accept user input, check to make sure the input is either an X or O
    # Assign the input to a marker to represent X or O. The marker will be
    # used to determine which input will display on the board.
    marker = ''

    while not (marker == 'X' or marker == 'O'):

        # If input is anything other than X or O, continue to prompt user for valid input
        try: 
            marker = str(input('Player one: Plese enter either X or O: ')).upper()
        
        except ValueError:
            print('Please select either X or O')
            continue


    if marker == 'X':
        x_marker = ('X', 'O')
        print(x_marker)
    else:
        y_marker = ('O', 'X')
        print(y_marker)


def choose_player():

    # TODO: Randomly determine if player 1 or player 2 will start
    # the game first.
    if random.randint(0, 1) == 0:
        return 'Player 2 goes first'
    else:
        return 'Player 1 goes first'

def place_marker(board, marker, position):

    # TODO: Accept a board list object, either X or O as a marker
    # and the desired position for the marker on the board. Use
    # the board list index 1 - 9 to determine where on the board to
    # place the marker.
    board[position] = marker


def check_for_win(board, mark):

    # TODO: Accept board list object and mark, X or O, to determine
    # check what mark has won.
    pass


# Tests
test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'] # List is used to populate a test board
create_board(test_board) # Creates a board using the values within the test_board list
player = choose_player() # Randomly choose a player to go first
print(player)   # Print out which player will go first
user_input() # Checks that user input is only X or O (case insensitive)
place_marker(test_board, '&', 7) # Run place_marker using test parameters
create_board(test_board) # Print the new board based on test parameters passed in via the place_marker function
