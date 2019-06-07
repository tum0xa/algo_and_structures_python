"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

from random import randint


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
