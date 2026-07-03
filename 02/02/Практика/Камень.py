import random

def get_user_choice():
    choices = ['камень', 'ножницы', 'бумага']
    user = input("Введите ваш выбор камень, ножницы, бумага или выход: ").lower()

    if user == 'выход':
        return user
    if user not in choices:
        raise ValueError ("Такого варианта нет")
        # print('Такого варианта нет')
    return user




def get_comp_choice():
    choices = ['камень', 'ножницы', 'бумага']
    computer = random.choice(choices)
    return computer

def check_winner(user, computer):
    if user == computer:
        return "Ничья!"
    elif ((user == "камень" and computer == "ножницы")
            or (user == "ножницы" and computer == "бумага")
            or (user == "бумага" and computer == "камень")):
        return "Вы выиграли!"
    return "Компьютер выиграл!"

while True:
    try:
        choices = ['камень', 'ножницы', 'бумага']
        user = get_user_choice()
        if user == 'выход':
            print('Игра окончена')
            break
        if user not in choices:
            print('Такого варианта нет')

        print(f'Вы выбрали {user}')
        computer = get_comp_choice()
        print(f'Компьютер выбрал {computer}')

        result = check_winner(user,computer)
        print(result)

    except Exception as e:
        print("Ошибка", e)




