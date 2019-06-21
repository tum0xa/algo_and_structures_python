"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

input_string = input("Type a string: ")

print(f"The string '{input_string}'' has length {len(input_string)} symbols.")

result = {}
for i in range(len(input_string)):
    for j in range(len(input_string)-1 if i == 0 else len(input_string), i, -1):
        result[input_string[i:j]] = hash(input_string[i:j])

print("The quantity of substring: ", len(result))
