'''
Катя узнала, что ей для сна надо X X X минут. В отличие от Коли, Катя ложится спать после полуночи в H H H часов и M M M минут.
Помогите Кате определить, на какое время ей поставить будильник, чтобы он прозвенел ровно через X X X минут после того, как она ляжет спать.

На стандартный ввод, каждое в своей строке, подаются значения X X X, H H H и M M M.
Гарантируется, что Катя должна проснуться в тот же день, что и заснуть.
Программа должна выводить время, на которое нужно поставить будильник: в первой строке часы, во второй — минуты.

Sample Input 1:
480
1
2

Sample Output 1:
9
2

Sample Input 2:
475
1
55

Sample Output 2:
9
50

'''

ST = int(input())
GtBH = int(input()) * 60
GtBM = int(input())
a = int(GtBH + GtBM + ST)
x = int(a // 60)
y = int(a % 60)
print(x)
print(y)
