#!/usr/bin/env python3
from brain_games.games.greetings import greetings
from brain_games.games.even_game import even_game

def main():
    name = greetings()
    even_game(name)


if __name__ == "__main__":
    main()
