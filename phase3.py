import utility


def get_acc() -> int:
    """Simulate the % accuracy of a game. Daily modifiers are taken into account."""
    interval = [1, 99]

    # increased by randint from range
    # interval[0] += 3

    # Run through the specified interval range
    acc = utility.elim_method(interval[0], interval[1], utility.learning_curve, 3)

    return acc
