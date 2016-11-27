

def cum_bin_choice(c, n, m=1):
    """ given a chance c, and number of trials n, returns chance a single success should have occured"""
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
    """ this is assuming SOS works in the same way as fishing"""
    chain = 20 if n > 20 else n

    base = 1 + 2*shiny_charm + 2 * chain

    if generation >= 6:
        chance = (1 - ((4095 / 4096) ** base))
    else:
        chance = (1 - ((8191 / 8192) ** base))

    cum_chance = cum_bin_choice(chance, n, successes)

    return cum_chance


def dex_nav(n, search_level, successes=1, shiny_charm=False):
    search_level

    if n >= 50:
        chain = 5
    elif n >= 100:
        chain = 10
    else:
        chain = 0


    base = 1 + chain + 2*shiny_charm + random_bonus

    pass


def horde(n, successes=1, shiny_charm=False, generation=7):
    base = (1 + 2*shiny_charm)*5

    if generation >= 6:
        chance = base/4096
    else:
        chance = base/8192

    cum_chance = cum_bin_choice(chance, n, successes)

    return cum_chance
