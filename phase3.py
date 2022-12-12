import numpy as np
import random
import utility


def get_p3_acc():
    """Used to simulate whether a subject won or lost a game"""

    interval = (1, 99)

    # Run through the whole range of specified intervals
    acc = utility.elim_method(interval[0], interval[1])[1]

    return acc
