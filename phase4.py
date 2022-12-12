import random
import numpy as np


def get_puzzles_daily():
    """Simulate number of chess puzzles done per day"""
    low_ranking_interval = random.randint(0, 3)
    medium_ranking_interval = random.randint(4, 10)
    high_ranking_interval = random.randint(11, 30)

    # The probabilities of drawing a number from each interval
    hri_prob = 0.35
    mri_prob = 0.55
    lri_prob = 0.1

    values = [low_ranking_interval, medium_ranking_interval, high_ranking_interval]
    probabilities = [hri_prob, mri_prob, lri_prob]

    puzzles_daily = np.random.choice(values, p=probabilities)

    return puzzles_daily
