# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

result = 0
result_dict = {}
for i in range(2, 10):
    result_dict[i] = 0

for num in range(2, 100):
    for dig in range(2, 10):
        if num % dig == 0:
            result_dict[dig] += 1

for num, qnt in result_dict.items():
    print(f"{qnt} numbers is multiple of {num}.")
