# 3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.


from random import randint

random_list = []
for i in range(3, randint(3, 20)):
    random_list.append(randint(1, 100))

random_list = list(set(random_list))

big, small = 0, 0
for pos, num in enumerate(random_list):
    if num < small or pos == 0:
        small = num
    if num > big:
        big = num

result_list = random_list.copy()
result_list[random_list.index(big)], result_list[random_list.index(small)] = \
    result_list[random_list.index(small)], result_list[random_list.index(big)]

print(f"The biggest number is {big} and the smaller is {small}")
print(f"The original random list is {random_list}")
print(f"The result list is {result_list}")
