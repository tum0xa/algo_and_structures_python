# 4.	Определить, какое число в массиве встречается чаще всего.

from random import randint

random_list = []
for i in range(3, randint(3, 30)):
    random_list.append(randint(1, 10))

max_qnt, result_number = 0, 0
for num in random_list:
    if random_list.count(num) > max_qnt:
        max_qnt = random_list.count(num)
        result_number = num

print(f"The random list is {random_list}")
print(f"The quantity of number {result_number} is bigger then others and equal {max_qnt}")