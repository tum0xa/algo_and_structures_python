"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

from random import randint

MAX_RANDOM_NUMBER = 100
MATRIX_SIZE = 4


def sum_of_row(in_row):
    result = 0
    for num in in_row:
        result += num
    return result


matrix = [[] for _ in range(4)]

print(f"Type the matrix {MATRIX_SIZE}x{MATRIX_SIZE}:")

for i in range(4):
    raw_row = input().split()
    int_row = []
    for el in raw_row:
        if el.isdecimal():
            int_row.append(int(el))
        else:
            int_row.append(randint(0, MAX_RANDOM_NUMBER))

    if len(int_row) < MATRIX_SIZE:
        while len(int_row) != MATRIX_SIZE:
            int_row.append(randint(0, MAX_RANDOM_NUMBER))
    elif len(int_row) > MATRIX_SIZE:
        int_row = int_row[:MATRIX_SIZE]

    int_row.append(sum_of_row(int_row))

    matrix[i] = int_row

for row in matrix:
    for i, col in enumerate(row):
        if i == (len(row) - 1):
            print(f"{col}")
        else:
            print(f"{col}", end=' ')
