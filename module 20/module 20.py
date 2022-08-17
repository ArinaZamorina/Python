# Пример
# import random
# first = tuple([random.randint(0, 5) for _ in range(10)])
# second = tuple([random.randint(-5, 0) for _ in range(10)])
# third = first + second
# print(third, f'Количество нулей: {third.count(0)}', sep='\n')

# задание 1
# students = {

#     1: {

#         'name': 'Bob',

#         'surname': 'Vazovski',

#         'age': 23,

#         'interests': ['biology, swimming']

#     },

#     2: {

#         'name': 'Rob',

#         'surname': 'Stepanov',

#         'age': 24,

#         'interests': ['math', 'computer games', 'running']

#     },

#     3: {

#         'name': 'Alexander',

#         'surname': 'Krug',

#         'age': 22,

#         'interests': ['languages', 'health food']

#     }

# }


# print('Задание 1')
# for i in students:
#     print({i}, students[i]['age'])

# print('Задание 2')
# def interest_and_len(dict):
#     interest = []
#     lenght = 0
#     for i in dict:
#         interest.append(dict[i]['interests'])
#         lenght += len(dict[i]['surname'])
    
#     return interest, lenght

# int_and_len = interest_and_len(students)
# print(int_and_len)







# Задание 3
# def search_tuple(lst, symbol):
#     new_list = []
#     for indx, i in enumerate(lst):
#         if i == symbol:
#             new_list.append(indx)
#     return new_list

# some_tuple = list(tuple(input('Введите строку: ')))
# some_sym = input('Введите символ: ')
# found_tuple = search_tuple(some_tuple, some_sym)
# if len(found_tuple) == 0:
#     print(tuple())
# elif len(found_tuple) == 1:
#     print(''.join(some_tuple[found_tuple[0]:]))
# elif len(found_tuple) >= 2:
#     if len(found_tuple) == 2:
#         print(''.join(some_tuple[found_tuple[0]:found_tuple[1]]))
#     else:
#         print(''.join(some_tuple[found_tuple[-2]:found_tuple[-1]]))


# # Задание 4
# players = {

#     ("Ivan", "Volkin"): (10, 5, 13),

#     ("Bob", "Robbin"): (7, 5, 14),

#     ("Rob", "Bobbin"): (12, 8, 2)

# }

# list_players = list(i_key + i_value for i_key, i_value in players.items():
#     print(list_players)


# Задание 5
# person_dict = {('Сидоров', 'Никита'): 35,

# ('Сидорова', 'Алина'): 34,

# ('Сидоров', 'Павел'): 10}

# surname = input('Введите фамилию: ')

# for i in person_dict:
#     if surname[-1] == 'а':
#         if i[0] == surname[:-1] or i[0] == surname:
#             print(i[0])
#     else:
#         if i[0] == surname + 'а' or i[0] == surname:
#             print(i[0])



# Задание 6

# orig_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print([*map(tuple, zip(orig_list[::2], orig_list[1::2]))])

# Задание 7
# def is_int(i):
#     if i.isdecimal():
#         return True
#     else:
#         return False

# user = int(input('Введите кол-во цифр: '))
# some_list = [input() for i in range(user)]
# for i in some_list:
#     if is_int(i):
#         pass
#     else:
#         print(tuple(some_list))
#         break
# print(tuple(sorted(some_list)))

# task8

# def contact_list(user, person_dict):
#     if user == 1:
#         return add_contact(person_dict)
#     elif user == 2:
#         return search_contact(person_dict)

# def add_contact(person_dict):
#     new_contact = tuple((input('Введите ФИ: ')).split(' '))    
#     if new_contact not in person_dict:
#         person_dict[new_contact] = input('Введите номер телефона')
    
#     return person_dict

# def search_contact(person_dict):
#     contact_in_dict = input('Введите фамилия контакта: ')
#     for i in person_dict:
#         if contact_in_dict in i:
#             return i[1], person_dict[i]
#         else:
#             return None

# person_dict = {}
# while True:
#     user = int(input("Введите номер действия (1 - добавить контакт, 2 - поиск контакта)"))
#     num = contact_list(user, person_dict)
#     print(num) 