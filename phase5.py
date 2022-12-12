import utility


def get_reviews_daily():
    """Simulate the percentage of lost games analysed per day"""

    interval = (1, 99)

    # Run through the whole range of specified intervals
    reviews_daily = utility.elim_method(interval[0], interval[1], utility.losses_analysed_curve)[1]

    return reviews_daily
