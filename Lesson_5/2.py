"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


class Hexadecimal:
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    def __init__(self, value='0'):
        self.value = value
        if not self._is_hex():
            self.value = '0'
        self.list = self._save_to_list()
        self.hex = "0x" + self.value
        self.int = eval(self.hex)

    def _is_hex(self):
        for symbol in self.value:
            if symbol not in self.symbols:
                return False
        return True

    def _save_to_list(self):
        sym_list = []
        for symbol in self.value:
            sym_list.append(symbol.upper())
        return sym_list

    def __add__(self, other):
        return Hexadecimal(str(hex(self.int + other.int)).upper()[2:])

    def __mul__(self, other):
        return Hexadecimal(str(hex(self.int * other.int)).upper()[2:])

    def __str__(self):
        return str(self.value)


a = Hexadecimal(input("Type the first hexadecimal number: "))
b = Hexadecimal(input("Type the second hexadecimal number: "))
c = a + b
d = a * b
print(f"The sum of them is {c}.")
print(f"The multiplication of them is {d}.")
