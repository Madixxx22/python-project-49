def is_win(correct_answer: int | str, user_answer: int | str,
           name: str, count_win: int) -> int:
    if correct_answer == user_answer:
        count_win += 1
        if count_win == 3:
            print('Correct!')
            print(f'Congratulations, {name}!')
        else:
            print('Correct!')
    else:
        count_win = -1
        print(f'\'{user_answer}\' is wrong answer ;(.'
              f'Correct answer was \'{correct_answer}\'.')
        print(f'Let\'s try again, {name}!')
    return count_win
