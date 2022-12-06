import random
import numpy as np


def assign_p1_time(ranking):
    # Initialise for debugging
    days = -1

    match ranking:
        case a if 100 <= ranking <= 899: days = 2400
        case b if 900 <= ranking <= 1399: days = 1900
        case c if 1400 <= ranking <= 1999: days = 1500

    return days


def get_p1_ranking():

    # 100-899 RP interval
    high_time_interval = random.randint(100, 899)
    hti_population = 9029000

    # 900-1399 RP interval
    medium_time_interval = random.randint(900, 1399)
    mti_population = 4229000

    # 1400-1999 RP interval
    low_time_interval = random.randint(1400, 1999)
    lti_population = 980000

    total_population = hti_population + mti_population + lti_population

    # Calculate the probabilities of drawing a number from each interval
    hti_probability = hti_population/total_population
    mti_probability = mti_population/total_population
    lti_probability = lti_population/total_population

    values = [high_time_interval, medium_time_interval, low_time_interval]
    probabilities = [hti_probability, mti_probability, lti_probability]

    ranking = np.random.choice(values, 1, p=probabilities)

    return assign_p1_time(ranking)