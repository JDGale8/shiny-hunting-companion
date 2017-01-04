"""
this is an environment where I can test a number of different modular GUIs

in this example,
I want to have a single counter that when I click on it, it updates some text, and saves info to a json file

"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QWidget
import bin.chance as ch


class TestGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.fish_counter = 0  # in the future - have this load from a json file
        self.fish_chance = 0
        self.RE_counter = 0
        self.RE_chance = 0
        self.initUI()

    def initUI(self):
        """ initialise the UI with the properties below"""
        self.setGeometry(400, 400, 600, 400)
        self.setWindowTitle('Shiny Pokemon Simulator')
        self.setWindowIcon(QIcon('../res/pokeball_favicon.png'))

        self.fish_init()
        self.RE_init()

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
        fish_grid.setSpacing(10) # sets margins between elements

        RE_grid = QGridLayout()
        RE_grid.setSpacing(10)

        hbox.addLayout(fish_grid)
        hbox.addLayout(RE_grid)

        # CHAIN FISHING
        fish_grid.addWidget(self.fish_title, 0, 0)
        fish_grid.addWidget(self.fish_counter_label, 1, 0)
        fish_grid.addWidget(self.fish_counter_disp, 1, 1)
        fish_grid.addWidget(self.fish_inc_btn, 1, 2)
        fish_grid.addWidget(self.fish_chance_lb, 2, 1)
        fish_grid.addWidget(self.fish_chance_amount, 2, 2)

        # RANDOM ENCOUNTERS

        RE_grid.addWidget(self.RE_title, 0, 0)
        RE_grid.addWidget(self.RE_counter_label, 1, 0)
        RE_grid.addWidget(self.RE_counter_disp, 1, 1)
        RE_grid.addWidget(self.RE_inc_btn, 1, 2)
        RE_grid.addWidget(self.RE_chance_lb, 2, 1)
        RE_grid.addWidget(self.RE_chance_amount, 2, 2)

        self.fish_update_chance()
        self.RE_update_chance()

        self.setLayout(hbox)
        self.show()

    """ INITIALIZE ATTRIBUTES """

    def fish_init(self):

        """ FISHING PROBABLITIES """
        # set display for chain counter
        self.fish_counter_disp = QTextEdit(str(self.fish_counter))
        self.fish_counter_disp.textChanged.connect(self.fish_set_chain)  # if it changes, change chain too

        # set titles and info for chain fishing
        self.fish_title = QLabel("Chain Fishing")
        self.fish_counter_label = QLabel("counter")
        self.fish_chance_lb = QLabel("Chance to have found a shiny by now:")
        self.fish_chance_amount = QTextEdit("{:.2f}".format(self.fish_chance))
        self.fish_chance_amount.setReadOnly(True)

        self.fish_inc_btn = QPushButton("+")
        self.fish_inc_btn.clicked.connect(self.fish_increase_counter)

    def RE_init(self):
        """ RANDOM ENCOUNTER PROBABLITIES """
        # set display for chain counter
        self.RE_counter_disp = QTextEdit(str(self.RE_counter))
        self.RE_counter_disp.textChanged.connect(self.RE_set_chain)  # if it changes, change chain too

        # set titles and info for random encounters
        self.RE_title = QLabel("Random Encounters")
        self.RE_counter_label = QLabel("Counter")
        self.RE_chance_lb = QLabel("Chance for at least one shiny:")
        self.RE_chance_amount = QTextEdit("{:.2f}".format(self.RE_chance))

        self.RE_inc_btn = QPushButton("+")
        self.RE_inc_btn.clicked.connect(self.RE_increase_counter)

    # FISHING #

    def fish_increase_counter(self):
        self.fish_counter += 1
        self.fish_counter_disp.setText(str(self.fish_counter))
        self.fish_update_chance()

        # should also then save this counter value to a json file

    def fish_update_chance(self):

        chance = ch.fishing(self.fish_counter)
        self.fish_chance_amount.setText("{:.2f}%".format(chance * 100))

    def fish_set_chain(self):
        entry = self.fish_counter_disp.toPlainText()
        try:
            entry = int(entry)
        except ValueError:
            entry = 0

        self.fish_counter = entry
        self.fish_update_chance()

    # RANDOM ENCOUNTER #

    def RE_set_chain(self):
        entry = self.RE_counter_disp.toPlainText()
        try:
            entry = int(entry)
        except ValueError:
            entry = 0

        self.RE_counter = entry
        self.RE_update_chance()

    def RE_increase_counter(self):
        self.RE_counter += 1
        self.fish_counter_disp.setText(str(self.RE_counter))
        self.RE_update_chance()

        # should also then save this counter value to a json file

    def RE_update_chance(self):

        chance = ch.random_encounter(self.RE_counter)
        self.RE_chance_amount.setText("{:.2f}%".format(chance * 100))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    instance = TestGUI()
    sys.exit(app.exec_())
