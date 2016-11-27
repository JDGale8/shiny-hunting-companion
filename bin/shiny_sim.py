import random
from bin import chance as ch


def plural(number):
    return '' if number == 1 else 's'


class Simulation:

    def __init__(self):
        self.shiny_charm = False
        self.masuda = False

    def shiny_eggs(self, n_eggs, successes=1):
        masuda = True

        shiny_chance = (1 + 5*masuda + self.shiny_charm)/4096

        shiny_eggs = []
        for i in range(n_eggs):
            chance = random.random()
            if chance < shiny_chance:
                shiny_eggs.append(i)

        cum_chance = ch.egg(n_eggs, masuda=masuda, shiny_charm=self.shiny_charm, successes=successes)

        print("In {} eggs you received {} shiny pokemon.".format(n_eggs, len(shiny_eggs)))
        if len(shiny_eggs) >0:
            print("They were in the following eggs: {}. ".format(shiny_eggs))
        print("There was a {:.2f}% chance of finding {} shiny egg{}".format(cum_chance*100, successes, plural(successes)))

    @staticmethod
    def shiny_starter(no_of_sr, successes=1, generation=7):
        """
        depending on the other generations, the starters shiny status may be visible before choosing.
        in gen 7 this is not the case, so I am writing the examples for that for now.
        if I figure out this is different for other generations I will add them in
        """
        if generation == 7:
            shiny_chance = 1/4096
        else:
            shiny_chance = 3/4096

        shiny_pokemon = []

        for i in range(no_of_sr):
            chance = random.random()
            if chance < shiny_chance:
                shiny_pokemon.append(i)

        cum_chance = ch.starter(no_of_sr, generation=generation)

        print("In {} eggs you received {} shiny pokemon.".format(no_of_sr, len(shiny_pokemon)))
        if len(shiny_pokemon) > 0:
            print("They were in the following resets: {}. ".format(shiny_pokemon))
        print("There was a {:.2f}% chance of finding {} shiny starter{}"
              .format(cum_chance*100, successes, plural(successes)))

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
