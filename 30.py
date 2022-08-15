'''


Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два.
Функция не должна ничего возвращать, требуется только изменение переданного списка, например:

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]

Функция не должна осуществлять ввод/вывод информации.
'''

def modify_list(l):
    cnt = cnt_1 = 0
    while cnt < len(l):
        for i in l:
            if l[cnt] % 2 != 0:
                del l[cnt]
                break
            elif i % 2 == 0:
                cnt +=1
                break
    for j in l:
        if j % 2 == 0:
            l[cnt_1] = j // 2
            cnt_1 +=1
