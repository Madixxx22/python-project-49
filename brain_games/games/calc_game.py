from random import choice, randint
from brain_games.games.greetings import greetings
from brain_games.games.is_win import is_win


def calc_game():
    name = greetings()
    OPERATIONS = ["+", "-", "*"]
    count_win = 0
    print('What is the result of the expression?')
    while count_win != -1 and count_win < 3:
        op = choice(OPERATIONS)
        num1 = randint(0, 100)
        num2 = randint(0, 100)
        if op == "+":
            print(f'Question: {num1} {op} {num2}')
            correct_answer = num1 + num2
        elif op == "-":
            print(f'Question: {num1} {op} {num2}')
            correct_answer = num1 - num2
        else:
            print(f'Question: {num1} {op} {num2}')
            correct_answer = num1 * num2
        user_answer = int(input('Your answer: '))
        count_win = is_win(correct_answer, user_answer, name, count_win)
