import utility


def get_acc(base: int = 0) -> int:
    """Return the accuracy of a game. Daily modifiers are taken into account."""
    # Run through the specified interval range
    acc = utility.elim_method(1, 99, utility.learning_curve, 3)

    return acc
