import random
import math
import scipy


def learning_curve(x):
    """A curve simulating learning. Argument has to be an integer from the interval 1-99"""
    return math.log(x, 1.0472)


def losses_analysed_curve(x):
    """A curve simulating % of people analysing lost games. Argument has to be an integer from the interval 1-99"""
    return 0.8299*(math.e**(0.0484*x))


def elim_method(range_start, range_stop, fun):
    """Elimination method for 1-99% range functions. The range_start and range_stop arguments are integers."""

    # Check if f(x) is lower than 0
    for x in range(range_start, range_stop):
        if fun(range_start) < 0:
            return "Error in elim_method"

    # Find the maximum of a function
    fmax = scipy.optimize.minimize_scalar(lambda n: -fun(n), bounds=[range_start, range_stop], method='bounded').x

    # Generate random xl and yl values
    xl = random.randint(range_start, range_stop)
    yl = random.randint(0, math.floor(fmax))

    if yl <= fun(xl):
        return xl, yl

    # If the guess was not correct, redo the randomisation process
    while yl > fun(xl):
        xl = random.randint(range_start, range_stop)
        yl = random.randint(0, math.floor(fmax))

    return xl, yl
