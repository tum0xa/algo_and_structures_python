# 5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.


from random import randint

random_list = []
for i in range(3, randint(3, 30)):
    random_list.append(randint(-10, 10))

random_list = list(set(random_list))

max_neg_number, max_neg_position = 0, 0
first_neg = False
for pos, num in enumerate(random_list):
    if num < 0 and not first_neg:
        first_neg = True
        max_neg_number = num
        max_neg_position = pos
    if num < 0 and abs(num) < abs(max_neg_number) and first_neg:
        max_neg_number = num
        max_neg_position = pos


print(f"The random list is {random_list}")
print(f"The max negative number is {max_neg_number} and its position is {max_neg_position}")
