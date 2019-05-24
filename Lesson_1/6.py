# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string

alphabet = list(string.ascii_lowercase)

pos_of_letter = input("Type the position of a letter in the english alphabet: ")

if pos_of_letter.isdecimal():
    pos_of_letter = int(pos_of_letter)
    if pos_of_letter < 0 or pos_of_letter > len(alphabet):
        print("Type the correct number of position (from 1 to 26), please!")
        quit(0)
    print(f"Your letter is '{alphabet[pos_of_letter - 1].upper()}'.")
else:
    print("Invalid input!")
