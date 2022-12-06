import random
import numpy as np


def get_p2_games_daily():

    high_time_interval = random.randint(1, 2)
    medium_time_interval = random.randint(3, 6)
    low_time_interval = random.randint(7, 30)

    # The probabilities of drawing a number from each interval
    hti_probability = 0.75
    mti_probability = 0.2
    lti_probability = 0.05

    values = [high_time_interval, medium_time_interval, low_time_interval]
    probabilities = [hti_probability, mti_probability, lti_probability]

    games_played = np.random.choice(values, p=probabilities)

    return games_played
