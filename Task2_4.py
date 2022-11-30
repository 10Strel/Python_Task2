# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

N = int(input('Введите размерность списка: '))

numbers = []
for i in range(-N, N + 1):
    numbers.append(i)
print(numbers)

lst = []
flag = False
pos = 0

while not flag:
    pos = input('Введите позицию (для выхода нажмите q): ')

    if pos == 'q':
        flag = True
        break

    if (not pos.isdigit()):
       continue

    int_pos = int(pos)

    if (int_pos not in range(0, len(numbers) + 1) or (int_pos in lst)):
        continue

    lst.append(int_pos)

print(lst)

res = 1
for i in lst:
    res *= numbers[i]

print(res)