# def factorial(number):
#     if number == 1:
#         return 1
#     factorial_num = number * factorial(number - 1)
#     return factorial_num

# search_fact = int(input('Введите число: '))
# result = factorial(search_fact)
# print(result)


# def power(a, n):
#     if n == 1:
#         return a
#     return a*power(a, n - 1 )
    


# float_num = float(input('Введите вещественное число: '))

# int_num = int(input('Введите степень числа: '))

# print(float_num, '**', int_num, '=', power(float_num, int_num))


# task 1
# def amount_of_number(user, start):
#     if start == user:
#         return start
#     print(start)
#     return amount_of_number(user,start + 1)


# user = int(input('Введите число: '))
# start = 0 
# print(amount_of_number(user, start))


# task 2
# first_list = ['a', 'b', 'c']
# second_list = [1, 2, 3, 4]

# if len(first_list) > len(second_list):
#     minimum = len(second_list)
# else:
#     minimum = len(first_list)

# for i in range(minimum):
#     print((first_list[i], second_list[i]))

# task 3
# def num_fib(position):
#     if position in (1, 2):
#         return 1
#     return num_fib(position - 1) + num_fib(position - 2)


# user = int(input('Введите число: '))
# print(f'Число: {num_fib(user)}')

#  task 4



# def dict_depth(d, depth=0):
#     if not isinstance(d, dict) or not d:
#         return depth
#     return max(dict_depth(v, depth+1) for k, v in d.items())


# site = {

#     'html': {

#         'head': {

#             'title': 'Мой сайт'

#         },

#         'body': {

#             'h2': 'Здесь будет мой заголовок',

#             'div': 'Тут, наверное, какой-то блок',

#             'p': 'А вот здесь новый абзац'

#         }

#     }

# }

# def search(d,user_key,level=-1):
#     if level == -1:
#         result = []
#         for k in d.keys():
#             if k == user_key:
#                result.append([d[k]])
#             if type(d[k]) is dict:
#                 result.append(search(d[k],user_key,level=-1))
#         return result
#     else:
#         if level == 0:
#             return []
#         else:
#             result = []
#             for k in d.keys():
#                 if k == user_key:
#                     result.append([d[k]])
#                 if type(d[k]) is dict:
#                     result.append(search(d[k],user_key,level-1))
#             return result
            
# print(search(site,'p'))      
# print(search(site,'p',level=3))

# task 5
# def calculating_math_func(data):
#     result = 0
#     if data in dict_fact:
#         result = dict_fact[data]
#     else:
#         result = 1
#         for index in range(1, data + 1):
#             result *= index
#         dict_fact[data] = result
#     result /= data ** 3
#     result = result ** 10

#     return result

# user = int(input('Введите число: '))
# calculator = calculating_math_func(user)
# dict_fact = {}

# task 6
# site = {

#     'html': {

#         'head': {

#             'title': 'Куплю/продам {} недорого'

#         },

#         'body': {

#             'h2': 'У нас самая низкая цена на {}',

#             'div': 'Купить',

#             'p': 'Продать'

#         }

#     }

# }

# def find_key(site, key, value):
#     if key in site:
#         site[key] = value
#         return site

#     for sub_site in site.values():
#             if isinstance(sub_site, dict):
#                 result = find_key(sub_site, key, value)
                


# count = int(input('Сколько сайтов: '))
# for _ in range(count):
#     product_name = input('Введите название продукта для нового сайта: ')
#     key = {'title': f'Куплю/продам {product_name} недорого', 'h2': f'У нас самая низкая цена на {product_name}'}
#     for i in key:
#         find_key(site, i, key[i])

#     print(f'Сайт для {product_name}:')
#     print(site, '\n')


# task 7
# def summ(*args):
#     def recurs(lst):
#         result = []
#         for i in lst:
#             if isinstance(i, int):
#                 result.append(i)
#             else:
#                 result.extend(recurs(i))
#         return result
#     return sum(recurs(args))

# user = summ([[1, 2, [3]], [1], 3])
# print(user)

# # task 8
# def summ(*args):
#     def recurs(lst):
#         result = []
#         for i in lst:
#             if isinstance(i, int):
#                 result.append(i)
#             else:
#                 result.extend(recurs(i))
#         return result
#     return (recurs(args))

# user = summ([[1, 2, [3]], [1], 3])
# print(user)