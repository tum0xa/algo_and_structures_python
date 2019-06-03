"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


# recursion

def sum_of_num(num):
    if num == 0:
        return 0
    else:
        return num + sum_of_num(num - 1)


n = input("Type a natural number: ")
if n.isdecimal() and int(n) > 0:
    n = int(n)
    if sum_of_num(n) == n * (n + 1) / 2:
        print(f"The equality 1+2+...+{n} = {n}*({n}+1)/2 is fulfilled!")
else:
    print("Invalid input")
