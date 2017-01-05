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
from PyQt5.QtWidgets import QRadioButton
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

        Tabs = QTabWidget()

        main_layout = QVBoxLayout()
        main_layout.addWidget(Tabs)
        self.setLayout(main_layout)

        cum_tab = self.generate_cumulative_tab()
        sim_tab = self.generate_simulation_tab()

        Tabs.addTab(cum_tab, "Cumulative Chances")
        Tabs.addTab(sim_tab, "Simulations")

        self.update()

        self.show()

    def generate_cumulative_tab(self):

        cum_tab = QWidget()
        vbox = QVBoxLayout(cum_tab)

        checkbox_hbox = QHBoxLayout()

        # CHECKBOXES #

        shiny_charm_chk = QCheckBox("Shiny Charm", self)
        masuda_meth_chk = QCheckBox("Masuda Method", self)
        checkbox_hbox.addWidget(shiny_charm_chk)
        checkbox_hbox.addWidget(masuda_meth_chk)

        shiny_charm_chk.stateChanged.connect(self.update_shiny_charm)
        masuda_meth_chk.stateChanged.connect(self.update_masuda)

        calculation_hbox_1 = QHBoxLayout()  # contains RE and fish
        calculation_hbox_2 = QHBoxLayout()  # contains egg and horde
        calculation_hbox_3 = QHBoxLayout()  # contains SOS and DexNav

        # CUMULATIVE GRIDS #
        self.fish_cum_grid = gen_ui.CumGrid('fish')
        self.RE_cum_grid = gen_ui.CumGrid('RE')
        self.horde_cum_grid = gen_ui.CumGrid('horde')
        self.egg_cum_grid = gen_ui.CumGrid('egg')
        self.SOS_grid = gen_ui.CumGrid('SOS')
        self.dex_grid = gen_ui.CumGrid('dex')

        calculation_hbox_1.addLayout(self.fish_cum_grid.grid)
        calculation_hbox_1.addLayout(self.RE_cum_grid.grid)
        calculation_hbox_2.addLayout(self.horde_cum_grid.grid)
        calculation_hbox_2.addLayout(self.egg_cum_grid.grid)
        calculation_hbox_3.addLayout(self.SOS_grid.grid)
        calculation_hbox_3.addLayout(self.dex_grid.grid)

        vbox.addLayout(checkbox_hbox)
        vbox.addLayout(calculation_hbox_1)
        vbox.addLayout(calculation_hbox_2)
        vbox.addLayout(calculation_hbox_3)

        return cum_tab

    def generate_simulation_tab(self):

        checkbox_hbox = QHBoxLayout()

        # CHECKBOXES #

        shiny_charm_chk = QCheckBox("Shiny Charm", self)
        masuda_meth_chk = QCheckBox("Masuda Method", self)
        checkbox_hbox.addWidget(shiny_charm_chk)
        checkbox_hbox.addWidget(masuda_meth_chk)

        shiny_charm_chk.stateChanged.connect(self.update_shiny_charm)
        masuda_meth_chk.stateChanged.connect(self.update_masuda)

        # RADIO BUTTONS #

        fish_radio = QRadioButton("Chain Fishing", self)
        RE_radio = QRadioButton("Rand. Ecounters", self)
        horde_radio = QRadioButton("Horde", self)
        egg_radio = QRadioButton("Eggs", self)
        SOS_radio = QRadioButton("SOS", self)
        dex_radio = QRadioButton("DexNav", self)

        sim_tab = QWidget()
        vbox = QVBoxLayout(sim_tab)

        radio_hbox = QHBoxLayout()
        radio_hbox.addWidget(fish_radio)
        radio_hbox.addWidget(RE_radio)
        radio_hbox.addWidget(horde_radio)
        radio_hbox.addWidget(egg_radio)
        radio_hbox.addWidget(SOS_radio)
        radio_hbox.addWidget(dex_radio)

        vbox.addLayout(checkbox_hbox)
        vbox.addLayout(radio_hbox)

        return sim_tab




    def update_shiny_charm(self, sc_chk):

        if sc_chk == Qt.Checked:
            self.RE_cum_grid.sc = True
            self.fish_cum_grid.sc = True
            self.horde_cum_grid.sc = True
            self.egg_cum_grid.sc = True
        else:
            self.RE_cum_grid.sc = False
            self.fish_cum_grid.sc = False
            self.horde_cum_grid.sc = False
            self.egg_cum_grid.sc = False

        self.update()

    def update_masuda(self, mm_chk):
        if mm_chk == Qt.Checked:
            self.egg_cum_grid.mm = True
        else:
            self.egg_cum_grid.mm = False

        self.update()

    def update(self):

        self.RE_cum_grid.update_chance()
        self.fish_cum_grid.update_chance()
        self.horde_cum_grid.update_chance()
        self.egg_cum_grid.update_chance()


def run():
    app = QApplication(sys.argv)
    return app
