import sys


global MINDIFF
MINDIFF = 0.0001


def improve_guess(n, guess):
    return ((n / guess) + guess) / 2


def good_enough(n, guess):
    return abs(n - (guess ** 2)) < MINDIFF


def newton_root(n, guess):
    if good_enough(n, guess):
        return guess
    else:
        return newton_root(n, improve_guess(n, guess))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Pease specify a number.")
    else:
        print(newton_root(float(sys.argv[1]), 1.0))
