import utility


def get_acc():
    """Simulate the % accuracy of a game"""

    interval = (1, 99)

    # Run through the whole range of specified intervals
    acc = utility.elim_method(interval[0], interval[1], utility.learning_curve)[1]

    return acc
