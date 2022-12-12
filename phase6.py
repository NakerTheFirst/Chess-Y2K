import numpy as np
import random
import utility


def get_minutes_watched():
    """Used to simulate number of minutes a subject spent on watching chess learning materials"""

    interval = (1, 99)

    # Run through the whole range of specified intervals
    acc = utility.elim_method(interval[0], interval[1])[1]

    return acc
