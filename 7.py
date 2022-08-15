'''
Напишите программу, принимающую на вход целое число, которая выводит True, если переданное значение попадает в интервал (−15,12]∪(14,17)∪[19,+∞) и False в противном случае (регистр символов имеет значение).

Sample Input 1:
20

Sample Output 1:
True

Sample Input 2:
-20

Sample Output 2:
False
'''

a = int(input())

if - 15 < a <= 12:
    print(True)
elif 14 < a < 17:
    print(True)
elif 19 <= a:
    print(True)
else:
    print(False)
