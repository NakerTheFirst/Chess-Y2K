import numpy as np
import random


def get_h_slept() -> int:
    """Return the number of hours the subject spent on sleeping per day"""

    low_ranking_interval = random.randint(0, 5)
    medium_ranking_interval = random.randint(6, 7)
    high_ranking_interval = random.randint(8, 10)

    # The probabilities of drawing a number from each interval
    lri_prob = 0.1
    mri_prob = 0.25
    hri_prob = 0.65

    values = [low_ranking_interval, medium_ranking_interval, high_ranking_interval]
    probabilities = [lri_prob, mri_prob, hri_prob]

    h_slept = np.random.choice(values, p=probabilities)

    return h_slept
