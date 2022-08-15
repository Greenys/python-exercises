'''
В институте биоинформатики по офису передвигается робот. Недавно студенты из группы программистов написали для него программу, по которой робот, когда заходит в комнату, считает количество программистов в ней и произносит его вслух: "n программистов".

Для того, чтобы это звучало правильно, для каждого n n n нужно использовать верное окончание слова.

Напишите программу, считывающую с пользовательского ввода целое число n n n (неотрицательное), выводящее это число в консоль вместе с правильным образом изменённым словом "программист", для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.

В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи, как минимум до 1000 человек.

Sample Input 1:
5

Sample Output 1:
5 программистов

Sample Input 2:
0

Sample Output 2:
0 программистов

Sample Input 3:
1

Sample Output 3:
1 программист

Sample Input 4:
2

Sample Output 4:
2 программиста
'''

n = int(input())

x = n % 10

if (5 <= n <= 20) or (105 <= n <= 120) or (205 <= n <= 220) or (305 <= n <= 320) or (405 <= n <= 420) or (
        505 <= n <= 520) or (605 <= n <= 620) or (705 <= n <= 720) or (805 <= n <= 820) or (905 <= n <= 920):
    print(n, 'программистов')

elif x == 1:
    print(n, 'программист')
elif 2 <= x <= 4:
    print(n, 'программиста')
elif (5 <= x <= 9) or x == 0:
    print(n, 'программистов')
else:
    print('Что-то пошло не по плану...')