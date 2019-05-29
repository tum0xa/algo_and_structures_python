# 8.	Определить, является ли год, который ввел пользователем,
# високосным или не високосным.
#Год является високосным в двух случаях: либо он кратен 4,
# но при этом не кратен 100, либо кратен 400.

year = input("Type the year for the check: ")

if year.isdecimal() and int(year) > 0:
    year = int(year)
    if year%4 == 0 and (year%100 != 0 or year%400 == 0):
        print("It's the leap year!")
    else:
        print("It's not the leap year!")
else:
    print("Invalid input!")