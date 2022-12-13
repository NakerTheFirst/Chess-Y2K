import game_sim
import utility
import p1
import p2
import p3
import p4
import p5
import p6
import p7
import p8

# TODO: Implement the daily modifiers for singular match simulation
# TODO: Implement the daily simulation process
# TODO: Change the delta in phase 8 to influence game acc


def main():

    ranking_init = p1.get_initial_ranking()
    ranking = ranking_init

    # Simulate a game played per day - NOT X GAMES PLAYED PER DAY
    for x in range(90):
        if game_sim.is_won():
            ranking += 8
        else:
            ranking -= 8

    delta = ranking - ranking_init

    return print(f"Initial ranking: \n{ranking_init} Final ranking: {ranking} \nDelta: {delta}")


if __name__ == "__main__":
    main()
