
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0.56 -> 11

input_number = float(input('Введите число: '))
str_number = str(input_number)
res = 0

for char in str_number:
    if char.isdigit():
        res += int(char)

print(f'Результат: {res}')