# Аня — координатор стажировок в Тинькофф. Она хочет нанять самых сильных олимпиадников.

# Для того чтобы понять, кто же лучший, Аня решила проанализировать результаты командной олимпиады за последние ﻿﻿NN﻿﻿ лет. Она знает все команды, занявшие первое место. Каждая команда задается тройкой имен, причем их порядок не важен, то есть записи ANTON BORIS CHRIS и BORIS ANTON CHRIS задают одну и ту же команду.

# Ане нужны лучшие из лучших, поэтому она хочет знать, какое максимальное число раз побеждала команда в одном и том же составе. Вы дружите с Аней, поэтому согласились ей помочь. 



# Формат входных данных

# В первой строке задано одно целое число ﻿﻿NN﻿﻿ ﻿﻿(1 \leq N \leq 10^3)(1≤N≤10 
# 3
#  )﻿﻿ — количество лет, за которые у Ани есть данные.

# В следующих ﻿﻿NN﻿﻿ строках заданы команды-победители: в каждой строке указаны три разделенных пробелом имени. Каждое имя имеет длину от ﻿﻿11﻿﻿ до ﻿﻿1010﻿﻿ символов, а также состоит из заглавных латинских символов ﻿﻿(A, ..., Z)(A,...,Z)﻿﻿.



# Формат выходных данных

# В единственной строке выведите число — максимальное число побед команды в одинаковом составе.
# def sortByAlphabet(list):
#     for i in list:
#         return i[0]

# teams = int(input())
# teams_list = []
# for i in range(teams):
#     player = (input('Введите игроков: ')).split(' ')
#     teams_list.append(player)

# new_list = [] 
# for i in teams_list:
#     i.sort(key=sortByAlphabet)
#     if i not in new_list:
#         new_list.append(i)

# print(len(new_list))


dictionary = {}
flag = False
with open("D:\Soft\Skillbox\тинькофф\prog.txt", 'r') as text:
    for i in text:
        i = i.replace('\n', '').split('=')
        if i[0] != '{' and i[0] != '}':
            if i[0] not in dictionary:
                if i[1] not in dictionary and i[1].isalpha():
                    dictionary[i[0]] = 0
                    print(dictionary[i[0]])
                else:
                    if i[1] in dictionary and i[1].isalpha():
                        dictionary[i[0]] = dictionary[i[1]]
                        print(dictionary[i[0]])
                    if i[1] not in dictionary and i[1].isdigit():
                        dictionary[i[0]] = i[1]

            else:
                if i[1] in dictionary or i[1].isdigit():
                    dictionary[i[0]] = i[1]
                    print(dictionary[i[0]])
                else: pass

        
        else:
            dictionary[i[0]] = dict()
