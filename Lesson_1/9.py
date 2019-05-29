# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

first_number = input("Type the first number: ")
second_number = input("Type the second number: ")
third_number = input("Type the third number: ")

if first_number.isnumeric() and second_number.isnumeric() and third_number.isnumeric():
    if second_number < first_number < third_number or second_number > first_number > third_number:
        print(f"{first_number} is average number!")
    elif first_number < second_number < third_number or first_number > second_number > third_number:
        print(f"{second_number} is average number!")
    elif first_number < third_number < second_number or first_number > third_number > second_number:
        print(f"{third_number} is average number!")
else:
    print("Invalid input!")
