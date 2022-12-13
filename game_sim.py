import utility
import phase3


def is_won() -> bool:
    """Simulate a singular chess match outcome"""

    player_acc = phase3.get_acc()
    opponent_acc = phase3.get_acc()

    if player_acc < opponent_acc:
        return False
    else:
        return True
