'''
Напишите программу, которая подключает модуль math и, используя значение числа π \pi π из этого модуля, находит для переданного ей на стандартный ввод радиуса круга периметр этого круга и выводит его на стандартный вывод.

Sample Input:
10.0

Sample Output:
62.83185307179586
'''

import math

print(2 * float(input()) * math.pi)
