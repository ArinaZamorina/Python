# task1

# count = 0 
# line_count = 0

# try:
#     with open('people.txt', 'r') as file:
#         for i in file:
#             line_count += 1
#             i = i.replace('\n', '')
#             if len(i) > 3:
#                 count += len(i)
             
# except BaseException:
#         print('Длина строки {} меньше трёх'.format(line_count))

# else:
#     print('Выполнено успешно') 
        
# print(count)


# task2
# import random

# def f(x, y):
#     x += random.randint(0, 10)
#     y += random.randint(0, 5)

#     return x / y

# def f2(x, y):
#     x -= random.randint(0, 10)
#     y -= random.randint(0, 5)

#     return y / x

# try:
#     file = open('coordinates.txt', 'r')

#     for line in file:
#         line = line.replace('\n', '')
#         nums_list = line.split(' ')
#         result_1 = f(int(nums_list[0]), int(nums_list[1]))

#         try:
#             result_2 = f2(int(nums_list[0]), int(nums_list[1]))
            
#             number = random.randint(0, 100)
#             file_2 = open('result.txt', 'w')
#             my_list = sorted([result_1, result_2, number])
#             for i in my_list:
#                 file_2.write(str(i)+'\n')

#         except Exception:
#             print("Что-то пошло не так со второй функцией")
#         finally:
#             file_2.close()

# except Exception as e:
#     print("Что-то пошло не так с первой функцией {e}")
# finally:
#     file.close()

# task3
# import random

# count = 0 
# file = open('probability.txt', 'w')

# try:
#     while count <= 777:
#         user = int(input('Введите число: '))
#         count += user
#         number = random.randint(1, 3) 
#         if number == 3:
#             raise random.choice(Exception.__subclasses__())
#         else:
#             file.write(str(user) + '\n')

# except Exception:
#         print('Ошибочка')

# finally:
#         file.close()

# print(count)

# task4

# def check_indent(line_name: str):
#     try:
#         if len(line_name.split(' ')) == 3:
#             return True
#         else:
#             raise IndexError
    
#     except IndexError:
#         return False

# def is_alpha(file): 
#     try: 
#         word_for_check = file.split(' ')[0] 
#         if word_for_check.isalpha():
#                 return True
#         else:
#             raise NameError('Ошибка в имени')
    
#     except NameError:
#         return False

# def check_email(line_file):
    
#         try:
#             ind = line_file.find('@')
#             if ind == 1:
#                 return True

#             else:
#                 raise SyntaxError
                
#         except SyntaxError:
#             return False

# def check_age(line_file):

#     try:
#         age = int(line_file.split(' ')[2])
#         if age >= 10 and age <= 99:
#             return True
#         else:
#            raise ValueError('Ошибка в почте')
    
#     except ValueError:
#         return False

# def write_into_file(result, string, line_file):
#     if result == True:
#         if line_file not in write_good_file:
#             write_good_file.write(line_file + '\n')
#         return write_good_file
#     else:
#         write_bad_file.write(line_file + '\n' + string)
#         return write_bad_file
    

# name_file = open('registrations.txt', 'r')
# write_good_file = open('registrations_good.txt', 'r+')
# write_bad_file = open('registrations_bad.txt', 'r+')
# for line_file in name_file:
#     line_file = line_file.replace('\n', '')

#     result_indent = check_indent(line_file)
#     new_note = write_into_file(result_indent, 'Ошибка в количестве полей', line_file)
#     result_letter = is_alpha(line_file)
#     new_note = write_into_file(result_letter, 'Ошибка написания', line_file)
#     result_email = check_email(line_file)  
#     new_note = write_into_file(result_email, 'Ошибка символики почты', line_file)
#     result_age = check_age(line_file)
#     new_note = write_into_file(result_age, 'Ошибка в возрасте', line_file)

# print(f'Содержимое файла write_bad_file:{write_bad_file.readline()}')
# for i in write_bad_file.readline():
#     print(i)
# print('Содержимое файла write_good_file:')
# for i in write_good_file.readline():
#     print(i)
# write_good_file.close()
# write_bad_file.close()


# task5
from io import FileIO

possible_operations = ["+", "-", "*", "/", "//", "%"]


def find_result(file_for_calc: FileIO):
    new_file = list()
    result = 0
    for i_line in file_for_calc:
        while True:
            try:
                (num1, num2, symbol) = parse_line(i_line)
                if is_correct(num1, num2, symbol):
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Строка имеет неверный формат")
                choice = input('Хотите заменить строку?')
                if choice == 'да':
                    answer = input('Введите строку:')
                    i_line = answer + "\n"

        result_expression = calculate_expression(int(num1), int(num2), symbol, result)
        print(result_expression)
        new_file.append(i_line)

        result += result_expression

    file_for_calc.seek(0)
    file_for_calc.writelines(new_file)
    file_for_calc.truncate()

    return result


def parse_line(line: str):
    list_line = line.replace('\n', '').split(' ')
    if len(list_line) == 3:
        symbol = list_line[1]
        num1, num2 = list_line[0], list_line[2]
        return num1, num2, symbol
    else:
        raise ValueError


def is_correct(num1, num2, operation):
    try:
        if operation not in possible_operations:
            raise SyntaxError

        if num2 == '0':
            raise ZeroDivisionError

        if num1.isdigit() and num2.isdigit():
            return True
        else:
            raise SyntaxError

    except SyntaxError:
        print('Ошибка в выражении')
        return False

    except ZeroDivisionError:
        print('Ошибка при делении на нуль')
        return False


def calculate_expression(num1: int, num2: int, sym, result):
    if sym == '+':
            result = num1 + num2

    elif sym == '-':
            result = num1 + num2

    elif sym == '%':
            result = num1 % num2

    elif sym == '/':
            result = num1 / num2

    elif sym == '//':
            result = num1 // num2

    elif sym == '*':
            result = num1 * num2

    return result



with open('second_calc.txt', 'r+') as file_for_calc:
    total = find_result(file_for_calc)

print('Result: {}'.format(
    total
    )
)




# task 6
# username = input('Введите имя: ')

# while True:

#     action = input('Прочитать или посмотреть сообщение: ')

#     if action == '0':

#         try:
#             with open('chat.txt', 'r', encoding='utf-8') as file:
#                 for i_line in file:
#                     print(i_line, end='')
#         except FileNotFoundError:
#             print('Сообщений нет. \n')

#     elif action == '1':
#         message = input('Введите сообщение: ')
#         with open('chat.txt', 'a', encoding='utf-8') as file:
#             file.write(f' { username } : { message } \n')
#     else:
#         print('Такой команды нет')
