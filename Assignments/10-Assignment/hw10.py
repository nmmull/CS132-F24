import numpy as np

def survival_matrix(chick_sr, adol_sr, adult_sr, num_eggs):
    """Matrix representing the population dynamics of a newly
    discovered seabird

    Parameters:

      chick_sr: integer between 0 and 100 (representing a percentage)
      adol_sr: integer between 0 and 100 (representing a percentage)
      adult_sr: integer between 0 and 100 (representing a percentage)
      num_eggs: nonnegative float

    Returns:

      numpy array A with shape (3, 3) for the linear dynamical system
      modeling the population dynamics of the newly discovered
      seabirds, given the chick survival rate (`chick_sr`), adolescent
      survival rate (`adol_sr`), adult survival rate (`adult_sr`), and the
      number of eggs per *pair* of adults (`num_eggs`).  Note that
      adolescents don't lay eggs

      Given a numpy array

        array([ num_chicks, num_adols, num_adults ])

      the array

        A @ array([num_chicks, num_adols, num_adults])

      is

        array([ num_chicks', num_adols', num_adults' ])

      where

        `num_chicks'` is the number of chicks after one year
        `num_adols'` is the number of adolescents after one year
        `num_adults'` is the number of adults after one year

    """
    return None # TODO

def min_non_extinct_rate_chicks(adol_sr, adult_sr, num_eggs):
    """Determines the smallest chick survival rate rounded to the
    nearest percentage for which the species is not expected to go
    extinct in the long term

    Parameters:

      adol_sr: integer between 0 and 100 (representing a percentage)
      adult_sr: integer between 0 and 100 (representing a percentage)
      num_eggs: nonnegative float

    Returns:

      The smallest integer S between 0 and 100 such that the largest
      eigenvalue of the survival matrix with the given parameters
      (with the same interpretation as in the previous function) and a
      chick survival rate of S percent is at least 1

      The function should return None if there is no such integer S

    Example:

      >>> min_non_extinct_rate_chicks(90, 70, 3)
      23
      >>> min_non_extinct_rate_chicks(80, 80, 4)
      13

    """
    return None # TODO


def min_non_extinct_rate(num_eggs):
    """Determines the smallest survival rate of both adolescents and
    adults (assuming they are the same) for which it non-extinction is
    possible.

    Parameters:

      num_eggs: nonnegative float

    Returns:

      The smallest integer S between 0 and 100 such that there is some
      chick survival rate C so that the largest eigenvalue of
      `survival_matrix(C, S, S, num_eggs)` is at least 1

      The function should return None if there is no such integer S

      Note that, if S is very low, it may be that even with a 100%
      chick survival rate, the species is still expected to go
      extinct

    Example:

      >>> min_non_extinct_rate(2)
      51
      >>> min_non_extinct_rate(3)
      41

    """
    return None # TODO

def years_until_extinct(
        chick_sr,
        adol_sr,
        adult_sr,
        num_eggs,
        num_chicks,
        num_adols,
        num_adults):
    """Determines how many years it will take for the seabird
    population to go extinct if it is expected to in the long term

    Parameters:

      chick_sr: integer between 0 and 100 (representing a percentage)
      adol_sr: integer between 0 and 100 (representing a percentage)
      adult_sr: integer between 0 and 100 (representing a percentage)
      num_eggs: nonnegative float
      num_chicks: nonnegative integer
      num_adols: nonnegative integer
      num_adults: nonnegative integer

    Returns:

      The number of years it takes for a population with `num_chicks`
      many chicks, `num_adols` many adolescents, and `num_adults` many
      adults to go extinct as determined by the linear dynamical
      system with the given parameters

      The function should return None if it is not expected that the
      population will go extinct

      IMPORTANT: when checking if the population is 0, you should
      floor divide the any estimates on the numbers of chicks,
      adolescents, and adults (there is no such thing as a fractional
      bird in the real world)

    Example:

      >>> years_until_extinct(20, 80, 80, 3, 40000, 30000, 30000) == None
      True
      >>> years_until_extinct(15, 80, 80, 3, 40000, 30000, 30000)
      754
      >>> years_until_extinct(15, 90, 70, 3, 40000, 30000, 30000)
      161

    """
    return None # TODO
