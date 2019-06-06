######################################################################
# Create a simple tic tac toe game that takes user input, X or O.    #
# Each player takes a turn selecting a position on the board, 1 - 9. #
# Check for winning combination or if the combination is a draw.     #
# Regardless of a win or draw, ask the players if they want to       #
# play again.                                                        #
# ####################################################################


def show_board(board):
    
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
    pass


def place_marker(board, marker, position):

    # TODO: Accept a board list object, either X or O as a marker
    # and the desired position for the marker on the board. Use
    # the board list index 1 - 9 to determine where on the board to
    # place the marker.
    pass


def check_for_win(board, mark):

    # TODO: Accept board list object and mark, X or O, to determine
    # check what mark has won.
    pass


# Test each function 
test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
show_board(test_board)