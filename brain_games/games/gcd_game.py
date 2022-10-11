from random import randint
from brain_games.games.greetings import greetings
from brain_games.games.is_win import is_win


def gcd_game():
    name = greetings()
    count_win = 0
    print('Find the greatest common divisior of given numbers.')
    while count_win != -1 and count_win < 3:
        num1 = randint(0, 100)
        num2 = randint(0, 100)
        print(f'Question: {num1} {num2}')
        user_answer = int(input('Your answer: '))
        while True:
            if num1 != 0 and num2 != 0:
                if num1 > num2:
                    num1 = num1 % num2
                else:
                    num2 = num2 % num1
            else:
                correct_answer = num1 + num2
                break
        count_win = is_win(correct_answer, user_answer, name, count_win)
