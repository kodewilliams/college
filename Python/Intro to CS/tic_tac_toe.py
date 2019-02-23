from tic_tac_toe_graphics import *
import sys

board_values = [[None, None, None],
                [None, None, None],
                [None, None, None]]
occupied = {}
previous = 'x'
moves = 0
game_over = False

def CheckBoard():
    global moves
    global game_over

    # Check horizontals
    for row in board_values:
        check = set(row)
        if len(check) == 1 and None not in check:
            return True
            
    # Check verticals
    col = 0
    row = 0
    while col < 3:
        temp = []
        for row in range(3):
            temp.append(board_values[row][col])
        temp = set(temp)
        if len(temp) == 1 and None not in temp:
            return True
        col += 1
    
    # Check diagonals
    from_left = []
    from_right = []
    for i in range(3):
        from_left.append(board_values[i][i])
    col = 2
    for i in range(3):
        from_right.append(board_values[i][col])
        col -= 1
    from_left = set(from_left)
    from_right = set(from_right)

    if (len(from_left) == 1 and None not in from_left) or (len(from_right) == 1 and None not in from_right):
        return True
    

def SwitchMove():
    global previous
    global moves
    
    if previous == 'x':
        previous = 'o'
    else:
        previous = 'x'
    moves += 1
    board.display_message('Player ' + previous + '\'s turn')
    


def BoardClicked(col_index, row_index):
    global previous
    global moves
    global occupied
    global game_over
    
    current = str(col_index) + str(row_index)
    if current not in occupied and not game_over:
        print (previous)
        board.mark_square(col_index, row_index, previous)
        board_values[row_index][col_index] = previous
        occupied[current] = True
        if CheckBoard():
            board.display_message('Winner is ' + previous)
            game_over = True
            sys.exit()
        else:
            SwitchMove()
    else:
        if moves == 9:
            board.display_message('It\'s a draw.')
            game_over = True
            sys.exit()
        print ('Already played there')


board = TicTacToeBoard(3, 3, BoardClicked)
board.display_message('Player ' + previous + '\'s turn')


# Make sure mainloop() is the last line of code in this program!
mainloop()
