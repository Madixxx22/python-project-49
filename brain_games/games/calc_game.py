from random import choice, randint
from brain_games.games.is_win import is_win_calc

def calc_game(name: str):
    operations = ["+", "-", "*"]
    count_win = 0
    print('What is the result of the expression?')
    while count_win != -1 and count_win < 3:
        op = choice(operations)
        num1 = randint(0, 100)
        num2 = randint(0, 100)
        if op == "+":
            print(f'Question: {num1} {op} {num2}')
            answer_correct = num1 + num2
        elif op == "-":
            print(f'Question: {num1} {op} {num2}')
            answer_correct = num1 - num2
        else:
            print(f'Question: {num1} {op} {num2}')
            answer_correct = num1 * num2
        user_answer = input('Your answer: ')
        count_win = is_win_calc(int(answer_correct), int(user_answer), count_win, name)
              
