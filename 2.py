'''

Коля каждый день ложится спать ровно в полночь и недавно узнал, что оптимальное время для его сна составляет X X X минут.
Коля хочет поставить себе будильник так, чтобы он прозвенел ровно через X X X минут после полуночи, однако для этого необходимо указать время сигнала в формате часы, минуты.
Помогите Коле определить, на какое время завести будильник.

Часы и минуты в выводе программы должны располагаться на разных строках (см. пример работы программы)

Sample Input 1:
480

Sample Output 1:
8
0

Sample Input 2:
512

Sample Output 2:
8
32

'''

ST = int(input())
x = int(ST // 60)
y = int(ST % 60)
print(x)
print(y)
