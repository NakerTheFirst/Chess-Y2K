import numpy as np
import utility
import random


def get_reviews_daily() -> str | tuple[int | int]:
    """Return the percentage of lost games analysed per day. Modifier function."""

    # The probabilities of drawing a number from each interval
    lri_prob = 0.26
    mri_prob = 0.44
    hri_prob = 0.30

    values = [1, 2, 3]
    probabilities = [lri_prob, mri_prob, hri_prob]

    choice = np.random.choice(values, p=probabilities)

    match choice:
        case 1:
            mod = random.randint(0, 3)
        case 2:
            mod = random.randint(0, 5)
        case 3:
            mod = random.randint(0, 10)
        case _:
            return "Error in match case"

    # Run through the whole range of specified intervals
    reviews_daily = utility.elim_method(1, 99, utility.losses_analysed_curve)

    return reviews_daily, mod
