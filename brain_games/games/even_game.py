from random import randint
from brain_games.games.greetings import greetings
from brain_games.games.is_win import is_win


def even_game():
    name = greetings()
    count_win = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count_win != -1 and count_win < 3:
        num = randint(1, 100)
        print(f'Question: {num}')
        user_answer = input('Your answer: ')
        if num % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        count_win = is_win(correct_answer, user_answer, name, count_win)