"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""
import random
import string


def isfloat(raw_str):
    """Function that return "True" if the input string is a float number.

    Keyword arguments:
    raw_str -- Raw string for checking

    """

    if str(raw_str).count('.') > 1 or str(raw_str).count('.') == 0:
        return False

    dec_part = str(raw_str).split('.')[0]
    float_part = str(raw_str).split('.')[1]

    if dec_part.isdecimal() and float_part.isdecimal:
        return True
    else:
        return False


print("You can generate random values for the next cases (depends of your input):\n"
      "- for integer numbers;\n"
      "- for floating numbers;\n"
      "- for english letters. ")
start_value = input("Type a start value for a range: ")
end_value = input("Type an end value for the range: ")

if start_value.isdecimal() and end_value.isdecimal():
    if int(end_value) < int(start_value):
        temp_value = start_value
        start_value = end_value
        end_value = temp_value
    print(f"Your random integer number is {random.randint(int(start_value), int(end_value))}")

elif isfloat(start_value) and isfloat(end_value):
    if float(end_value) < float(start_value):
        temp_value = start_value
        start_value = end_value
        end_value = temp_value
    print(f"Your random floating number is {float(start_value) + (float(end_value) - float(start_value)) * random.random()}")

elif len(start_value) == 1 and len(end_value) == 1 and start_value.isalpha() and end_value.isalpha():
    if end_value < start_value:
        temp_value = start_value
        start_value = end_value
        end_value = temp_value

    # get the list of lowercase letters
    alphabet = list(string.ascii_lowercase)
    start_value = start_value.lower()
    end_value = end_value.lower()
    print(f"Your random character symbol is '{random.choice(alphabet[alphabet.index(start_value):alphabet.index(end_value)])}'")

else:
    print("Invalid input!")
