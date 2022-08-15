'''
Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
В качестве ответа укажите вывод программы, а не саму программу.
Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC

Sample Output:
abc 3
'''

file_in = r'input.txt'
file_out = r'otput.txt'

# Функция чтения файла построчно в список
def ReadFile(fiename):
    str = []
    with open(fiename) as import_file:
        for line in import_file:
            str.append(line.lower().strip())
    return str

# Функция сохранения списка построчно
def SaveFile(filename, file_strings):
    with open(filename, "w") as export_file:
        for line in file_strings:
            export_file.write(line + "\n")

# Функция декомперссии (a1b8)
def UncompressString(s):
    nom = 0
    new_str = ""
    while nom < len(s):
        ch1 = str(s[nom])
        ch2 = ""
        while nom + 1 < len(s) and s[nom + 1].isdigit():
            ch2 += str(s[nom + 1])
            nom += 1
        new_str += str(ch1 * int(ch2))
        nom += 1
    return new_str

# Функция словарь пословно с количеством ('aaa': 8)
def WordCountInDict(list_in):
    dic = {}
    for line in list_in:
        list_words = line.split()
        for word in list_words:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] = dic[word] + 1
    return dic


# Функция поиск максимума по значению в словаре
def MaxInDict(dict_in):
    max_key = ""
    max_value = 0
    maximus = {}
    sorted_dict = reversed(sorted(dict_in.items(), key=lambda x: x[1]))
    dict_in = dict(sorted_dict)
    for key, val in dict_in.items():
        if len(maximus) < 1:
            maximus[key] = val

        if max_value < val:
            max_value = val
            max_key = key
        elif max_value == val:
            maximus[key] = val

    max_key = ""
    max_value = 0
    for key, value in maximus.items():
        if max_key < key:
            max_key = key

    return max_key


# Словарик
dic = {}
file_strings = ""

# Получить список
file_strings = ReadFile(file_in)

# Список в словарь
dic = WordCountInDict(file_strings)

# Максимальное значение в словаре
max_dic = MaxInDict(dic)

# Максимум в список
file_strings.clear()
file_strings.append(max_dic + " " + str(dic[max_dic]))

print(file_strings)

# Список в файл
SaveFile(file_out, file_strings)