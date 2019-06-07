"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

from random import random


# from sys import setrecursionlimit

# setrecursionlimit(1000)


def merge(left_array, right_array):
    result = []

    while len(left_array) > 0 and len(right_array) > 0:
        if left_array[0] <= right_array[0]:
            result.append(left_array[0])
            left_array = left_array[1:]
        else:
            result.append(right_array[0])
            right_array = right_array[1:]

    while len(left_array) > 0:
        result.append(left_array[0])
        left_array = left_array[1:]

    while len(right_array) > 0:
        result.append(right_array[0])
        right_array = right_array[1:]

    return result


def merge_sort(array):

    if len(array) <= 1:
        return array
    else:
        middle = len(array) // 2
        left_array = array[:middle]
        right_array = array[middle:]
        left_array = merge_sort(left_array)
        right_array = merge_sort(right_array)

        result_array = merge(left_array, right_array)

        return result_array


SIZE_OF_ARRAY = 20
MAX_NUMBER = 50

unsort_array = [round(random() * MAX_NUMBER, 2) for i in range(SIZE_OF_ARRAY)]

print(f"Unsort array: {unsort_array}")
print(f"Sort array: {merge_sort(unsort_array)}")
