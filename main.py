import game_sim
import utility
import p1
import p2
import p4
import p5
import p6
import p7
import p8

# TODO: Write the data to data.txt file
# TODO: Create a histogram from the data.txt - x: samples with the same result y: value of delta
# TODO: Create a valid documentation - simply use README.md


def sim_90_days():
    """Return the delta ranking of one test subject after running 90 days of simulation"""
    ranking_init = p1.get_initial_ranking()
    ranking = ranking_init
    age_mod = p8.get_player_age()[1]
    delta = 0

    for x in range(90):
        games_daily = p2.get_games_daily()
        mod = utility.get_mod(p4.get_puzzles_daily()[1], p5.get_reviews_daily()[1],
                              p6.get_minutes_watched()[1], p7.get_h_slept()[1], age_mod)

        for n in range(games_daily):
            if game_sim.is_won(mod):
                ranking += 8
            else:
                ranking -= 8

        delta = ranking - ranking_init

    return delta


def main():
    data = []

    # Simulate the process 7000 times
    for x in range(100):
        data.append(sim_90_days())

    return 0


if __name__ == "__main__":
    main()
