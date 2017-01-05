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
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QCheckBox

import ui.generate_ui as gen_ui
import calc.shiny_sim as sim

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
        self.SOS_cum_grid = gen_ui.CumGrid('SOS')
        self.dex_cum_grid = gen_ui.CumGrid('dex')

        calculation_hbox_1.addLayout(self.fish_cum_grid.grid)
        calculation_hbox_1.addLayout(self.RE_cum_grid.grid)
        calculation_hbox_2.addLayout(self.horde_cum_grid.grid)
        calculation_hbox_2.addLayout(self.egg_cum_grid.grid)
        calculation_hbox_3.addLayout(self.SOS_cum_grid.grid)
        calculation_hbox_3.addLayout(self.dex_cum_grid.grid)

        vbox.addLayout(checkbox_hbox)
        vbox.addLayout(calculation_hbox_1)
        vbox.addLayout(calculation_hbox_2)
        vbox.addLayout(calculation_hbox_3)

        return cum_tab

    def generate_simulation_tab(self):

        checkbox_hbox = QHBoxLayout()

        # CHECKBOXES #

        self.shiny_charm_chk = QCheckBox("Shiny Charm", self)
        self.masuda_meth_chk = QCheckBox("Masuda Method", self)
        checkbox_hbox.addWidget(self.shiny_charm_chk)
        checkbox_hbox.addWidget(self.masuda_meth_chk)

        self.shiny_charm_chk.stateChanged.connect(self.update_shiny_charm)
        self.masuda_meth_chk.stateChanged.connect(self.update_masuda)

        # RADIO BUTTONS #

        self.fish_radio = QRadioButton("Chain Fishing", self)
        self.RE_radio = QRadioButton("Rand. Ecounters", self)
        self.horde_radio = QRadioButton("Horde", self)
        self.egg_radio = QRadioButton("Eggs", self)
        self.SOS_radio = QRadioButton("SOS", self)
        self.dex_radio = QRadioButton("DexNav", self)

        sim_tab = QWidget()
        vbox = QVBoxLayout(sim_tab)

        radio_hbox = QHBoxLayout()
        radio_hbox.addWidget(self.fish_radio)
        radio_hbox.addWidget(self.RE_radio)
        radio_hbox.addWidget(self.horde_radio)
        radio_hbox.addWidget(self.egg_radio)
        radio_hbox.addWidget(self.SOS_radio)
        radio_hbox.addWidget(self.dex_radio)

        vbox.addLayout(checkbox_hbox)
        vbox.addLayout(radio_hbox)

        self.counter = 0  # in the future - have this load from a json file

        # quick simulation buttons - maybe?

        self.counter_text = QLineEdit(str(self.counter))
        self.counter_text.setAlignment(Qt.AlignRight)
        self.counter_text.setMaximumWidth(40)
        self.counter_text.textChanged.connect(self.set_chain)  # deals with non integer entries

        self.simulation_results = QLabel("Press \'Run\' to run a simulation...")
        self.simulation_results.wordWrap()
        self.simulation_results.setAlignment(Qt.AlignTop)
        self.run_btn = QPushButton("Run")
        self.run_btn.setMaximumWidth(50)
        self.run_btn.clicked.connect(self.run_simulation)

        controls_hbox = QHBoxLayout()
        controls_hbox.addStretch(1)
        controls_hbox.addWidget(self.counter_text)
        controls_hbox.addWidget(self.run_btn)
        vbox.addLayout(controls_hbox)
        vbox.addWidget(self.simulation_results)

        return sim_tab


    def run_simulation(self):
        # try for random encounters first then add other options
        result = "Press \'Run\' to run a simulation..."  # default entry

        simulation = sim.Simulation(self.shiny_charm_chk.isChecked(), self.masuda_meth_chk.isChecked())
        if self.fish_radio.isChecked():
            result = simulation.shiny_fish(self.counter)
        if self.RE_radio.isChecked():
            result = simulation.random_encounter(self.counter)
        if self.horde_radio.isChecked():
            result = simulation.horde_encounter(self.counter)
        if self.egg_radio.isChecked():
            result = simulation.shiny_eggs(self.counter)
        if self.SOS_radio.isChecked():
            result = simulation.SOS(self.counter)
        if self.dex_radio.isChecked():
            result = simulation.dex_nav(self.counter)


        self.simulation_results.setText(str(result))

    def set_chain(self):
        entry = self.counter_text.text()
        try:
            entry = int(entry)
        except ValueError:
            entry = 0

        self.counter = entry


    def update_shiny_charm(self, sc_chk):

        if sc_chk == Qt.Checked:
            self.sc = True
            self.RE_cum_grid.sc = True
            self.fish_cum_grid.sc = True
            self.horde_cum_grid.sc = True
            self.egg_cum_grid.sc = True
            self.SOS_cum_grid.sc = True
            self.dex_cum_grid.sc = True
        else:
            self.sc = False
            self.RE_cum_grid.sc = False
            self.fish_cum_grid.sc = False
            self.horde_cum_grid.sc = False
            self.egg_cum_grid.sc = False
            self.SOS_cum_grid.sc = False
            self.dex_cum_grid.sc = False

        self.update()

    def update_masuda(self, mm_chk):
        if mm_chk == Qt.Checked:
            self.egg_cum_grid.mm = True
            self.mm = True
        else:
            self.mm = False
            self.egg_cum_grid.mm = False

        self.update()

    def update(self):

        self.RE_cum_grid.update_chance()
        self.fish_cum_grid.update_chance()
        self.horde_cum_grid.update_chance()
        self.egg_cum_grid.update_chance()
        self.dex_cum_grid.update_chance()
        self.SOS_cum_grid.update_chance()


def run():
    app = QApplication(sys.argv)
    return app
