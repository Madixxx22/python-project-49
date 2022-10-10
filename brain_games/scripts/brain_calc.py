from brain_games.games.greetings import greetings
from brain_games.games.calc_game import calc_game


def main():
    name = greetings()
    calc_game(name)


if __name__ == "__main__":
    main()
