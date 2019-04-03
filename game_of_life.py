#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" module dosctring """

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget,
                             QGridLayout, QPushButton, QLabel, QLineEdit,      
                             QInputDialog)

class Board(QWidget):
    """ class docstring """

    def __init__(self):
        super().__init__()
        self.board_height = 0
        self.board_width = 0
        self.init_ui()

    def init_ui(self):
        """ init_ui dosctring """
        self.set_height_dialog()
        self.set_width_dialog()

        grid = QGridLayout()
        grid.setHorizontalSpacing(0)
        grid.setVerticalSpacing(0)
        for i in range(self.board_height):
            for j in range(self.board_width):
                t_b = QPushButton("")
                t_b.setCheckable(True)
                t_b.setMaximumWidth(16)
                t_b.setMaximumHeight(9)
                t_b.setFlat(True)
                grid.addWidget(t_b, i, j)

        #build out board via grid layout
        #resize will need work once I figure out WTF I'm doing
        self.setLayout(grid)
        #self.resize(self.board_width * 3, self.board_height * 3)
        self.center()
        self.setWindowTitle('Conways Game of Life')
        self.show()

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

    def set_height(self, height):
        """ sets board height """
        self.board_height = height
    def set_width(self, width):
        """ sets board width """
        self.board_width = width
    def get_height(self):
        """ returns board height """
        return self.board_height
    def get_width(self):
        """ returns board width """
        return self.board_width
    def to_string(self):
        """ prints board class toString """
        print("Height: {0} Width: {1}".format(self.board_height, self.board_width))

if __name__ == '__main__':

    #build user input interface here
    APP = QApplication(sys.argv)
    BOARD = Board()
    sys.exit(APP.exec_())
