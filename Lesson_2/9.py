"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

from random import randint

DEFAULT_LENGTH = 3
DEFAULT_DIGIT = 3
MAX_RANDINT = 9999999


def sum_of_digits_in_number(num):
    if num // 10 == 0:
        return num % 10
    else:
        return num % 10 + sum_of_digits_in_number(num // 10)


length = input("Type the length of sequence: ")

if length.isdecimal():
    length = int(length)
else:
    print(f"Invalid input! Default length is {DEFAULT_LENGTH}!")
    length = DEFAULT_LENGTH

result = 0
max_number = 0
for i in range(length):
    n = input("Type a natural number: ")
    if not n.isdecimal():
        n = randint(0, MAX_RANDINT)
        print(f"Invalid input! Random number is {n}!")
    elif n.isdecimal() and int(n) < 0:
        n = randint(0, MAX_RANDINT)
        print(f"Invalid input! Random number is {n}!")
    if sum_of_digits_in_number(int(n)) > result:
        result = sum_of_digits_in_number(int(n))
        max_number = n

print(f"The max sum digits in {max_number} and equal {result}.")
