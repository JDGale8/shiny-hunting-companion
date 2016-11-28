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
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QWidget
import chance as ch


class TestGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.fishing_counter = 0  # in the future - have this load from a json file
        self.chance = 0
        self.initUI()

    def initUI(self):
        """ initialise the UI with the properties below"""
        self.setGeometry(400, 400, 600, 400)
        self.setWindowTitle('Shiny Pokemon Simulator')
        self.setWindowIcon(QIcon('../res/pokeball_favicon.png'))

        """ FISHING PROBABLITIES """
        # set display for chain counter
        self.counter_disp = QTextEdit(str(self.fishing_counter))
        self.counter_disp.textChanged.connect(self.set_chain)  # if it changes, change chain too

        # set titles and info
        self.fishing_title = QLabel("Chain Fishing")
        self.counter_label = QLabel("counter")
        self.chance_lb = QLabel("Chance to have found a shiny by now:")
        self.chance_amount = QTextEdit("{:.2f}".format(self.chance))
        self.chance_amount.setReadOnly(True)

        self.inc_btn = QPushButton("+")
        self.inc_btn.clicked.connect(self.increase_fishing_counter)

        grid = QGridLayout()
        grid.setSpacing(5)

        # grid information for chain fishing widget
        grid.addWidget(self.fishing_title, 0, 0)
        grid.addWidget(self.counter_label, 1, 0)
        grid.addWidget(self.counter_disp, 1, 1)
        grid.addWidget(self.inc_btn, 1, 2)
        grid.addWidget(self.chance_lb, 2, 1)
        grid.addWidget(self.chance_amount, 2, 2)

        self.update_chance()

        self.setLayout(grid)
        self.show()

    def increase_fishing_counter(self):
        self.fishing_counter += 1
        self.counter_disp.setText(str(self.fishing_counter))
        self.update_chance()

        # should also then save this counter value to a json file

    def update_chance(self):

        chance = ch.fishing(self.fishing_counter)
        self.chance_amount.setText("{:.2f}%".format(chance * 100))

        #QApplication.processEvents()  # update gui for pyqt

    def set_chain(self):
        entry = self.counter_disp.toPlainText()
        try:
            entry = int(entry)
        except ValueError:
            entry = 0

        self.fishing_counter = entry
        self.update_chance()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    instance = TestGUI()
    sys.exit(app.exec_())
