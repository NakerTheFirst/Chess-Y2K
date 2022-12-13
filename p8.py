import numpy as np
import random


def get_player_age() -> str | tuple[int, int]:
    """Return the age of the player. Modifier function."""
    # The probabilities of drawing a number from each interval
    lri_prob = 0.4
    lri2_prob = 0.06
    mri_prob = 0.21
    hri_prob = 0.33

    values = [1, 2, 3, 4]
    probabilities = [lri_prob, lri2_prob, mri_prob, hri_prob]

    choice = np.random.choice(values, p=probabilities)

    # Randomise the number of games played and set the base modifier
    match choice:
        case 1:
            player_age = random.randint(46, 90)
            mod = 0
        case 2:
            player_age = random.randint(1, 4)
            mod = 0
        case 3:
            player_age = random.randint(29, 45)
            mod = random.randint(0, 8)
        case 4:
            player_age = random.randint(5, 28)
            mod = random.randint(0, 15)
        case _:
            return "Error in match case"

    return player_age, mod
