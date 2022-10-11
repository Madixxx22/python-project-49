from random import randint

from brain_games.games.greetings import greetings
from brain_games.games.is_win import is_win


def prime_game():
    name = greetings()
    count_win = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while count_win != -1 and count_win < 3:
        list_decimal = []
        num = randint(1, 100)
        for i in range(1, num+1):
            if num % i == 0:
                list_decimal.append(i)
        if len(list_decimal) == 2:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f'Question: {num}')
        user_answer = input('Your answer: ')
        count_win = is_win(correct_answer, user_answer, name, count_win)
