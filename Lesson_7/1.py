"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
from memory_profiler import profile
from random import randint

@profile
def bubble_sort(array):
    step = 0

    while step < len(array):
        exchange = False
        for i in range(len(array) - step):
            if i < len(array) - step - 1:
                if array[i] > array[i + 1]:
                    array[i + 1], array[i] = array[i], array[i + 1]
                    exchange = True
        if not exchange:
            break
        else:
            step += 1
    # print(f"Quantity of a sort steps: {step}")
    return array


SIZE_OF_ARRAY = 50

unsort_array = [randint(-100, 100) for i in range(SIZE_OF_ARRAY)]

print(f"Unsort array: {unsort_array}")
print(f"Sort array: {bubble_sort(unsort_array)}")


# Line #    Mem usage    Increment   Line Contents
# ================================================
# 10     35.5 MiB     35.5 MiB   @profile
# 11                             def bubble_sort(array):
# 12     35.5 MiB      0.0 MiB       step = 0
# 13
# 14     35.5 MiB      0.0 MiB       while step < len(array):
# 15     35.5 MiB      0.0 MiB           exchange = False
# 16     35.5 MiB      0.0 MiB           for i in range(len(array) - step):
# 17     35.5 MiB      0.0 MiB               if i < len(array) - step - 1:
# 18     35.5 MiB      0.0 MiB                   if array[i] > array[i + 1]:
# 19     35.5 MiB      0.0 MiB                       array[i + 1], array[i] = array[i], array[i + 1]
# 20     35.5 MiB      0.0 MiB                       exchange = True
# 21     35.5 MiB      0.0 MiB           if not exchange:
# 22     35.5 MiB      0.0 MiB               break
# 23                                     else:
# 24     35.5 MiB      0.0 MiB               step += 1
# 25                                 # print(f"Quantity of a sort steps: {step}")
# 26     35.5 MiB      0.0 MiB       return array
