'''
Требуется определить, является ли данный год високосным.

Напомним, что високосными годами считаются те годы, порядковый номер которых либо кратен 4, но при этом не кратен 100, либо кратен 400 (например, 2000-й год являлся високосным, а 2100-й будет невисокосным годом).

Программа должна корректно работать на числах 1900≤n≤3000.

Выведите "Високосный" в случае, если считанный год является високосным и "Обычный" в обратном случае (не забывайте проверять регистр выводимых программой символов).

Sample Input 1:
2100

Sample Output 1:
Обычный

Sample Input 2:
2000

Sample Output 2:
Високосный
'''

a = int(input())
b = int(400)
c = int(100)
d = int(4)

if a % b == 0:
  print('Високосный')
elif a % b != 0:
  if (a % c == 0):
    print('Обычный')
  elif(a % d == 0):
    print('Високосный')
  else:
    print('Обычный')
