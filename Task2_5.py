# Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint

from random import randint

lst = [10, 3, 5, 67, 89, 11, 4, 1, 55, 34]
print (lst)

tmp_lst = lst[:]

for i in range(len(tmp_lst)):        
    index = randint(0, len(tmp_lst) - 1)    
    temp = tmp_lst[i]
    tmp_lst[i] = tmp_lst[index]
    tmp_lst[index] = temp

print(tmp_lst)
