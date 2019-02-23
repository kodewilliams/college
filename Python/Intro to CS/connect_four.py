from connect_four_graphics import *
import sys


def ShowBoard():
    for row in board_values:
        print (row)

def GameOver():
    global current
    global cols
    global rows
    global winning_mark

    # Check rows
    for index in range(rows-1, -1, -1):
        row = board_values[index]
        seq = 0
        x = row[0]
        for item in row:
            if item == x:
                seq += 1
            else:
                seq = 1
                x = item
            if seq == winning_mark and item != None:
                return True

    # Check columns
    for column in range(cols):
        seq = 0
        x = board_values[rows-1][column]
        for row in range(rows-1, -1, -1):
            if board_values[row][column] == x:
                seq += 1
            else:
                seq = 1
                x = board_values[row][column]
            if seq == winning_mark and board_values[row][column] != None:
                return True

    # Go to each square
    for row in range(rows-1, -1, -1):
        for col in range(cols):
            current_row = row
            current_col = col
                
            # Up right
            r = current_row
            c = current_col
            seq = 0
            x = board_values[r][c]
            while r >= 0 and c <= cols-1:
                if board_values[r][c] == x:
                    seq += 1
                else:
                    seq = 1
                    x = board_values[r][c]
                if seq == winning_mark and board_values[r][c] != None:
                    return True
                r -= 1
                c += 1

                
            # Up left
            r = current_row
            c = current_col
            seq = 0
            x = board_values[r][c]
            while r >= 0 and c >= 0:
                if board_values[r][c] == x:
                    seq += 1
                else:
                    seq = 1
                    x = board_values[r][c]
                if seq == winning_mark and board_values[r][c] != None:
                    return True
                r -= 1
                c -= 1

    return False



def ChangePlayer():
    global current
    global color1
    global color2
    global moves

    if current == color1:
        current = color2
    else:
        current = color1
    board.display_message(current + '\'s turn')
    moves += 1


def IsPlayable(col):
    for i in range(len(board_values)-1, -1, -1):
        if board_values[i][col] == None:
            return str(i)
    return False


def BoardClicked(col_index):
    global current
    global game_over
    global moves
    global rows
    global cols

    if game_over == True:
        sys.exit()
    elif game_over == False and moves >= (rows * cols):
        board.display_message('It\'s a draw.')
        game_over = True
    else:
        result = IsPlayable(col_index)
        if result != False:
            result = int(result)
            board.add_chip(col_index, result, current)
            board_values[result][col_index] = current
            if GameOver():
                board.display_message(current + ' wins')
                game_over = True
            else:
                ChangePlayer()
        else:
            board.display_message('Illegal play')


rows = int(input('Enter desired rows: '))
cols = int(input('Enter desired columns: '))
winning_mark = int(input('Enter number of chips to win: '))
color1 = input('Player 1 color: ')
color2 = input('Player 2 color: ')
current = color1
game_over = False
moves = 0

board_values = []
for r in range(rows):
    board_values.append([])
    for c in range(cols):
        board_values[r].append(None)

board = ConnectFourBoard(rows, cols, BoardClicked)
board.display_message(current + '\'s turn')

# Make sure mainloop() is the last line of code in this program!
mainloop()
