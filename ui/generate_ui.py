from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QVBoxLayout

import calc.chance as ch
import calc.shiny_sim as sim


class CumGrid:

    def __init__(self, e):

        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.sc = False  # shiny charm
        self.mm = False  # masuda

        self.encounter = e
        self.chance = 0
        self.counter = 0  # in the future - have this load from a json file

        self.counter_text = QLineEdit(str(self.counter))
        self.counter_text.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.counter_text.textChanged.connect(self.set_chain)  # if it changes, change chain too

        # set titles and info
        self.counter_label = QLabel("counter")
        self.chance_lb = QLabel("Chance:")

        self.inc_btn = QPushButton("+")
        self.inc_btn.clicked.connect(self.increase_counter)
        self.inc_btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.cum_chance_text = QLineEdit("{:.2f}".format(self.chance))
        self.cum_chance_text.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.cum_chance_text.setReadOnly(True)

        self.set_title()

        self.set_grid()

    def set_grid(self):

        self.grid.addWidget(self.title, 0, 0)
        self.grid.addWidget(self.counter_label, 1, 0)
        self.grid.addWidget(self.counter_text, 1, 1)
        self.grid.addWidget(self.inc_btn, 1, 2)
        self.grid.addWidget(self.chance_lb, 2, 1)
        self.grid.addWidget(self.cum_chance_text, 2, 2)

    def set_title(self):
        title = None
        if self.encounter == 'fish':
            title = "Chain Fishing"
        elif self.encounter == 'RE':
            title = "Random Encounters"
        elif self.encounter == 'horde':
            title = "Horde Encounters"
        elif self.encounter == 'egg':
            title = "Hatched Eggs"
        elif self.encounter == 'SOS':
            title = "SOS"
        elif self.encounter == 'dex':
            title = "DexNav"

        self.title = QLabel(title)

    def increase_counter(self):
        self.counter += 1
        self.counter_text.setText(str(self.counter))
        self.update_chance()

        # should also then save this counter value to a json file

    def update_chance(self):
        if self.encounter == 'fish':
            chance = ch.fishing(self.counter, shiny_charm=self.sc)
        elif self.encounter == 'RE':
            chance = ch.random(self.counter, shiny_charm=self.sc)
        elif self.encounter == 'horde':
            chance = ch.horde(self.counter, shiny_charm=self.sc)
        elif self.encounter == 'egg':
            chance = ch.egg(self.counter, shiny_charm=self.sc, masuda=self.mm)
        elif self.encounter == 'SOS':
            chance = ch.SOS(self.counter, shiny_charm=self.sc)
        elif self.encounter == 'dex':
            chance = ch.dex_nav(self.counter, shiny_charm=self.sc)

        self.cum_chance_text.setText("{:.2f}%".format(chance * 100))

    def set_chain(self):
        entry = self.counter_text.text()
        try:
            entry = int(entry)
        except ValueError:
            entry = 0

        self.counter = entry
        self.update_chance()


class SimUI:

    def __init__(self):
        self.grid = QVBoxLayout()
        self.grid.setSpacing(10)

        self.sc = False  # shiny charm
        self.mm = False  # masuda

        self.counter = 0  # in the future - have this load from a json file

        # quick simulation buttons - maybe?

        self.counter_text = QLineEdit(str(self.counter))
        self.counter_text.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        self.counter_text.textChanged.connect(self.set_chain)  # deals with non integer entries

        self.simulation_results = QLabel("Press \'Run\' to run a simulation...")
        self.run_btn = QPushButton("Run")
        self.run_btn.clicked.connect(self.run_simulation)

        controls_hbox = QHBoxLayout()
        controls_hbox.addWidget(self.counter_text)
        controls_hbox.addWidget(self.run_btn)

        self.grid.addLayout(controls_hbox)
        self.grid.addWidget(self.simulation_results)

    def set_chain(self):
        entry = self.counter_text.toPlainText()
        try:
            entry = int(entry)
        except ValueError:
            entry = 0

        self.counter = entry

    def run_simulation(self):
        # try for random encounters first then add other options

        # result = sim.random(self.counter)
        self.simulation_results.setText("asdasd")
