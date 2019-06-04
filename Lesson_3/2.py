"""
2.	Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

input_list = input("Type the list of numbers divided by spaces: ").split()
result_list = []
for pos, num in enumerate(input_list):
    if num.isdecimal():
        if int(num) % 2 == 0:
            result_list.append(pos)
            continue
        else:
            if input_list.index(num) == len(input_list) - 1:
                result_list = None

print(f"The position(s) of even number(s) in the list: {result_list}")
