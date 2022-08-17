"""
Lambda - функции


"""

from re import L
from typing import List

# def string_to_int(elem: str):
#     return int(elem[4:])

users: List[str] = ['user1', 'user2', 'user30', 'user3', 'user22']
# нужно сделать сортировку по номеру юзера
# print(sorted(users)) - не подойдет

# sorted_users = sorted(users, key=string_to_int)

sorted_users = sorted(users, key=lambda elem: int(elem[4:])) #лямбда функции заменяет строки 16 и 9-10
print(sorted_users)

""" 
переменным тоже можно присваивать лямбду

"""
x = lambda a: a + 10

""" 
PEP8:
" Всегда используйте оператор def вместо оператора присваивания,
который связывает лямбду непосредственоо с идентификатором "

"""

def f(x): return 2 * x #хорошо

f = lambda x: 2 * x #плохо

"""можно использовать, только если сложно придумать лаконичный pythonic way"""


"""
Плохие примеры использования lambda:

1. вызов исключения в лямбда-выражении
    def some_exception(ex): raise ex

    (lambda: some_exception(Exception('Какая-то ошибка')))()

2. Cryptonic style
    (lambda _: list(map(lambda _: _ //3, _)))([1,2,3,4,5,6,7,8,9,10])

3. Лямбда как метод класса
class Person:
    def __init__(self, name:str, age: int) -> None:
        ...

    name = property(lambda self: getattr(self, '_name'),
                    lambda self, value.setattr(self, _name, value))
"""



""" MAP """

"""
функция map возвращает итератор
map может использовать сразу несколько итерируемых объектов
если мы используем несколько итер объектов, то кол-во итераций будет = кол-во значений в минимальном итер объекте
"""

from typing import List

my_nums: List[int] = [3,1,4,1,5,9,2,6]
other_nums: List[int] = [2,7,1,8,2,8,1,8]

result: List[int] = list(map(lambda x, y: x + y, my_nums, other_nums))
print(result)


""" Функция map против list comprehensions """

#есть список
animals = ['cat', 'dog', 'cow']
#нужно 
['Cat', 'Dog', 'Cow']
#решение с map
new_animals = list(map(lambda elem: elem.capitalize(), animals))
#решение с list comprehension
new_animals = [elem.capitalize() for elem in animals]

#какой выбрать?
"""
1. map удобно использовать для ленивых вычислений
2. lambda замедляет map, но он все равно обычно быстрее list comprehensions(если выражение простое)
"""


"""Filter"""

""" принимает только один итерируемый объект и возвращает итератор"""
#нужно отобрать четные числа

result: List[int] = list(map(lambda x, y: x + y, my_nums, other_nums))
"""
filter отбирает значения по лямбде и возвращает только значения равные True
"""
result_even: List[int] = list(filter(lambda x: x % 2 == 0, result))


#можно все совместить
result = map(lambda num: num * 3, filter(lambda num: num % 2, my_nums))

#сумма всех элементов итератора
result = sum(map(lambda num: num * 3, filter(lambda num: num % 2, my_nums)))

#если на первом месте в filter будет стоять None, то у нас вернутся истинные значения
filter(None, my_nums)


"""Функциональное программирование"""

"""
Функции lambda, map, filter, zip, reduce являются элементами функционального программирования
А также создание декораторовб декораторы для сеттеров и геттеров и тд
"""




""" __name__ """

""" 
забота о безопасности нашего кода, в случае если мы хотим импортировать
функцию в другой код без вызова основного кода из импорт файла

cнимок кода в папке module30
"""




""" Пространство имен """

"""
переменная - ссылка на объект
совокупность объектов или имен образует пространство имён(namescape)

локальное пространство имён(local namespace) - это пространство имён содержит локальные имена внутри функции.
Создаётся при вызове функции и продолжается до тех пор, пока функция не вернется.

глобальное пространство имен(global namespace) - включает имена из основного кода и из различных импортируемых модулей.
существует до завершения скрипта

встроенное пространство имен (build-in namespace) - содержит встроенные функции и имена исключений
"""

def f1():
    print('Внутри f1 num =', number)

def f2():
    number = 50 #local value
    print('Внутри f2 num =', number)

def f3():
    def f4():
        # global number
        nonlocal number
        number = 10
        print('Внутри f3/f4 num =', number)

    number = 30
    print('Внутри f3 num =', number)
    f4()
    print('Внутри f3/f4 num =', number)


number = 100 #global value
print('global num =', number)
f1()
f2()
f3()
print('global num =', number)

#result:
#global num = 100
#Внутри f1 num = 100
#Внутри f2 num = 50
#Внутриf3 num = 30
#Внутри f3/f4 num = 10
#Внутри f3 num = 10
#global num = 100
