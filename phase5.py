import random
import numpy as np


def get_reviews_daily():
    """Get percentage of games analysed and reviewed per day"""

    low_ranking_interval = random.randint(0, 24)
    medium_ranking_interval = random.randint(25, 69)
    high_ranking_interval = random.randint(70, 100)

    # The probabilities of drawing a number from each interval
    hri_prob = 0.2
    mri_prob = 0.65
    lri_prob = 0.15

    values = [low_ranking_interval, medium_ranking_interval, high_ranking_interval]
    probabilities = [hri_prob, mri_prob, lri_prob]

    reviews_daily = np.random.choice(values, p=probabilities)

    return reviews_daily
