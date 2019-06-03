"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


# recursion


def invert_number(num):
    """

    :param num: Number that will be inverted
    :return: Inverted number
    """
    if int(num) != 0:
        return num % 10 * (10 ** (len(str(num)) - 1)) + invert_number(num // 10)
    else:
        return False


n = input("Type a number: ")
if n.isdecimal() and int(n) > 0:
    print(f"Your reverse number is {invert_number(int(n))}.")
else:
    print("Invalid input!")
