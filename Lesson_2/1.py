"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""


# cycle


# while True:
#     operator = input("Type the operator ('0' - to exit, '+', '-', '*', '/'): ")
#     if operator == '0':
#         break
#     elif operator != '+' and operator != '-' and operator != '*' and operator != '/':
#         print("Invalid input! Try again.")
#         continue
#     else:
#         operand1 = input("Type the first operand: ")
#         operand2 = input("Type the second operand: ")
#         if operator == '/' and operand2 == '0':
#             print("Division by '0' is impossible!")
#             continue
#         elif operand1.isnumeric() and operand2.isnumeric():
#             print(f"Result: {operand1} {operator} {operand2} = {eval(operand1+operator+operand2)}")
#         else:
#             print("Invalid input! Try again.")


# recursion


def calc(operand_1='', operand_2='', operator=''):
    if operator == '':
        operator = input("Type the operator ('0' - to exit, '+', '-', '*', '/'): ")
    if operator == '0':
        return False
    elif operator not in '+-/*':
        print("Invalid input! Try again.")
        return calc()
    else:
        if operand_1 == '':
            operand_1 = input("Type the first operand: ")
        if operand_2 == '':
            operand_2 = input("Type the second operand: ")
        if operator == '/' and operand_2 == '0':
            print("Division by '0' is impossible!")
            return calc(operand_1)
        elif operand_1.isnumeric() and operand_2.isnumeric():
            print(f"Result: {operand_1} {operator} {operand_2} = {eval(operand_1 + operator + operand_2)}")
            return eval(operand_1 + operator + operand_2)
        else:
            print("Invalid input! Try again.")
            return calc()


# with user interaction
calc()

# without user interaction
print(f"1 + 2 = {calc('1', '2', '+')}")
