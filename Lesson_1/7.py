"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""

a = input("Type length of the first side of a triangle: ")
b = input("Type length of the second side of a triangle: ")
c = input("Type length of the third side of a triangle: ")

if a.isnumeric() and b.isnumeric() and c.isnumeric():
    a = float(a)
    b = float(b)
    c = float(c)
    if a < (b + c) and b < (a + c) and c < (a + b):
        print("Your triangle exists!")
        if a == b and b == c:
            print("Your triangle is equilateral!")
        elif a == b and b != c or a == c and c != b or b == c and c != a:
            print("Your triangle is isosceles!")
        else:
            print("Your triangle is scalene!")
    else:
        print("Your triangle does not exist!")
else:
    print("Invalid input!")
