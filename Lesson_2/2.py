"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


# recursion

def get_cnt_odd_even(natural_number, cnt_even=0, cnt_odd=0):
    """

    :param natural_number: Input natural_number
    :param cnt_even: Counter for even digits
    :param cnt_odd: Counter for odd digits
    :return: Quantity of even and odd digit in the number
    """
    if natural_number % 2 == 0:
        cnt_even += 1
    else:
        cnt_odd += 1
    natural_number = natural_number // 10
    if natural_number < 1:
        return cnt_even, cnt_odd
    else:
        return get_cnt_odd_even(natural_number, cnt_even, cnt_odd)


num = input("Type the natural number: ")

if num.isdecimal() and int(num) > 0:
    cnt_even, cnt_odd = get_cnt_odd_even(int(num))
    print(f"Your number {num} has {cnt_even} even digit(s) and {cnt_odd} odd digit(s)")
else:
    print("Invalid input! Only a natural numbers allowed.")

