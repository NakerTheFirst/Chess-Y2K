import numpy as np
import random


def get_minutes_watched() -> tuple[int, int]:
    """Return number of minutes subject spent on watching educational chess materials per day. Modifier function."""

    # The probabilities of drawing a number from each interval
    lri_prob = 0.3
    mri_prob = 0.45
    hri_prob = 0.25

    values = [1, 2, 3]
    probabilities = [lri_prob, mri_prob, hri_prob]

    choice = np.random.choice(values, p=probabilities)

    # Randomise the number of games played and set the base modifier
    match choice:
        case 1:
            minutes_watched = random.randint(0, 9)
            mod = random.randint(0, 3)
        case 2:
            minutes_watched = random.randint(10, 19)
            mod = random.randint(0, 8)
        case 3:
            minutes_watched = random.randint(20, 60)
            mod = random.randint(0, 15)
        case _:
            return -1, -1

    return minutes_watched, mod
