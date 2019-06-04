"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""

from random import randint

DEFAULT_LENGTH = 3
DEFAULT_DIGIT = 3
MAX_RANDINT = 9999999


def counter_digit_in_number(num, dig):
    if num % 10 == dig and num // 10 == 0:
        return 1
    elif num % 10 == dig and num // 10 != 0:
        return 1 + counter_digit_in_number(num // 10, dig)
    elif num % 10 != dig and num // 10 == 0:
        return 0
    else:
        return counter_digit_in_number(num // 10, dig)


length = input("Type the length of sequency: ")

if length.isdecimal():
    length = int(length)
else:
    print(f"Invalid input! Default length is {DEFAULT_LENGTH}!")
    length = DEFAULT_LENGTH

digit = input("Type the digit that you want to count in the sequency: ")
if digit.isdecimal():
    digit = int(digit)
else:
    print(f"Invalid input! Default digit is {DEFAULT_DIGIT}!")
    digit = DEFAULT_DIGIT

result = 0

for i in range(length):
    n = input("Type the number: ")
    if not n.isdecimal():
        n = randint(0, MAX_RANDINT)
        print(f"Invalid input! Random number is {n}!")
    result += counter_digit_in_number(int(n), digit)

print(f"Your result is {result}")
