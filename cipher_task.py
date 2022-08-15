'''
Дополнительная

В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили каким-то странным набором звуков.

В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру и теперь нуждаются в помощи:

Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Sample Input 1:
abcd
*d%#
abacabadaba
#*%*d*%

Sample Output 1:
*d*%*d*#*d*
dacabac

Sample Input 2:
dcba
badc
dcba
badc

Sample Output 2:
badc
dcba
'''

cipher_key = {}
cip = str(input())
decip = str(input())
i = 0

for char_1 in cip:
    cipher_key[char_1] = decip[0 + i]
    i += 1


def encryption(to_incr):
    r = ''
    for n in to_incr:
        r += str(cipher_key[n])
    return r


def decryption(to_decr):
    r = ''
    for n in to_decr:
        for key, value in cipher_key.items():
            if n == value:
                r += str(key)
    return r


to_encrypt = encryption(str(input()))
to_decrypt = decryption(str(input()))

print(to_encrypt)
print(to_decrypt)
