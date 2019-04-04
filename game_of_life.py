#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
module sdocstring goes here
"""

import random
import sys
import time
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget,
                             QGridLayout, QPushButton, QLabel, QLineEdit,
                             QInputDialog)

class Board(QWidget):
    """ class docstring """

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """ init_ui dosctring """
        self.board_height = 0
        self.board_width = 0
        self.set_height_dialog()
        self.set_width_dialog()
        self.setGeometry(0, 0, self.board_width * 10, self.board_height * 10)
        self.center()
        self.setWindowTitle('Conways Game of Life')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        board = self.random_state(self.board_height, self.board_width)
        self.draw_board(qp, board)
        qp.end()


    def draw_board(self, qp, board):
        black = QColor(255, 255, 255)
        white = QColor(0,0,0)
        offset = 10
        height_offset = 0
        


    def random_state(self, height: int, width: int):
        """
        Function takes in 2 args (height and width) and returns a board_state (list) in
        which every cell has been randomly initalized to either alive (1) or dead (0).
        These boards are known as 'soups'
        """
        random_board = []
        for _ in range(height):
            sub = []
            for _ in range(width):
                sub.append(random.randint(0,1))
            random_board.append(sub)
        return random_board

    def dead_state(self, height: int, width: int):
        #same as random_state only initializes to completely dead
        dead_board = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(0)
            dead_board.append(row)
        return dead_board

    def next_board_state(self, board: list):
        #determine width/height of board to set up nexted loop
        next_board_height = len(board)
        next_board_width = len(board[0])
        #generate a dead_state board to build new state from
        next_board = self.dead_state(next_board_height, next_board_width)
        #build nested loop to analyze board
        for i in range(next_board_height):
            for j in range(next_board_width):
                neighbors = self.walk_and_tally(board, next_board_height, next_board_width, i, j)
                if(board[i][j] == 1): #alive
                    if(neighbors >= 2 and neighbors < 4):
                        next_board[i][j] = 1
                else: #dead
                    if(neighbors == 3):
                        next_board[i][j] = 1
        return next_board

    def walk_and_tally(self, board: list, h: int, w: int, i: int, j: int):
        #check for corner
        neighbors = 0
        tlcorner = (i == 0 and j == 0)
        if(tlcorner):
            #up/left (wrap)
            if(board[h - 1][w - 1] == 1):
                neighbors += 1
            #up (wrap)
            if(board[h - 1][j] == 1):
                neighbors += 1
            #up/right (wrap)
            if(board[h - 1][j + 1] == 1):
                neighbors += 1
            #right
            if(board[i][j + 1] == 1):
                neighbors += 1
            #right/down
            if(board[i + 1][j + 1] == 1):
                neighbors += 1
            #down
            if(board[i + 1][j] == 1):
                neighbors += 1
            #down/left (wrap)
            if(board[i + 1][w - 1] == 1):
                neighbors += 1
            #left (wrap)
            if(board[i][w - 1] == 1):
                neighbors += 1
            return neighbors

        trcorner = (i == 0 and j == w - 1)
        if(trcorner):
            #up/left (wrap)
            if(board[h - 1][j - 1] == 1):
                neighbors += 1
            #up (wrap)
            if(board[h - 1][j] == 1):
                neighbors += 1
            #up/right (wrap)
            if(board[h - 1][0] == 1):
                neighbors += 1
            #right (wrap)
            if(board[i][0] == 1):
                neighbors += 1
            #down/right (wrap)
            if(board[i + 1][0] == 1):
                neighbors += 1
            #down
            if(board[i + 1][j] == 1):
                neighbors += 1
            #down/left
            if(board[i + 1][j - 1] == 1):
                neighbors += 1
            #left
            if(board[i][j - 1] == 1):
                neighbors += 1
            return neighbors

        blcorner = (i == h - 1 and j == 0)
        if(blcorner):
            #up/left (wrap)
            if(board[i - 1][w - 1] == 1):
                neighbors += 1
            #up
            if(board[i - 1][j] == 1):
                neighbors += 1
            #up/right
            if(board[i - 1][j + 1] == 1):
                neighbors += 1
            #right
            if(board[i][j + 1] == 1):
                neighbors += 1
            #down/right (wrap)
            if(board[0][j + 1] == 1):
                neighbors += 1
            #down (wrap)
            if(board[0][j] == 1):
                neighbors += 1
            #down/left (wrap)
            if(board[0][w - 1] == 1):
                neighbors += 1
            #left (wrap)
            if(board[i][w - 1] == 1):
                neighbors += 1
            return neighbors

        brcorner = (i == h - 1 and j == w - 1)
        if(brcorner):
            #up/left
            if(board[i - 1][j - 1] == 1):
                neighbors += 1
            #up
            if(board[i - 1][j] == 1):
                neighbors += 1
            #up/right (wrap)
            if(board[i - 1][0] == 1):
                neighbors += 1
            #right (wrap)
            if(board[i][0] == 1):
                neighbors += 1
            #down/right (wrap)
            if(board[0][0] == 1):
                neighbors += 1
            #down (wrap)
            if(board[0][j] == 1):
                neighbors += 1
            #down/left (wrap)
            if(board[0][j - 1] == 1):
                neighbors += 1
            #left
            if(board[i][j - 1] == 1):
                neighbors += 1
            return neighbors

        #check for edge
        tedge = (i == 0)
        if(tedge):
            #up/left (wrap)
            if(board[h - 1][j - 1] == 1):
                neighbors += 1
            #up (wrap)
            if(board[h - 1][j] == 1):
                neighbors += 1
            #up/right (wrap)
            if(board[h - 1][j + 1] == 1):
                neighbors += 1
            #right
            if(board[i][j + 1] == 1):
                neighbors += 1
            #down/right
            if(board[i + 1][j + 1] == 1):
                neighbors += 1
            #down
            if(board[i + 1][j] == 1):
                neighbors += 1
            #down/left
            if(board[i + 1][j - 1] == 1):
                neighbors += 1
            #left
            if(board[i][j - 1] == 1):
                neighbors += 1
            return neighbors
            
        redge = (j == w - 1)
        if(redge):
            #up/left
            if(board[i - 1][j - 1] == 1):
                neighbors += 1
            #up
            if(board[i - 1][j] == 1):
                neighbors += 1
            #up/right (wrap)
            if(board[i - 1][0] == 1):
                neighbors += 1
            #right (wrap)
            if(board[i][0] == 1):
                neighbors += 1
            #down/right (wrap)
            if(board[i + 1][0] == 1):
                neighbors += 1
            #down
            if(board[i + 1][j] == 1):
                neighbors += 1
            #down/left
            if(board[i + 1][j - 1] == 1):
                neighbors += 1
            #left
            if(board[i][j -1] == 1):
                neighbors += 1
            return neighbors

        bedge = (i == h - 1)
        if(bedge):
            #up/left
            if(board[i - 1][j - 1] == 1):
                neighbors += 1
            #up
            if(board[i - 1][j] == 1):
                neighbors += 1
            #up/right
            if(board[i - 1][j + 1] == 1):
                neighbors += 1
            #right
            if(board[i][j + 1] == 1):
                neighbors += 1
            #down/right (wrap)
            if(board[0][j + 1] == 1):
                neighbors += 1
            #down (wrap)
            if(board[0][j] == 1):
                neighbors += 1
            #down/left (wrap)
            if(board[0][j - 1] == 1):
                neighbors += 1
            #left
            if(board[i][j - 1] == 1):
                neighbors += 1
            return neighbors

        ledge = (j == 0)
        if(ledge):
            #up/left (wrap)
            if(board[i - 1][w - 1] == 1):
                neighbors += 1
            #up
            if(board[i - 1][j] == 1):
                neighbors += 1
            #up/right
            if(board[i - 1][j + 1] == 1):
                neighbors += 1
            #right
            if(board[i][j + 1] == 1):
                neighbors += 1
            #down/right
            if(board[i + 1][j + 1] == 1):
                neighbors += 1
            #down
            if(board[i + 1][j] == 1):
                neighbors += 1
            #down/left (wrap)
            if(board[i + 1][w - 1] == 1):
                neighbors += 1
            #left (wrap)
            if(board[i][w - 1] == 1):
                neighbors += 1
            return neighbors

        #handle central
        #up/left
        if(board[i - 1][j - 1] == 1):
            neighbors += 1
        #up
        if(board[i - 1][j] == 1):
            neighbors += 1
        #up/right
        if(board[i - 1][j + 1] == 1):
            neighbors += 1
        #right
        if(board[i][j + 1] == 1):
            neighbors += 1
        #down/right
        if(board[i + 1][j + 1] == 1):
            neighbors += 1
        #down
        if(board[i + 1][j] == 1):
            neighbors += 1
        #down/left
        if(board[i + 1][j - 1] == 1):
            neighbors += 1
        #left
        if(board[i][j - 1] == 1):
            neighbors += 1
        return neighbors

    def pretty_print(board: list):
        """ docstring """
        def print_horiz_border(board_width: int):
            for _ in range(board_width + 2):
                print('-', end='')
            print()

        board_height = len(board)
        board_width = len(board[0])
        #print top of board
        print_horiz_border(board_width)
        #print interior rows of board
        for i in range(board_height):
            print('|', end='')
            for j in range(board_width):
                if board[i][j] == 1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print('|')
        #print bottom of board
        print_horiz_border(board_width)

    def center(self):
        """ docstring """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def set_height_dialog(self):
        text, ok = QInputDialog.getText(self, "Board Height", "Enter board height:")
        if ok:
            self.set_height(int(text))

    def set_width_dialog(self):
        text, ok = QInputDialog.getText(self, "Board Width", "Enter board width:")
        if ok:
            self.set_width(int(text))

    #setters
    def set_height(self, height):
        """ sets board height """
        self.board_height = height

    def set_width(self, width):
        """ sets board width """
        self.board_width = width

    #getters
    def get_height(self):
        """ returns board height """
        return self.board_height

    def get_width(self):
        """ returns board width """
        return self.board_width

    def get_grid(self):
        """ returns grid """
        return self.grid

    def to_string(self):
        """ prints board class toString """
        print("Height: {0} Width: {1}".format(self.board_height, self.board_width))

if __name__ == '__main__':

    #build user input interface here
    APP = QApplication(sys.argv)
    BOARD = Board()
    sys.exit(APP.exec_())
