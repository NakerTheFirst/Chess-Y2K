import utility
import p3


def is_won(base: int = 0) -> bool:
    """Simulate a singular chess match outcome"""
    player_acc = p3.get_acc(base)
    opponent_acc = p3.get_acc()

    if player_acc < opponent_acc:
        return False
    else:
        return True
