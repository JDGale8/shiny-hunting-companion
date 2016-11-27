"""
this is an environment where I can test a number of different modular GUIs

in this example,
I want to have a single counter that when I click on it, it updates some text, and saves info to a json file

"""
import sys
from PyQt5.QtGui import QIcon
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

        self.counter = 0  # in the future - have this load from a json file
        self.chance = 0
        self.initUI()

    def initUI(self):
        """ initialise the UI with the properties below"""
        self.setGeometry(400, 400, 600, 400)
        self.setWindowTitle('Shiny Pokemon Simulator')
        self.setWindowIcon(QIcon('../res/pokeball_favicon.png'))

        self.counter_disp = QTextEdit(str(self.counter))
        self.counter_label = QLabel("counter")
        self.chance_lb = QLabel("Chance to have found a shiny by now:")
        self.chance_amount = QTextEdit("{:.2f}".format(self.chance))
        self.chance_amount.setReadOnly(True)

        self.inc_btn = QPushButton("+")
        self.inc_btn.clicked.connect(self.increase_counter)

        grid = QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(self.counter_label, 0, 0)
        grid.addWidget(self.counter_disp, 0,1)
        grid.addWidget(self.inc_btn, 0,2)
        grid.addWidget(self.chance_lb, 1,1)
        grid.addWidget(self.chance_amount, 1,2)

        self.setLayout(grid)
        self.show()

    def increase_counter(self):
        self.counter += 1
        self.counter_disp.setText(str(self.counter))

        chance = ch.fishing(self.counter)
        self.chance_amount.setText("{:.2f}%".format(chance*100))
        # should also then save this counter value to a json file
        #QApplication.processEvents()  # update gui for pyqt

if __name__ == '__main__':
    app = QApplication(sys.argv)

    instance = TestGUI()
    sys.exit(app.exec_())
