from brain_games.cli import welcome_user


def greetings() -> str:
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(f'Hello, {name}!')
    return name
