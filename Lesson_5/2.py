"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


def add_hex(a, b):
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    a = deque(a)
    b = deque(b)
    max_len = max(len(a), len(b))

    if len(a) < max_len:
        for i in range(0, max_len - len(a)):
            a.appendleft('0')
    elif len(b) < max_len:
        for i in range(0, max_len - len(b)):
            b.appendleft('0')

    a.reverse()
    b.reverse()
    ost = 0
    result = deque('')
    for i in range(0, max_len):
        tmp_sum = symbols.index(a[i]) + symbols.index(b[i]) + ost

        if tmp_sum > len(symbols) - 1:
            ost = 1
            result.appendleft(symbols[tmp_sum - len(symbols)])
        else:
            ost = 0
            result.appendleft(symbols[tmp_sum])
    if ost == 1:
        result.appendleft(symbols[ost])
    return result


def mul_hex(a, b):
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if len(a) == 1 and len(b) == 1:
        cur = 0
        high_digit = 0
        for i in range(0, symbols.index(b)):
            cur += symbols.index(a)
            if cur > len(symbols):
                high_digit += 1
                cur = cur - len(symbols)
        return deque(str(symbols[high_digit] + symbols[cur]))
    else:
        a = deque(a)
        b = deque(b)
        a.reverse()
        b.reverse()
        tmp = deque('00')
        result = deque('')
        for i in range(0, len(b)):
            for j in range(0, len(a)):
                tmp = add_hex(mul_hex(a[j], b[i]), tmp[0])
                result.append(tmp[1])
        result.append(tmp[0])
        result.reverse()
        return result


def is_hex(number='0'):
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for digit in number:
        if digit not in symbols:
            return False
    return True


# class Hexadecimal:
#
#     symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
#
#     def __init__(self, value='0'):
#         self.value = value
#         if not self._is_hex():
#             self.value = '0'
#         self.list = self._save_to_list()
#         self.hex = "0x"+self.value
#         self.int = eval(self.hex)
#
#     def _is_hex(self):
#         for symbol in self.value:
#             if symbol not in self.symbols:
#                 return False
#         return True
#
#     def _save_to_list(self):
#         sym_list = []
#         for symbol in self.value:
#             sym_list.append(symbol.upper())
#         return sym_list
#
#     def __add__(self, other):
#         return Hexadecimal(str(hex(self.int+other.int)).upper()[2:])
#
#     def __mul__(self, other):
#         return Hexadecimal(str(hex(self.int*other.int)).upper()[2:])
#
#     def __str__(self):
#         return str(self.value)
#
#
# a = Hexadecimal(input("Type the first hexadecimal number: "))
# b = Hexadecimal(input("Type the second hexadecimal number: "))
# c = a+b
# d = a*b
# print(f"The sum of them is {c}.")
# print(f"The multiplication of them is {d}.")


from collections import deque

first_number = input("Type the first hexadecimal number: ").upper()
second_number = input("Type the second hexadecimal number: ").upper()

if is_hex(first_number) and is_hex(second_number):
    print(f"The sum of them is {add_hex(first_number, second_number)}")
    print(f"The multiplication of them is {mul_hex(first_number, second_number)}")
