"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

from random import randint

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
for pos,item in enumerate(random_array):
    if pos == m:
        print(f'"{item}"', end=' ')

    else:
        print(item, end=' ')
