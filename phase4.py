import random
import numpy as np


def get_p5_puzzles():

    high_time_interval = random.randint(0, 3)
    medium_time_interval = random.randint(4, 10)
    low_time_interval = random.randint(11, 30)

    # The probabilities of drawing a number from each interval
    hti_probability = 0.35
    mti_probability = 0.55
    lti_probability = 0.1

    values = [high_time_interval, medium_time_interval, low_time_interval]
    probabilities = [hti_probability, mti_probability, lti_probability]

    puzzles_daily = np.random.choice(values, p=probabilities)

    return puzzles_daily
