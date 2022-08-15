'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число n n n — количество завершенных игр.
После этого идет n n n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15

Sample Output:
Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
'''
import itertools

# Variables
main_list = [input().split(';') for x in range(int(input()))]
game = [(i[0], i[2]) for i in main_list]
total_games, win, draw, lose, total_points = 0, 1, 2, 3, 4

teams = set(itertools.chain.from_iterable(game))
result = {club: [0, 0, 0, 0, 0] for club in teams}
for team_1, goal_1, team_2, goal_2 in main_list:
    result[team_1][total_games] += 1
    result[team_2][total_games] += 1
    if int(goal_1) > int(goal_2):
        result[team_1][win] += 1
        result[team_1][total_points] += 3
        result[team_2][lose] += 1
    elif int(goal_1) < int(goal_2):
        result[team_2][win] += 1
        result[team_2][total_points] += 3
        result[team_1][lose] += 1
    elif int(goal_1) == int(goal_2):
        result[team_1][draw] += 1
        result[team_1][total_points] += 1
        result[team_2][draw] += 1
        result[team_2][total_points] += 1
for team in teams:
    print('{}:{}'.format(team, ' '.join(map(str, result[team]))))
