# task 1
# number_file = open('number.txt', 'r')
# data = number_file.read().replace(' ', '').replace('\n', '')
# count = 0 
# for i in data:
#     if isinstance(int(i), int):
#         count += int(i)
# print(count)

# task 2

# zen_file = open('zen.txt', 'r')
# list_data = zen_file.readlines()
# list_data[-1] += '\n'
# list_data.reverse()
# print(''.join(list_data))

# task 3

# def search_letter(name_file):
#     data = open(name_file, 'r')
#     count = 0
#     for i in data:
#         i = i.rstrip()
#         for j in i:
#             if j.isalpha():
#                 count += 1
#     data.close()
#     return count

# def search_line(name_file):
#     data = open(name_file, 'r')
#     count = 0
#     for i in data.readlines():
#         if i != '\n':
#             count+=1
#     data.close()
#     return count

# def search_words(name_file):
#     marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_'''
#     data = open(name_file, 'r')
#     count = 0
#     for i in data:
#         i = i.replace('\n', '')
#         for j in i.split(' '):
#             count +=1
#             for x in j:
#                 if x in marks:
#                     i = i.replace(x, '')
        
#     data.close()
#     return count

# zen_file = open('zen.txt', 'r')
# words = search_words('zen.txt')
# line = search_line('zen.txt')
# letter = search_letter('zen.txt')
# print(words)
# print(line)
# print(letter)

# task 4
# import os

# def get_size(start_path = '.'):
#     total_size = 0
#     for dirpath, dirnames, filenames in os.walk(start_path):
#         for i in filenames:
#             fp = os.path.join(dirpath, i)
#             total_size += os.path.getsize(fp)
#     return total_size

# path = os.getcwd()
# count_file = len([i for i in os.listdir(path) if os.path.isfile(i)])
# size_dir = get_size(path)

# print(f'{path} {count_file} {size_dir}', end = '')

# task 5
# import os

# def find(name, path):
#     for root, dirs, files in os.walk(path):
#         if name in files:
#             return os.path.join(root, name)
#         else:
#             write_file = open(name, 'w')
#             write_file.close()
#             return os.path.join(root, write_file)


# def save_str(text, path):
#     if os.path.getsize(path) == 0:
#         write_file = open(path, 'r+')
#         write_file.write(text)

#     else:
#         user = input('Перезаписать? ')
#         if user == 'да':
#             write_file = open(path, 'r+')
#             write_file.write(text)
#             write_file.read()
#         else:
#             pass
        
#     return write_file

        


# text = input('Введите строку: ')
# path = input('Введите путь до папки: ')
# file_txt = input('Введите имя файла: ')
# file = find(file_txt, path)
# saving = save_str(text, path)
# for i in saving.read():
#     print(i)


# task 6
 
def search_line(data):
    data = open('file.txt', 'r')
    count = 0
    for i in data.readlines():
        i = i.replace('\n', '')
        count+=1
    data.close()
    return count

str_alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'


search = search_line('file.txt')
open_file = open('file.txt', 'r')
for i in range(1, search + 1):
    for f in open_file.readline(i):
        string = ''
        for j in f: 
            for a in str_alf:
                if j == a:
                    ind = str_alf.index(a) + 1
                    string += str_alf[ind]
                else:
                    pass
        print(string)



# task 7

# count = 1
# file_write = open('second_tour.txt','r+')
# for linenum,line in enumerate(open('first_tour.txt','r+')):
#     line = line.replace('\n', '')
#     if linenum == 0 and int(line):
#         with open('second_tour.txt', 'w') as file:
#             file_write.write(line + '\n')
#             save_line = int(line)
#     else:
#         count += 1

# new_list = []
# num_list = []

# file_read = open('first_tour.txt','r+')
# for i in file_read.readlines()[1:]:
#     if int(((i.replace('\n', '')).split(' '))[-1]) >= save_line:
#         new_list.append(i.replace('\n', ''))
#         num_list.append(int((i.split(' '))[-1]))
# num_list.sort()

# sorted_list = [i for j in num_list for i in new_list  if str(j) in i.split(' ')]
# for i in sorted_list:
#     file_write.write(i + '\n') 


# task 8
# import re
# def search_count(file):
#     dict_sym = {}
#     for i in open(file, 'r'):
#         for j in i.lower():
#             if j.isalpha():
#                 if j not in dict_sym:
#                     dict_sym[j] = 1
#                 else:
#                     for key, value in dict_sym.items():
#                         if key == j:
#                             value += 1
#                             dict_sym[key] = value

#     return dict_sym

# def sorted_values(search_dict):
#     sorted_values = sorted(search_dict.values()) 
#     sorted_dict = {}

#     for i in sorted_values:
#         for k in search_dict.keys():
#             if search_dict[k] == i:
#                 sorted_dict[k] = search_dict[k]
#                 break
#     return sorted_dict

# marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_'''
# open_file = open('string.txt', 'r')
# for i in open_file:    
#     string = re.sub(r'[^\w\s]','', i)
#     string = string.replace(' ', '')
# lenght = len(string)
# open_file.close()


# search_dict = search_count('string.txt')


# for key, value in search_dict.items():
#     search_dict[key] = value/lenght

# sort_dict = sorted_values(search_dict)
# print(sort_dict)