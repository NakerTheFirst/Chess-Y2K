import game_sim
import utility
import phase1
import phase2
import phase3
import phase4
import phase5
import phase6
import phase7
import phase8

# TODO: Implement the daily modifiers for singular match simulation
# TODO: Implement the daily simulation process
# TODO: Change the delta in phase 8 to influence game acc


def main():

    ranking_init = phase1.get_initial_ranking()
    ranking = ranking_init
    print("Initial ranking: ", ranking_init)

    # Simulate a game played per day - NOT X GAMES PLAYED PER DAY
    for x in range(90):
        if game_sim.is_won():
            ranking += 8
        else:
            ranking -= 8

    delta = ranking - ranking_init

    return print("Final ranking: ", ranking, "\nDelta: ", delta)


if __name__ == "__main__":
    main()
