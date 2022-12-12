import numpy as np
import random


def get_player_age():
    """Simulate the age of the player"""
    low_ranking_interval = random.randint(46, 90)
    low_ranking_interval2 = random.randint(1, 4)
    medium_ranking_interval = random.randint(29, 45)
    high_ranking_interval = random.randint(5, 28)

    # The probabilities of drawing a number from each interval
    lri_prob = 0.4
    lri2_prob = 0.06
    mri_prob = 0.21
    hri_prob = 0.33

    values = [low_ranking_interval, low_ranking_interval2, medium_ranking_interval, high_ranking_interval]
    probabilities = [lri_prob, lri2_prob, mri_prob, hri_prob]

    player_age = np.random.choice(values, p=probabilities)

    return player_age


def get_age_modifier(age):
    """Generate learning modifier delta for specific age intervals"""
    delta = "Default delta value"
    if 1 <= age <= 4 and 46 <= age <= 90:
        delta = "To be set"
    elif 29 <= age <= 45:
        delta = "To be set"
    elif 5 <= age <= 28:
        delta = "To be set"

    return delta
