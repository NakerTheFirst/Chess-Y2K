import numpy as np
import random


def get_minutes_watched():
    """Simulate number of minutes the subject spent on watching chess studying materials per day"""

    low_ranking_interval = random.randint(0, 9)
    medium_ranking_interval = random.randint(10, 19)
    high_ranking_interval = random.randint(20, 60)

    # The probabilities of drawing a number from each interval
    lri_prob = 0.3
    mri_prob = 0.45
    hri_prob = 0.25

    values = [low_ranking_interval, medium_ranking_interval, high_ranking_interval]
    probabilities = [lri_prob, mri_prob, hri_prob]

    minutes_watched = np.random.choice(values, p=probabilities)

    return minutes_watched
