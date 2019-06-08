"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
from memory_profiler import profile
from random import random


# from sys import setrecursionlimit

# setrecursionlimit(1000)

@profile
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


@profile
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


@profile
def function():
    SIZE_OF_ARRAY = 20
    MAX_NUMBER = 50

    unsort_array = [round(random() * MAX_NUMBER, 2) for i in range(SIZE_OF_ARRAY)]

    print(f"Unsort array: {unsort_array}")
    print(f"Sort array: {merge_sort(unsort_array)}")


function()

# Python 3.7.0 OS: Windows 10 x64

# Line #    Mem usage    Increment   Line Contents
# ================================================
# 53     35.1 MiB     35.1 MiB   @profile
# 54                             def function():
# 55     35.1 MiB      0.0 MiB       SIZE_OF_ARRAY = 20
# 56     35.1 MiB      0.0 MiB       MAX_NUMBER = 50
# 57
# 58     35.1 MiB      0.0 MiB       unsort_array = [round(random() * MAX_NUMBER, 2) for i in range(SIZE_OF_ARRAY)]
# 59
# 60     35.1 MiB      0.0 MiB       print(f"Unsort array: {unsort_array}")
# 61     35.1 MiB      0.0 MiB       print(f"Sort array: {merge_sort(unsort_array)}")


# Line #    Mem usage    Increment   Line Contents
# ================================================
# 14     35.1 MiB     35.1 MiB   @profile
# 15                             def merge(left_array, right_array):
# 16     35.1 MiB      0.0 MiB       result = []
# 17
# 18     35.1 MiB      0.0 MiB       while len(left_array) > 0 and len(right_array) > 0:
# 19     35.1 MiB      0.0 MiB           if left_array[0] <= right_array[0]:
# 20     35.1 MiB      0.0 MiB               result.append(left_array[0])
# 21     35.1 MiB      0.0 MiB               left_array = left_array[1:]
# 22                                     else:
# 23     35.1 MiB      0.0 MiB               result.append(right_array[0])
# 24     35.1 MiB      0.0 MiB               right_array = right_array[1:]
# 25
# 26     35.1 MiB      0.0 MiB       while len(left_array) > 0:
# 27                                     result.append(left_array[0])
# 28                                     left_array = left_array[1:]
# 29
# 30     35.1 MiB      0.0 MiB       while len(right_array) > 0:
# 31     35.1 MiB      0.0 MiB           result.append(right_array[0])
# 32     35.1 MiB      0.0 MiB           right_array = right_array[1:]
# 33
# 34     35.1 MiB      0.0 MiB       return result


# Line #    Mem usage    Increment   Line Contents
# ================================================
# 37     35.1 MiB     35.1 MiB   @profile
# 38                             def merge_sort(array):
# 39     35.1 MiB      0.0 MiB       if len(array) <= 1:
# 40     35.1 MiB      0.0 MiB           return array
# 41                                 else:
# 42     35.1 MiB      0.0 MiB           middle = len(array) // 2
# 43     35.1 MiB      0.0 MiB           left_array = array[:middle]
# 44     35.1 MiB      0.0 MiB           right_array = array[middle:]
# 45     35.1 MiB      0.0 MiB           left_array = merge_sort(left_array)
# 46     35.1 MiB      0.0 MiB           right_array = merge_sort(right_array)
# 47
# 48     35.1 MiB      0.0 MiB           result_array = merge(left_array, right_array)
# 49
# 50     35.1 MiB      0.0 MiB           return result_array
