from random import choice, randint
from brain_games.games.is_win import is_win

def calc_game(name: str):
    operations = ["+", "-", "*"]
    count_win = 0
    print('What is the result of the expression?')
    while count_win != -1 and count_win < 3:
        op = choice(operations)
        num1 = randint(0, 100)
        num2 = randint(0, 100)
        if op == "+":
            print('Question: {num1} {op} {num2}')
            correct_answer = num1 + num2
        elif op == "-":
            print(f'Question: {num1} {op} {num2}')
            correct_answer = num1 - num2
        else:
            print(f'Question: {num1} {op} {num2}')
            correct_answer = num1 * num2
        user_answer = int(input('Your answer: '))
        if correct_answer == user_answer:
            is_win(True, False, correct_answer, user_answer, name)
            count_win += 1
        else:
            is_win(False, False, correct_answer, user_answer, name)
            count_win = -1
        if count_win == 3:
            is_win(True, True, correct_answer, user_answer, name)