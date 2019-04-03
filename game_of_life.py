#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" module dosctring """

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Board(QWidget):
    """ class docstring """

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        """ init_ui dosctring """
        #Height text Height textbox
        #Width text Width textbox
        #OK button

        self.setGeometry(300, 300, 280, 150)
        self.setWindowTitle('Board Dimensions')
        self.show()

if __name__ == '__main__':

    #build user input interface here
    APP = QApplication(sys.argv)
    BOARD = Board()
    sys.exit(APP.exec_())
