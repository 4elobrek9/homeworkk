import time
import random

# Игра «Угадай число»

def guess_number():
    min_num = 0
    max_num = 100

    while True:
        print("Загадайте число от 0 до 100, а я угадаю)))")
        time.sleep(2)
        random_number = random.randint(min_num, max_num)  # Генерация случайного числа
        print(f"Ваше число {random_number} ?")

        user_input = input("Введите > если число больше, < если меньше, = если равно: ")

        if user_input == '>':
            min_num = random_number + 1
        elif user_input == '<':
            max_num = random_number - 1
        elif user_input == '=':
            print(f"Ура! Я угадал ваше число - {random_number}!")
            break
        else:
            print("Неверный ввод. Попробуйте еще раз.")

# Запуск игры
guess_number()
