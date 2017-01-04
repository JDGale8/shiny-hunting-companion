from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QTextEdit

import calc.chance as ch


class CumGrid:

    def __init__(self, e):
        self.encounter = e
        self.chance = 0
        self.counter = 0  # in the future - have this load from a json file

        self.counter_text = QTextEdit(str(self.counter))
        self.counter_text.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.counter_text.textChanged.connect(self.set_chain)  # if it changes, change chain too

        # set titles and info
        self.counter_label = QLabel("counter")
        self.chance_lb = QLabel("Cum. Shiny Chance:")

        self.inc_btn = QPushButton("+")
        self.inc_btn.clicked.connect(self.increase_counter)
        self.cum_chance_text = QTextEdit("{:.2f}".format(self.chance))
        self.cum_chance_text.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.cum_chance_text.setReadOnly(True)

        if self.encounter == 'fish':
            self.title = QLabel("Chain Fishing")
        elif self.encounter == 'RE':
            self.title = QLabel("Random Encounters")


    def increase_counter(self):
        self.counter += 1
        self.counter_text.setText(str(self.counter))
        self.update_chance()

        # should also then save this counter value to a json file

    def update_chance(self):

        if self.encounter == 'fish':
            chance = ch.fishing(self.counter)
        elif self.encounter == 'RE':
            chance = ch.random_encounter(self.counter)

        self.cum_chance_text.setText("{:.2f}%".format(chance * 100))

    def set_chain(self):
        entry = self.counter_text.toPlainText()
        try:
            entry = int(entry)
        except ValueError:
            entry = 0

        self.counter = entry
        self.update_chance()