import random
import numpy as np


def assign_p2_time(games_played):
    # Initialise for debugging
    days = -1

    match games_played:
        case a if 1 <= games_played <= 3: days = 1500
        case b if 4 <= games_played <= 8: days = 1200
        case c if 9 <= games_played <= 25: days = 700

    return days


def get_p2_games():

    high_time_interval = random.randint(1, 3)
    medium_time_interval = random.randint(4, 8)
    low_time_interval = random.randint(9, 25)

    # The probabilities of drawing a number from each interval
    hti_probability = 0.75
    mti_probability = 0.2
    lti_probability = 0.05

    values = [high_time_interval, medium_time_interval, low_time_interval]
    probabilities = [hti_probability, mti_probability, lti_probability]

    games_played = np.random.choice(values, 1, p=probabilities)

    return assign_p2_time(games_played)
