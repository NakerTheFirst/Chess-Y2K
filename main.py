import phase5
import utility
import phase1
import phase2
import phase3

# TODO:
# TODO: Implement daily simulation process with a ranking points track based on matches won


def main():

    # print(phase3.get_acc())
    # print(phase5.get_reviews_daily())
    # print(utility.losses_analysed_curve(95))
    x = utility.elim_method(1, 99, utility.losses_analysed_curve)
    print(x)

    return 0


if __name__ == "__main__":
    main()
