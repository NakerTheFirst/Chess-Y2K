import phase1
import phase2


def main():

    p1_days = phase1.get_p1_ranking()
    p2_days = phase2.get_p2_games()

    print(p1_days, p2_days)


if __name__ == "__main__":
    main()
