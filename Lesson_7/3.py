"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
from memory_profiler import profile
from random import randint


@profile
def function():
    m = 5

    random_array = [randint(0, 100) for _ in range(2 * m + 1)]

    print(f"The array is: {random_array}")

    median = 0
    for num in random_array:
        greater = 0
        less = 0
        for i in range(len(random_array)):
            if num > random_array[i]:
                greater += 1
            if num < random_array[i]:
                less += 1
            if num == random_array[i]:
                continue

            if greater > m or less > m:
                break

        # print(num, greater, less)

        if greater == m or less == m:
            median = num

    print(f"Your median is {median}!")

    # Выводим отсортированный массив с выделенной медианой для наглядности
    random_array.sort()
    for pos, item in enumerate(random_array):
        if pos == m:
            print(f'"{item}"', end=' ')

        else:
            print(item, end=' ')


function()

# Line #    Mem usage    Increment   Line Contents
# ================================================
# 12     35.1 MiB     35.1 MiB   @profile
# 13                             def function():
# 14     35.1 MiB      0.0 MiB       m = 5
# 15
# 16     35.1 MiB      0.0 MiB       random_array = [randint(0, 100) for _ in range(2 * m + 1)]
# 17
# 18     35.1 MiB      0.0 MiB       print(f"The array is: {random_array}")
# 19
# 20     35.1 MiB      0.0 MiB       median = 0
# 21     35.1 MiB      0.0 MiB       for num in random_array:
# 22     35.1 MiB      0.0 MiB           greater = 0
# 23     35.1 MiB      0.0 MiB           less = 0
# 24     35.1 MiB      0.0 MiB           for i in range(len(random_array)):
# 25     35.1 MiB      0.0 MiB               if num > random_array[i]:
# 26     35.1 MiB      0.0 MiB                   greater += 1
# 27     35.1 MiB      0.0 MiB               if num < random_array[i]:
# 28     35.1 MiB      0.0 MiB                   less += 1
# 29     35.1 MiB      0.0 MiB               if num == random_array[i]:
# 30     35.1 MiB      0.0 MiB                   continue
# 31
# 32     35.1 MiB      0.0 MiB               if greater > m or less > m:
# 33     35.1 MiB      0.0 MiB                   break
# 34
# 35                                     # print(num, greater, less)
# 36
# 37     35.1 MiB      0.0 MiB           if greater == m or less == m:
# 38     35.1 MiB      0.0 MiB               median = num
# 39
# 40     35.1 MiB      0.0 MiB       print(f"Your median is {median}!")
# 41
# 42                                 # Выводим отсортированный массив с выделенной медианой для наглядности
# 43     35.1 MiB      0.0 MiB       random_array.sort()
# 44     35.1 MiB      0.0 MiB       for pos,item in enumerate(random_array):
# 45     35.1 MiB      0.0 MiB           if pos == m:
# 46     35.1 MiB      0.0 MiB               print(f'"{item}"', end=' ')
# 47
# 48                                     else:
# 49     35.1 MiB      0.0 MiB               print(item, end=' ')
