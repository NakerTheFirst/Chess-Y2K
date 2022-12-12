import random
import math
import scipy


def learning_curve(x):
    """Argument has to be a float from the interval 1-99"""
    return math.log(x, 1.0472)


def elim_method(range_start, range_stop):
    """Elimination method for learning curve. The arguments interval range have to be integers from 1-99."""

    # Check if f(x) is lower than 0
    for x in range(range_start, range_stop):
        if learning_curve(range_start) < 0:
            return "Error in elim_method"

    # Find the maximum of a function
    fmax = scipy.optimize.minimize_scalar(lambda n: -learning_curve(x), bounds=[range_start, range_stop], method='bounded').x

    # Generate random xl and yl values
    xl = random.randint(range_start, range_stop)
    yl = random.randint(0, math.floor(fmax))

    if yl <= learning_curve(xl):
        return xl, yl

    # If the guess was not correct, redo the randomisation process
    while yl > learning_curve(xl):
        xl = random.randint(range_start, range_stop)
        yl = random.randint(0, math.floor(fmax))

    return xl, yl
