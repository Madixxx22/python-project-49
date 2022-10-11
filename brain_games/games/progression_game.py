from random import choice, randint

from brain_games.games.greetings import greetings
from brain_games.games.is_win import is_win


def progression_game():
    name = greetings()
    count_win = 0
    print('What number is missing in the progression?')
    while count_win != -1 and count_win < 3:
        size_progression = randint(5, 10)
        start_num = randint(0, 100)
        progression = [start_num]
        step_after = randint(1, 10)
        for i in range(size_progression):
            progression.append(step_after + progression[-1])
        correct_answer = choice(progression)
        for i, v in enumerate(progression):
            if v == correct_answer:
                progression[i] = '..'
        print(f'Question: {" ".join(map(str, progression))}')
        user_answer = int(input('Your answer: '))
        count_win = is_win(correct_answer, user_answer, name, count_win)
