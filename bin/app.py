"""
this is an environment where I can test a number of different modular GUIs

in this example,
I want to have a single counter that when I click on it, it updates some text, and saves info to a json file

"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QWidget

import calc.chance as ch
import ui.generate_ui as gen_ui


class ShinyGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.fish_counter = 0  # in the future - have this load from a json file
        self.fish_chance = 0
        self.RE_counter = 0
        self.RE_chance = 0
        self.initUI()

    def initUI(self):
        """ initialise the UI with the properties below"""
        # self.setGeometry(400, 400, 600, 400)
        self.setWindowTitle('Shiny Pokemon Simulator')
        self.setWindowIcon(QIcon('res/pokeball_favicon.png'))

        # self.fish_init()
        # self.RE_init()

        # the layouts and functions are generated in another file, call them here
        self.fish_ui = gen_ui.CumGrid('fish')
        self.RE_ui = gen_ui.CumGrid('RE')

        """ GRIDS """
        # lets play with some layouts!
        # ok, so lets see if this works. have a main hbox with grids in each segment

        #  |'''''|'''''|
        #  |     |     |
        #  |-----|-----|
        #  |     |     |
        #  |.....|.....|
        #
        # sort of ike this

        # how would I implement?
        # create hbox
        # self.addLayout(hbox)
        # hbox.addLayout(grid_1, 2 ....)

        hbox = QHBoxLayout()
        hbox.addStretch(1)


        fish_grid = QGridLayout()
        fish_grid.setSpacing(10)  # sets margins between elements

        RE_grid = QGridLayout()
        RE_grid.setSpacing(10)

        hbox.addLayout(fish_grid)
        hbox.addLayout(RE_grid)

        # CHAIN FISHING
        fish_grid.addWidget(self.fish_ui.title, 0, 0)
        fish_grid.addWidget(self.fish_ui.counter_label, 1, 0)
        fish_grid.addWidget(self.fish_ui.counter_text, 1, 1)
        fish_grid.addWidget(self.fish_ui.inc_btn, 1, 2)
        fish_grid.addWidget(self.fish_ui.chance_lb, 2, 1)
        fish_grid.addWidget(self.fish_ui.cum_chance_text, 2, 2)

        # RANDOM ENCOUNTERS

        RE_grid.addWidget(self.RE_ui.title, 0, 0)
        RE_grid.addWidget(self.RE_ui.counter_label, 1, 0)
        RE_grid.addWidget(self.RE_ui.counter_text, 1, 1)
        RE_grid.addWidget(self.RE_ui.inc_btn, 1, 2)
        RE_grid.addWidget(self.RE_ui.chance_lb, 2, 1)
        RE_grid.addWidget(self.RE_ui.cum_chance_text, 2, 2)

        self.RE_ui.update_chance()
        self.fish_ui.update_chance()

        self.setLayout(hbox)
        self.show()


def run():
    app = QApplication(sys.argv)
    return app
