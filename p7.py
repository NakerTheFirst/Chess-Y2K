import numpy as np
import random


def get_h_slept() -> str | tuple[int, int]:
    """Return the number of hours the subject spent on sleeping per day. Modifier function."""

    # The probabilities of drawing a number from each interval
    lri_prob = 0.1
    mri_prob = 0.25
    hri_prob = 0.65

    values = [1, 2, 3]
    probabilities = [lri_prob, mri_prob, hri_prob]

    choice = np.random.choice(values, p=probabilities)

    # Randomise the number of games played and set the base modifier
    match choice:
        case 1:
            h_slept = random.randint(0, 5)
            mod = random.randint(-20, 0)
        case 2:
            h_slept = random.randint(6, 7)
            mod = random.randint(-5, 5)
        case 3:
            h_slept = random.randint(8, 10)
            mod = random.randint(15, 0)
        case _:
            return "Error in match case"

    return h_slept, mod
