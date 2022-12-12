import random
import numpy as np


def get_p2_games_daily():

    low_ranking_interval = random.randint(1, 2)
    medium_ranking_interval = random.randint(3, 6)
    high_ranking_interval = random.randint(7, 30)

    # The probabilities of drawing a number from each interval
    lri_prob = 0.75
    mri_prob = 0.2
    hri_prob = 0.05

    values = [low_ranking_interval, medium_ranking_interval, high_ranking_interval]
    probabilities = [lri_prob, mri_prob, hri_prob]

    games_played = np.random.choice(values, p=probabilities)

    return games_played
