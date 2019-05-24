# 5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

import string

alphabet = list(string.ascii_lowercase)

first_letter = input("Type a first letter: ")
second_letter = input("Type a second letter: ")

if len(first_letter) == 1 and len(second_letter) == 1 \
        and alphabet.count(first_letter) == 1 and alphabet.count(second_letter) == 1:
    print(f"Position of the letter '{first_letter}' is {alphabet.index(first_letter) + 1}.")
    print(f"Position of the letter '{second_letter}' is {alphabet.index(second_letter) + 1}.")

    if second_letter < first_letter:
        temp_value = first_letter
        first_letter = second_letter
        second_letter = temp_value

    print(f"Letters between of them: {alphabet.index(second_letter) - alphabet.index(first_letter)}.")
else:
    print("Invalid input!")
