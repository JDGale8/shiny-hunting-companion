def cum_bin_choice(c, n, m=1):
    """ given a chance c, and number of trials n, returns chance a single success should have occurred"""
    return 1 - (1 * c ** (m-1) * ((1 - c)**n))


def random_encounter(n, successes=1, generation=7, friend_safari=False, shiny_charm=False):
    base = 1 + 2*shiny_charm

    if generation >= 6:
        chance = base/4096
    else:
        friend_safari = False
        chance = base/8192

    if friend_safari:
        chance = 1/512

    cum_chance = cum_bin_choice(chance, n, successes)

    return cum_chance


def egg(n, successes=1, masuda=True, shiny_charm=False, generation=7):
    base = 1 + 2*shiny_charm + masuda

    if generation >= 6:
        chance = base/4096
    else:
        chance = base/8192

    cum_chance = cum_bin_choice(chance, n, successes)

    return cum_chance


def starter(n, choice=False, generation=7):
    base = 1 + 2*choice

    if generation >= 6:
        chance = base/4096
    else:
        chance = base/8192

    cum_chance = cum_bin_choice(chance, n)

    return cum_chance


def fishing(n, successes=1, shiny_charm=False, generation=7):

    chain = 20 if n > 20 else n

    base = 1 + 2*shiny_charm + 2 * chain

    if generation >= 6:
        chance = (1 - ((4095 / 4096) ** base))
    else:
        chance = (1 - ((8191 / 8192) ** base))

    cum_chance = cum_bin_choice(chance, n, successes)

    return cum_chance


def SOS(n, successes=1, shiny_charm=False, generation=7):
    """
    this is assuming SOS works in the same way as fishing
    this is yet to be confirmed
    """
    chain = 20 if n > 20 else n

    base = 1 + 2*shiny_charm + 2*chain

    if generation >= 6:
        chance = (1 - ((4095 / 4096) ** base))
    else:
        chance = (1 - ((8191 / 8192) ** base))

    cum_chance = cum_bin_choice(chance, n, successes)

    return cum_chance


def dex_nav(n, successes=1, shiny_charm=False):
    """
    the jury seems a little out depending on the source you look at as to how the shiny chance
    is affected by chaining the DexNav and by the shiny charm.
    according to https://mrnbayoh.github.io/pkmn6gen/shiny_calculator/:
        the search level and chain make a difference, however, I haven't found any other source to back this up

    according to https://daily.pokecommunity.com/2016/06/13/all-about-shiny-pokemon/ and a similar reddit thread:
        the chance increase (regardless of chain and search level) to something around 1/308

    I don't know which one to trust at the moment, so let's just use the simpler version until more evidence is found

    """

    chance = 1/308
    cum_chance = cum_bin_choice(chance, n, successes)

    return cum_chance


def horde(n, successes=1, shiny_charm=False, generation=7):
    base = (1 + 2*shiny_charm)*5

    if generation >= 6:
        chance = base/4096
    else:
        chance = base/8192

    cum_chance = cum_bin_choice(chance, n, successes)

    return cum_chance
