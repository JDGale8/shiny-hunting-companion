"""
this is an environment where I can test a number of different modular GUIs

in this example,
I want to have a single counter that when I click on it, it updates some text, and saves info to a json file

"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QCheckBox

import ui.generate_ui as gen_ui


class ShinyGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """ initialise the UI with the properties below"""
        self.setGeometry(400, 400, 500, 300)
        self.setWindowTitle('Shiny Pokemon Simulator')
        self.setWindowIcon(QIcon('res/pokeball_favicon.png'))

        # lets try creating a tab

        QTab = QTabWidget()



        # set layouts
        # main layout will be vertical, with sub horizontal layouts within




        main_layout = QVBoxLayout()
        main_layout.addWidget(QTab)
        self.setLayout(main_layout)

        cum_tab = self.generate_cumulative_tab()
        QTab.addTab(cum_tab, "Cumulative Chances")

        self.update()

        self.show()

    def generate_cumulative_tab(self):

        cum_tab = QWidget()
        vbox = QVBoxLayout(cum_tab)

        checkbox_hbox = QHBoxLayout()

        # CHECKBOXES #

        shiny_charm_chk = QCheckBox("Shiny Charm", self)
        masuda_chk = QCheckBox("Masuda Method", self)
        shiny_charm_chk.stateChanged.connect(self.update_shiny_charm)
        masuda_chk.stateChanged.connect(self.update_masuda)
        checkbox_hbox.addWidget(shiny_charm_chk)
        checkbox_hbox.addWidget(masuda_chk)

        calculation_hbox_1 = QHBoxLayout()  # contains RE and fish
        calculation_hbox_2 = QHBoxLayout()  # contains egg and horde
        calculation_hbox_3 = QHBoxLayout()  # contains SOS and DexNav

        # CUMULATIVE GRIDS #
        self.fish_grid = gen_ui.CumGrid('fish')
        self.RE_grid = gen_ui.CumGrid('RE')
        self.horde_grid = gen_ui.CumGrid('horde')
        self.egg_grid = gen_ui.CumGrid('egg')
        self.SOS_grid = gen_ui.CumGrid('SOS')
        self.dex_grid = gen_ui.CumGrid('dex')

        calculation_hbox_1.addLayout(self.fish_grid.grid)
        calculation_hbox_1.addLayout(self.RE_grid.grid)
        calculation_hbox_2.addLayout(self.horde_grid.grid)
        calculation_hbox_2.addLayout(self.egg_grid.grid)
        calculation_hbox_3.addLayout(self.SOS_grid.grid)
        calculation_hbox_3.addLayout(self.dex_grid.grid)

        vbox.addLayout(checkbox_hbox)
        vbox.addLayout(calculation_hbox_1)
        vbox.addLayout(calculation_hbox_2)
        vbox.addLayout(calculation_hbox_3)

        return cum_tab

    def update_shiny_charm(self, sc_chk):

        if sc_chk == Qt.Checked:
            self.RE_grid.sc = True
            self.fish_grid.sc = True
            self.horde_grid.sc = True
            self.egg_grid.sc = True
        else:
            self.RE_grid.sc = False
            self.fish_grid.sc = False
            self.horde_grid.sc = False
            self.egg_grid.sc = False

        self.update()

    def update_masuda(self, mm_chk):
        if mm_chk == Qt.Checked:
            self.egg_grid.mm = True
        else:
            self.egg_grid.mm = False

        self.update()


    def update(self):

        self.RE_grid.update_chance()
        self.fish_grid.update_chance()
        self.horde_grid.update_chance()
        self.egg_grid.update_chance()

def run():
    app = QApplication(sys.argv)
    return app
