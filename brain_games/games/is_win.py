def is_win_even(correct_answer: int, user_answer: str, count_win: int, name: str) -> int:
    if correct_answer % 2 == 0 and user_answer == 'yes':
        print('Correct!')
        count_win += 1
    elif correct_answer % 2 != 0 and user_answer == 'no':
        print('Correct!')
        count_win += 1
    else:
        count_win = -1
        if user_answer == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f'Let\'s try again, {name}!')
        else:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f'Let\'s try again, {name}!')
    if count_win == 3:
        print(f'Congratulations, {name}!')
    return count_win

def is_win_calc(correct_answer: int, user_answer: int, count_win: int, name: str) -> int:
    if correct_answer == user_answer:
        print('Correct!')
        count_win += 1
    else:
            print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            count_win = -1
    if count_win == 3:
        print(f'Congratulations, {name}')
    return count_win