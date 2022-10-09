#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user


def main():
    count_win = 0
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count_win != -1 and count_win < 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = input('Your answer: ')

        if number % 2 == 0 and answer == 'yes':
            print('Correct!')
            count_win += 1
        elif number % 2 != 0 and answer == 'no':
            print('Correct!')
            count_win += 1
        else:
            count_win = -1
            if answer == 'yes':
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print(f'Let\'s try again, {name}!')
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print(f'Let\'s try again, {name}!')
    if count_win == 3:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
