import numpy as np
import random


def get_puzzles_daily() -> str | tuple[int, int]:
    """Return number of chess puzzles done per day. Modifier function."""
    # The probabilities of drawing a number from each interval
    lri_prob = 0.1
    mri_prob = 0.55
    hri_prob = 0.35

    values = [1, 2, 3]
    probabilities = [lri_prob, mri_prob, hri_prob]

    choice = np.random.choice(values, p=probabilities)

    # Randomise the number of games played and set the base modifier
    match choice:
        case 1:
            puzzles_daily = random.randint(0, 3)
            mod = random.randint(0, 3)
        case 2:
            puzzles_daily = random.randint(4, 10)
            mod = random.randint(0, 5)
        case 3:
            puzzles_daily = random.randint(11, 30)
            mod = random.randint(0, 15)
        case _:
            return "Error in match case"

    return puzzles_daily, mod
