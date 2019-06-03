"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


# recursion


def sum_of_row(num, value=1.0):
    if num > 1:
        return value + sum_of_row(num - 1, value - value * 1.5)
    else:
        return value


n = input("Type the quantity of elements in the sequence (1 -0.5 0.25 -0.125 ...): ")
if n.isdecimal():
    print(f"Sum of the sequence's elements equals to {sum_of_row(int(n))}")
else:
    print("Invalid input!")
