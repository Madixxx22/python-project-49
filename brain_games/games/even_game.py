from random import randint
from brain_games.games.is_win import is_win

def even_game(name: str):
    count_win = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count_win != -1 and count_win < 3:
        correct_answer = randint(1, 100)
        print(f'Question: {correct_answer}')
        user_answer = input('Your answer: ')
        if correct_answer % 2 == 0 and user_answer == 'yes':
            is_win(True, False, correct_answer, user_answer, name)
            count_win += 1
        elif correct_answer % 2 != 0 and user_answer == 'no':
            is_win(True, False, correct_answer, user_answer, name)
            count_win += 1
        else:
            count_win = -1
            if user_answer == 'yes':
                is_win(False, False, correct_answer, user_answer, name)
            
            else:
                is_win(False, False, correct_answer, user_answer, name)
        if count_win == 3:
            is_win(True, True, correct_answer, user_answer, name)
