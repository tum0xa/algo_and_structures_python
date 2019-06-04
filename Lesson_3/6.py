"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

random_list = []
for i in range(0, randint(3, 30)):
    rand_number = randint(0, 10)
    if rand_number not in random_list:
        random_list.append(rand_number)

max_element = max(random_list)
min_element = min(random_list)

pos_max = random_list.index(max_element)
pos_min = random_list.index(min_element)


if pos_max < pos_min:
    pos_max, pos_min = pos_min, pos_max

sum = 0
for i in range(pos_min + 1, pos_max):
    sum += random_list[i]

print(f"The random list is {random_list}")
print(f"The max element is {max_element} and the min element is {min_element}")
print(f"The sum of numbers beetwen them is {sum}")
