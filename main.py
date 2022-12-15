import matplotlib.pyplot as plt
import scipy.optimize
import numpy as np
import game_sim
import utility
import p1
import p2
import p4
import p5
import p6
import p7
import p8

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
    # Simulate the process 7000 times
    # for x in range(7000):
    #     data.append(sim_90_days())

    # Write the data to file
    # with open('data.txt', 'w') as f:
    #     for x in range(len(data)):
    #         f.write(f"{str(data[x])} ")
    #     f.write("\n")

    # Read the data from file
    with open('data.txt') as f:
        data = f.readlines()

    for x in range(7000):
        data[x] = data[x].rstrip()
        data[x] = int(data[x])

    tops, bin_edges = np.histogram(data, bins=50)
    bin_centres = []
    mean = np.mean(data)
    std = np.std(data)

    for x in range(len(tops)):
        bin_centres.append((bin_edges[x] + bin_edges[x+1]) / 2)

    plt.hist(data, bins=50, density=True, label="Data")

    fit_params, cov_matrix = scipy.optimize.curve_fit(utility.gauss_dist, bin_centres, tops)
    y_output = scipy.stats.norm.pdf(bin_centres, mean, std)

    plt.title("How much can one's ranking change after 90 days of learning?")
    plt.xlabel("Ranking change")
    plt.ylabel("Density")
    plt.plot(bin_centres, y_output, label=f"Fitting function")
    plt.legend()
    plt.show()

    return 0


if __name__ == "__main__":
    main()
