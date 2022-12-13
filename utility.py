import random
import math
import scipy


def learning_curve(x: int) -> float:
    """A curve simulating learning. Argument has to be an integer from the interval 1-99"""
    return math.log(x, 1.0472)


def losses_analysed_curve(x: int) -> float:
    """A curve simulating % of people analysing lost games. Argument has to be an integer from the interval 1-99"""
    return 0.8299 * (math.e ** (0.0484 * x))


def elim_method(range_start: int, range_stop: int, fun, base: int = 0) -> int | str:
    """Elimination method for curve functions"""

    # Check if f(x) is lower than 0
    for x in range(range_start, range_stop):
        if fun(range_start) < 0:
            return "Error in elim_method"

    # Find the maximum of a function
    fmax = scipy.optimize.minimize_scalar(lambda n: -fun(n), bounds=[range_start, range_stop], method='bounded').x

    # Generate random xl and yl values
    xl = random.randint(range_start, range_stop)
    yl = random.randint(base, math.floor(fmax))

    if yl <= fun(xl):
        return yl

    # If the guess was not correct, redo the randomisation process
    while yl > fun(xl):
        xl = random.randint(range_start, range_stop)
        yl = random.randint(0, math.floor(fmax))

    return yl


def get_mod(puzz_mod: int = 0, revs_mod: int = 0, vids_mod: int = 0, sleep_mod: int = 0, age_mod: int = 0):
    """Return the modified base of the interval from which the acc is generated"""
    base = puzz_mod + revs_mod + vids_mod + sleep_mod + age_mod

    # Handle base < 0 exception
    if base < 0:
        base = 0

    return base
