from tkinter import *


CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600

class TicTacToeBoard():
    def __init__(self, num_rows, num_columns, user_clicked_func):
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.user_clicked_func = user_clicked_func
        self.master = Tk()
    
        self.canvas = Canvas(
            self.master, 
            width = CANVAS_WIDTH,
            height = CANVAS_HEIGHT)
        self.message = self.canvas.create_text(
            CANVAS_WIDTH / 2, 50, text='', font=('Helvetica', 32),
            anchor=CENTER)
        self.board_coords = (50, CANVAS_HEIGHT - 500, CANVAS_WIDTH - 50, CANVAS_HEIGHT)

        # Draw columns
        col_width = (self.board_coords[2] - self.board_coords[0]) / self.num_columns
        for i in range(1, self.num_columns):
            self.canvas.create_line(
                self.board_coords[0] + i * col_width,
                self.board_coords[1],
                self.board_coords[0] + i * col_width,
                self.board_coords[3],
                fill='black')

        # Draw rows
        row_width = (self.board_coords[3] - self.board_coords[1]) / self.num_rows
        for i in range(1, self.num_rows):
            self.canvas.create_line(
                self.board_coords[0],
                self.board_coords[1] + i * row_width,
                self.board_coords[2],
                self.board_coords[1] + i * row_width,
                fill='black')

        self.canvas.pack()
        self.master.bind("<Button-1>", self.clicked)

    def clicked(self, event):
        if (event.x >= self.board_coords[0] and event.x <= self.board_coords[2] and
            event.y >= self.board_coords[1] and event.y <= self.board_coords[3]):
            x = event.x - self.board_coords[0]
            col_width = (self.board_coords[2] - self.board_coords[0]) / self.num_columns
            col_index = int(x / col_width)

            y = event.y - self.board_coords[1]
            row_width = (self.board_coords[3] - self.board_coords[1]) / self.num_rows
            row_index = int(y / row_width)
            self.user_clicked_func(col_index, row_index)

    def mark_square(self, col_index, row_index, player):
        if row_index >= self.num_rows:
            raise IndexError(
                'row_index is out of range. row_index is {}. '
                'Available row indexes are 0 to {}.'.format(
                    row_index, self.num_rows - 1))
        elif col_index >= self.num_columns:
            raise IndexError(
                'col_index is out of range. col_index is {}. '
                'Available column indexes are 0 to {}.'.format(
                    col_index, self.num_columns - 1))

        col_width = (self.board_coords[2] - self.board_coords[0]) / self.num_columns
        row_width = (self.board_coords[3] - self.board_coords[1]) / self.num_rows

        coords = (self.board_coords[0] + col_index * col_width,
            self.board_coords[1] + row_index * row_width,
            self.board_coords[0] + (col_index + 1) * col_width, 
            self.board_coords[1] + (row_index + 1) * row_width)

        if player in ('o', 'O', '0'):
            self.canvas.create_oval(
                coords[0], coords[1], coords[2], coords[3], fill='white')
        elif player in ('x', 'X'):
            self.canvas.create_line(
                coords[0], coords[1], coords[2], coords[3], fill='black')
            self.canvas.create_line(
                coords[0] + col_width, coords[1], coords[2] - col_width, coords[3], fill='black')

        self.master.update()

    def display_message(self, string):
        '''
        Displays a message on the board.
        '''
        self.canvas.itemconfig(self.message, text=string)
