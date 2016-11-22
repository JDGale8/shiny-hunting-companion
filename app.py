import sys
from PyQt5 import Qt

from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class ShinyGui(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        """ initialise the UI with the properties below"""
        w_width = 800
        w_height = 1000

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setGeometry(400, 400, w_height, w_width)
        self.setWindowTitle('Shiny Pokemon Simulator')
        self.setWindowIcon(QIcon('res/pokeball_favicon.png'))

        btn = QPushButton('Button', self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.setToolTip('This is a <b>button</b>')

        quit_button = QPushButton('Quit', self)

        quit_button.clicked.connect(QCoreApplication.instance().quit)
        quit_button.move(50, 100)

        # change background colour, requires a pallete object
        p = self.palette()
        p.setColor(self.backgroundRole, Qt.red)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    instance = ShinyGui()
    sys.exit(app.exec_())
