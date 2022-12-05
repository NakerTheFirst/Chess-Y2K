import random
import numpy as np


def assign_p2_time(puzzle_number):
    # Initialise for debugging
    days = -1

    match puzzle_number:
        case a if 0 <= puzzle_number <= 3: days = 1500
        case b if 4 <= puzzle_number <= 10: days = 1000
        case c if 11 <= puzzle_number <= 30: days = 500

    return days


def get_p2_games():

    high_time_interval = random.randint(0, 3)
    medium_time_interval = random.randint(4, 10)
    low_time_interval = random.randint(11, 30)

    # The probabilities of drawing a number from each interval
    hti_probability = 0.35
    mti_probability = 0.55
    lti_probability = 0.1

    values = [high_time_interval, medium_time_interval, low_time_interval]
    probabilities = [hti_probability, mti_probability, lti_probability]

    puzzle_number = np.random.choice(values, 1, p=probabilities)

    return assign_p2_time(puzzle_number)
