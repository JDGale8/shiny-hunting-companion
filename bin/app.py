import sys

from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QHBoxLayout, QVBoxLayout,
                             QApplication, QMainWindow)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QRect


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
        self.setWindowIcon(QIcon('../res/pokeball_favicon.png'))

        quit_button =QPushButton('Quit')
        ok_button = QPushButton('Ok')
        quit_button.clicked.connect(QCoreApplication.instance().quit)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(quit_button)
        hbox.addWidget(ok_button)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)


        self.show()

    def closeEvent(self, event):
        """ automatically called when the window is closed, overrides the normal functoinality"""

        reply = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    instance = ShinyGui()
    sys.exit(app.exec_())
