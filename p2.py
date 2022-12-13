import random
import numpy as np


def get_games_daily() -> int | str:
    """Return number of games played per day"""
    # The probabilities of drawing a number from each interval
    lri_prob = 0.75
    mri_prob = 0.2
    hri_prob = 0.05

    values = [1, 2, 3]
    probabilities = [lri_prob, mri_prob, hri_prob]

    choice = np.random.choice(values, p=probabilities)

    # Randomise the number of games played and set the base modifier
    match choice:
        case 1:
            games_played = random.randint(1, 2)
        case 2:
            games_played = random.randint(3, 6)
        case 3:
            games_played = random.randint(7, 30)
        case _:
            return "Error in match case"

    return games_played
