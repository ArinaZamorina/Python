""" Декоратор context manager """

"""
Для написания простого кода отдельный класс для 
контекст-менеджера потребует больше лишней возни, поэтому используем библиотеку 
и вызываем контекст-менеджер(декоратор)
"""
from contextlib import contextmanager
from collections.abc import Iterator
import functools

# данная функция оборачивает генератор в уже готовый контекст-менеджер
@contextmanager
def next_num(num: int) -> Iterator:
    print('Вход в функцию')
    try:
        yield num + 1 # без данного генератора вылетает ошибка
    except ZeroDivisionError as e:
        print('Обнаружена ошибка: {exc}'.format(exc=e))
    finally:
        print('Здесь код выполняется в любом случае')

    print('Выход из функции')

with next_num(-1) as next:
    print('Следующее число = {num}'.format(num=next))
    print(10/next)



""" Благодаря вызову конт-мен через библиотеку можно упростить задачу про время"""
import time
from contextlib import contextmanager
from collections.abc import Iterator 

@contextmanager
def timer() -> Iterator:
    start = time.time()
    try: 
        yield
    except Exception as e:
        print(e)
    finally:
        print(time.time() - start)


with timer() as t1:
    print('Первая часть')
    val_1 = 100*100*1000000
    val_1 += 'abc' # для ошибки в exit
    # еще какой-то код

with timer() as t2:
    print('Вторая часть')
    val_2 = 200*200*2000000
    # еще какой-то код

with timer() as t3:
    print('Третья часть')
    val_3 = 300*300*3000000
    # еще какой-то код


""" Как сделать так, чтобы функция возвращала время с разной точностью"""

import time
from typing import Callable, Any
from typing import Optional

"""
_func - это флаг, отвечающий был ли декоратор вызван с аргументами или без них, 
то есть все аргументы декоратора должна передаваться как именованные аргументы
для этого можем использовать специальный синтаксис *
* указывает на то, что следующие аргументы передаются по ключу
"""
def timer_with_precision(_func: Optional[Callable]=None, *, precision: int = 10) -> Callable:
    def timer_decorator(func:Callable):
        """Функция - таймер. Выводит время работы функции и возвращает ее результат"""
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            started_at = time.time()
            result = func(*args, **kwargs)
            ended_at = time.time()
            run_time = round(ended_at - started_at, precision)
            print('Функция работала {} секунд'.format(
                run_time
            ))

            return result
        return wrapped
    # return timer_decorator #если мы тут не сделаем проверку, то вылетит ошибка
    #потому что здесь мы подразумеваем, что у декоратора всегда есть аргумент
    #если аргументов нет, то нужно возвращать обычный декоратор от функции, поэтому и был введен маркер _func
    if _func is None:
        return timer_decorator
    return timer_decorator(_func)

"""
в данной ситуации мы не можем убрать скобчки, даже если мы хотим аргумент по дефолту, так как
поскольку ссылка на декорируемую функцию передаетмя на прямую только в случае, если декоратор был вызван без аргумента,
то ссылка на функцию должна быть необязательным аргументом
"""
@timer_with_precision()
def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**2 for i_num in range(10000)])

    return result

@timer_with_precision(precision=4)
def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**3 for i_num in range(10000)])

    return result


my_result = squares_sum()
print(my_result)
my_cubes_num = cubes_sum(number=200)
print(my_cubes_num)


"""Декораторы для классов"""
# Время создания объекта, когда он инициализируется в программе
# Нужно сделать так, чтобы при вызове класса, выводилось время его работы

import functools
from datetime import datetime
import time
from typing import Callable

def create_time(cls):# cls здесь, потому что мы передаем инстанс, а не функцию

    """Декоратор класса. Выводит время создания инстанса класса"""
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print('Время создания инстанса класса: {time}'.format(time=datetime.utcnow()))
        return instance
    return wrapper #возвращает инстанс

def timer_decorator(func:Callable):
    """Функция - таймер. Выводит время работы функции и возвращает ее результат"""
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at)
        print('Функция работала {} секунд'.format(
                run_time
        ))

        return result
    return wrapped
def for_all_methods(decorator: Callable) -> Callable:
    """
    Декоратор класса.
    Получает другой декоратор 
    и применяет его ко всем методам класса
    """
    @functools.wraps(decorator)
    def decorate(cls):
        """ Для получения всех методов класса в списке используется dir() """
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                # чтобы с помощью имени, взять метод класса в качестве объекта, воспользуемся getattr
                cur_method = getattr(cls, i_method)
                decorated_method = decorator(cur_method)
                #заменяем старый метод на новый 
                setattr(cls, i_method, decorated_method)  
        return cls

    return decorate

""" декораторы выполняются сверху вниз """
@create_time
@for_all_methods(timer)
class Functions:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    @timer# чтобы не прописывать везде декораторы, 
    # декорируем все с помощью собственной функции for_all_methods
    def squares_sum(self) -> int:
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num**2 for i_num in range(self.max_num)])

        return result

    @timer
    def cubes_sum(self, number: int) -> int:
    
        result = 0
        for _ in range(number + 1):
            result += sum([i_num**3 for i_num in range(self.max_num)])

        return result


my_func_1 = Functions(max_num=1000)
time.sleep(1)
my_func_2 = Functions(max_num=2000)
time.sleep(1)
my_func_3 = Functions(max_num=3000)


""" Декоратор как класс (используется крайне редко)"""

# нужно написать декоратор, который при каждом выводе функции будет выводить кол-во выводов
from typing import Callable
import functools

class CountCalls:

    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self. func)
        self.func = func
        self.num_calls = 0

    # после инициализации класса нужно сделать из него декоратор с помощью call

    def __call__(self, *args: Any, **kwds: Any) -> Callable:
        # x() == x.__call__
        self.num_calls += 1
        print('Вызов номер: {num}, функция: {func}'.format(
            num=self.num_calls, func=self.func.__name__
        ))
        return self.func(*args, **kwds)

@CountCalls
def say_hello():
    print('Hello')

say_hello()
say_hello()
print(say_hello.num_calls)
