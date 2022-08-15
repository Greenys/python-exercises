'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое последнего файла из набора, как ответ на это задание.
'''

import requests

link = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open('Start.txt') as inf:
    t = inf.readline().strip()

t = str(requests.get(t).text)
while 'we' not in t:
    print(t)
    t = requests.get(link + t).text
print(t)
