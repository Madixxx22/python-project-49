def is_win(check_cor: bool, check_win: bool, correct_answer: int | str, user_answer: int | str, name: str):
    if check_cor == True:
        print('Correct!')
    else:
        print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
        print(f'Let\'s try again, {name}!')
    if check_win == True:
        print(f'Congratulations, {name}!')