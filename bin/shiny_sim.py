import random
import chance as ch


class Simulate:

    def __init__(self):
        self.shiny_charm = False
        self.masuda = False

    def shiny_eggs(self, n_eggs):
        masuda = True

        shiny_chance = (1 + 5*masuda + self.shiny_charm)/4096

        shiny_eggs = []
        for i in range(n_eggs):
            chance = random.random()
            if chance < shiny_chance:
                shiny_eggs.append(i)

        print("In {} eggs you received {} shiny pokemon. They were in the following eggs: {}"
              .format(n_eggs, len(shiny_eggs), shiny_eggs))

    @staticmethod
    def shiny_starter(no_of_sr):
        shiny_chance = 3/4096

        shiny_pokemon = []

        for i in range(no_of_sr):
            chance = random.random()
            if chance < shiny_chance:
                shiny_pokemon.append(i)

        print("In {} soft resets you received {} shiny pokemon. They were in the following SRs: {}"
              .format(no_of_sr, len(shiny_pokemon), shiny_pokemon))

    def shiny_fish(self, fishing_chain):
        chain = 1
        shiny_fish = []
        for i in range(fishing_chain):
            if chain > 20:
                chain = 20

            numerator = 1 + 2 * self.shiny_charm + chain * 2
            shiny_chance = numerator/4096

            chance = random.random()
            if chance < shiny_chance:
                shiny_fish.append(i)
            chain += 1

        print("In a chain of {}, you received {} shiny pokemon. They were in the following reels: {}"
              .format(fishing_chain, len(shiny_fish),shiny_fish))

    def random_encounter(self, number_of_encounters, friend_safari=False):

        shiny_encounters = []

        for i in range(number_of_encounters):
            if friend_safari:
                shiny_chance = 1/512
            else:
                shiny_chance = (1 + 2*self.shiny_charm)/4096
            chance = random.random()
            if chance < shiny_chance:
                shiny_encounters.append(i)

        print("In {} encounters you received {} shiny pokemon. They were in the following encounters: {}"
              .format(number_of_encounters, len(shiny_encounters),shiny_encounters))

    def horde_encounter(self, number_of_encounters):
        shiny_encounters = []

        shiny_chance = ((1 + 2*self.shiny_charm)*5)/4096
        for i in range(number_of_encounters):
            chance = random.random()
            if chance < shiny_chance:
                shiny_encounters.append(i)

        print("In {} encounters you received {} shiny pokemon. They were in the following encounters: {}"
              .format(number_of_encounters, len(shiny_encounters), shiny_encounters))
