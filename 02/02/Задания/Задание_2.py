from operator import truediv


def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Ошибка: Деление на ноль"
    return x / y

def save(r, filename="calculations.txt"):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(str(r) + '\n')


print("Выберите операцию: ")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Вывести историю вычислений")


while True:
    choice = input("Введите номер операции (1/2/3/4/5): ")
    if choice == '1':
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        r = f"Результат: {num1} + {num2} = {add(num1, num2)}"
        print(r)
        save(r)

    elif choice == '2':
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        r = f"Результат: {num1} - {num2} = {subtract(num1, num2)}"
        print(r)
        save(r)
    elif choice == '3':
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        r = f"Результат: {num1} * {num2} = {multiply(num1, num2)}"
        print(r)
        save(r)
    elif choice == '4':
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        r = f"Результат: {num1} / {num2} = {divide(num1, num2):.2f}"
        print(r)
        save(r)
    elif choice == '5':
        print("История вычислений:")
        with open('../calculations.txt', 'r', encoding='utf-8') as file:
            for line in file:
                print(line.strip())
        #return1 = input('Хотите продолжить? Введите "Да" или "Нет": ')
        while True:
            return1 = input('Хотите продолжить? Введите "Да" или "Нет": ')
            if return1 == "Нет" :
                print('Конец программы')
                break
            elif return1 == 'Да' :
                break
        if return1 == 'Нет':
            break


    else:
        print("Неверный ввод")


