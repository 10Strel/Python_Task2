# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# Запрещено использовать функцию factorial из библиотеки math


def func(n):
    if n < 1:
        return 1
    else:
        res = n * func(n - 1)
        lst.append(res)
        return res


input_number = int(input('Введите число: '))
lst = []

func(input_number)
print(lst)