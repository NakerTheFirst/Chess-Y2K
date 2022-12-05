import random
import numpy as np


def assign_p3_time(delta):
    # Initialise for debugging
    days = -1

    match delta:
        case a if -20 <= delta <= 0: days = 2000
        case b if 1 <= delta <= 20: days = 100
        case c if 21 <= delta <= 100: days = 20

    return days


def get_p3_delta():

    high_time_interval = random.randint(-20, 0)
    medium_time_interval = random.randint(1, 20)
    low_time_interval = random.randint(21, 100)

    # The probabilities of drawing a number from each interval
    hti_probability = 0.4
    mti_probability = 0.5
    lti_probability = 0.1

    values = [high_time_interval, medium_time_interval, low_time_interval]
    probabilities = [hti_probability, mti_probability, lti_probability]

    delta = np.random.choice(values, 1, p=probabilities)

    return assign_p3_time(delta)
