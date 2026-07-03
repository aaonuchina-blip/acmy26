import random


def get_computer_choice():
    choices = ["камень", "ножницы", "бумага"]
    return random.choice(choices)


def get_user_choice():
    while True:
        user_input = (
            input("Введите ваш выбор (камень, ножницы, бумага): ")
            .strip()
            .lower()
        )
        if user_input in ["камень", "ножницы", "бумага"]:
            return user_input
        print("Некорректный ввод. Попробуйте еще раз.")


def check_winner(user, computer):
    if user == computer:
        return "Ничья!"

    if (
        (user == "камень" and computer == "ножницы")
        or (user == "ножницы" and computer == "бумага")
        or (user == "бумага" and computer == "камень")
    ):
        return "Вы выиграли!"

    return "Компьютер выиграл!"


def play_game():

    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nВаш выбор: {user_choice}")
    print(f"Выбор компьютера: {computer_choice}")

    result = check_winner(user_choice, computer_choice)
    print(f"\n{result}")


# Запуск игры
if __name__ == "__main__":
    play_game()