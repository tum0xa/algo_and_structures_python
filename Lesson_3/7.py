"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import randint

random_list = []
for i in range(0, randint(3, 30)):
    rand_number = randint(0, 10)
    # if rand_number not in random_list:
    random_list.append(rand_number)

min_1 = 0
min_2 = 0

for pos, num in enumerate(random_list):
    if pos == 0:
        min_1 = num
    # elif min_2 < min_1 < num:
    #     min_2 = num
    elif num < min_1:
        min_2 = min_1
        min_1 = num
    elif min_1 < num < min_2:
        min_2 = num
    elif min_1 >= min_2 and num > min_2:
        min_2 = num



print(random_list)
print(f"Min 1: {min_1}\nMin 2: {min_2}")
