# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

in_number = int(input("Type a positive three digit number, please: "))

if in_number > 999 or in_number < 100:
    print("Invalid input!")
    quit()

first_digit = in_number % 10
# print(f'First digit is {first_digit}')
last_digit = int(in_number / 100)
# print(f'Last digit is {last_digit}')
middle_digit = int((in_number - last_digit * 100) / 10)
# print(f'Middle digit is {middle_digit}')

print(f'Sum of three digits of the number equal {first_digit + last_digit + middle_digit}')
print(f'and multiplication of three digits of the number equal {first_digit * last_digit * middle_digit}')
