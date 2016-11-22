import sys

from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMainWindow)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QRect


class Button(QPushButton):

    def __init__(self, parent, text='button'):
        super(Button, self).__init__(parent)

        self.setAcceptDrops(True)
        self.setGeometry(QRect(90, 90, 61, 51))
        self.setText(text)


class ShinyGui(QMainWindow):
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


        ### creates a menu bar at the top of the window with an option to quit on it
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        ###

        ### show's a status bar at the bottom of the screen
        self.statusBar().showMessage('Ready')

        btn = QPushButton('Button', self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.setToolTip('This is a <b>button</b>')

        quit_button = Button(self, 'Quit')
        quit_button.clicked.connect(QCoreApplication.instance().quit)


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
