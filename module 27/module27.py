# Функция как объект. Функция высшего порядка
# метод time
import time
from typing import Callable, Any

def timer(func:Callable, *args, **kwargs):
    """Функция - таймер. Выводит время работы функции и возвращает ее результат"""
    started_at = time.time()
    result = func(*args, **kwargs)
    ended_at = time.time()
    run_time = round(ended_at - started_at, 4)
    print('Функция работала {} секунд'.format(
        run_time
    ))

    return result

def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**2 for i_num in range(10000)])

    return result


def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**3 for i_num in range(10000)])

    return result


my_result = timer(squares_sum)
print(my_result)
my_cubes_num = timer(cubes_sum, 200)
print(my_cubes_num)


# декоратор
# декорируем функцию func с помощью функции timer
# декотратор заворачивает исходную функцию в код, который нам потребуется

import time
from typing import Callable, Any

def timer(func:Callable) -> Callable:
    """Декоратор. Выводит время, которое заняло выполнение декорируемой функции """
    
    def wrapped_func(*args, **kwargs) -> Any: # аргументы декорируемой функции передаются в функцию обертки,
        # после чего с ними можно делать, что угодно
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 4)
        print('Функция работала {} секунд'.format(
            run_time
        ))

        return result
    return wrapped_func # возращаем готовую функцию, которой можно пользоваться

@timer # обернули функцию squares_sum, то есть можно убрать постоянное переприсваивание на строке 82 и 83 и 87-88
def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**2 for i_num in range(10000)])

    return result

@timer
def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**3 for i_num in range(10000)])

    return result


# new_squares_sum = timer(squares_sum)
# my_sum = new_squares_sum()
my_sum = squares_sum()
print(my_sum)

# new_cubes_sum = timer(cubes_sum)
# my_cubes_sum = new_cubes_sum(200)
my_cubes_sum = cubes_sum(200)
print(my_cubes_sum)



# Модель декоратора
def decorator(func):
    def wrapped_func(*args, **kwargs):
        # код до вызова функции
        value = func(*args, **kwargs)
        # код после вызова функции
        return value
    return wrapped_func

@decorator
def some_function(*args):
    pass
# ! отладка декоратора затруднительна !



# логирование

import time
from typing import Callable, Any

def timer(func:Callable) -> Callable:
    """Декоратор. Выводит время, которое заняло выполнение декорируемой функции """
    
    def wrapped_func(*args, **kwargs) -> Any: 
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 4)
        print('Функция работала {} секунд'.format(
            run_time
        ))

        return result
    return wrapped_func 

def logging(func: Callable) -> Callable:
    def timer(func:Callable) -> Callable:
        """Декоратор, логирующий работу кода"""
        
        def wrapped_func(*args, **kwargs) -> Any: 
            print('\n Вызывается функция {func}\t'
            'Позиционные аргументы: {args}\t'
            'Именованные аргументы: {kwargs}'.format(
                func=func.__name__, args=args,kwargs=kwargs
            ))
            result = func(*args, **kwargs)
            print('Функция успешно завершила работу')
            return result
        return wrapped_func 

@logging
@timer 
def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**2 for i_num in range(10000)])

    return result

@logging
@timer
def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**3 for i_num in range(10000)])

    return result


my_sum = squares_sum()
print(my_sum)

my_cubes_sum = cubes_sum(200)
print(my_cubes_sum)

# особенности использования декораторов
# не всегда декораторы должны оборачивать функцию

from typing import Callable, Dict

PLUGINS: Dict = dict()

def register(func: Callable) -> Callable:
    """Декоратор. Регистрирует функции как плагин"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name:str) -> str:
    return "Hello {name}!".format(name=name)

@register
def say_goodbye(name:str) -> str:
    return "Goodbye {name}!".format(name=name)

print(PLUGINS)
print(say_hello('Tom'))


# модуль functools. декоратор funtools.wraps()
import time
import functools
from typing import Callable, Any

def timer(func:Callable) -> Callable:
    """Декоратор. Выводит время, которое заняло выполнение декорируемой функции """
    
    @functools.wraps(func) # мы приписываем нашей обертке методы, которые указаны у нашей функции
    def wrapped_func(*args, **kwargs) -> Any: # аргументы декорируемой функции передаются в функцию обертки,
        # после чего с ними можно делать, что угодно
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 4)
        print('Функция работала {} секунд'.format(
            run_time
        ))

        return result
    return wrapped_func # возращаем готовую функцию, которой можно пользоваться

@timer
def squares_sum() -> int:
    """
    Функция нахождения суммы квадратов
    для каждого N от 0 до 10000,
    где 0 <= N <= 10000,

    :return: сумма квадратов
    """
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**2 for i_num in range(10000)])

    return result

@timer
def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**3 for i_num in range(10000)])

    return result


print(squares_sum.__doc__) #без functools.wraps(func) у нас выводится None 
print(squares_sum.__name__) # а тут wrapped_func