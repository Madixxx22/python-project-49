from random import randint
from brain_games.games.is_win import is_win_even

def even_game(name: str):
    count_win = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count_win != -1 and count_win < 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        user_answer = input('Your answer: ')
        count_win = is_win_even(number, user_answer, count_win, name)