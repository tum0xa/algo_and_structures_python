"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

import random

random_number = random.randint(0, 100)

for i in range(0, 10):
    user_number = input("Try guess the number (from 0 to 100): ")
    if user_number.isdecimal() and (int(user_number) > 100 or int(user_number) < 0):
        print("Invalid input! Try again.")
        continue
    else:
        if int(user_number) == random_number:
            print("Congratulations! You guessed the number!")
            quit()
        elif int(user_number) > random_number:
            print("The hidden number is less!")
            continue
        elif int(user_number) < random_number:
            print("The hidden number is greater!")
            continue
        else:
            print("Something wrong!? Try again.")
            continue

print(f"So sad! The number is {random_number}!")