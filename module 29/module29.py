# Реализуйте функцию (не класс) timer в качестве контекст-менеджера: 
# функция должна работать с оператором with и замерять время работы вложенного кода.

# from contextlib import contextmanager
# import time

# @contextmanager
# def timer():
#     start = time.time()
#     try:
#         yield
#     except Exception as e:
#         print('Error: {exc}'.format(exc=e))
#     finally:
#         print(time.time() - start)


# with timer() as time1:
#     print('Первая часть')
#     num = 1**10*100

# with timer() as time2:
#     print('Вторая часть')
#     num = 1*100*1000*10
#     num += 'abc'

# task1
# import functools
# from typing import Callable


# def check_permission(user_name: str) -> Callable:
#     user_permissions = ['admin']

#     def checking(func: Callable) -> Callable:

#         @functools.wraps(func)
#         def wrapper(*args, **kwargs) -> Callable:
#             try:
#                 if user_name in user_permissions:
#                     return func(*args, **kwargs)
#                 else:
#                     raise PermissionError
#             except PermissionError as per:
#                 print('{perm}: пользователь не имеет прав для выполнения функции {func_name}'.format(
#                     perm=per, func_name=func.__name__
#                     ))
#         return wrapper
#     return checking

# @check_permission('admin')
# def delete_site():
#     print('Удаляем сайт')


# @check_permission('user_1')
# def add_comment():
#     print('Добавляем комментарий')

# delete_site()
# add_comment()


# task2
# from typing import Callable, Optional
# import functools
 
# app = dict()
 
 
# def callback(_func: Optional[Callable] = None, *, route: str = None) -> Callable:
#     def decorator_callback(name_func: Callable) -> Callable:
#         """ Декоратор функции обратного вызова """
#         app[route] = name_func
 
#         @functools.wraps(name_func)
#         def wrapper(*args, **kwargs):
#             func_call = name_func(*args, **kwargs)
#             return func_call
#         return wrapper
#     if _func is None:
#         return decorator_callback
#     return decorator_callback(_func)
 
 
# @callback(route='//')
# def example() -> str:
#     print('Пример функции, которая возвращает ответ сервера')
#     return 'OK'
 
 
# route = app.get('//')
# if route:
#     response = route()
#     print('Ответ:', response)
# else:
#     print('Такого пути нет')
 
# print(app)



# task3
import time
from datetime import datetime
from typing import Callable
 
 
def timer(cls, func, date_format):
    def wrapped(*args, **kwargs):
        format = date_format
        for letter in format:
            if letter.isalpha():
                format = format.replace(letter, '%' + letter)
 
        print(f"Запускается '{cls.__name__}.{func.__name__}'. Дата и время запуска: {datetime.now().strftime(format)}")
        start = time.time()
        result = func(*args, **kwargs)                                  
        end = time.time()
        print(f"Завершение '{cls.__name__}.{func.__name__}', время работы = {round(end - start, 3)} сек.")
        return result
 
    return wrapped
 
 
def log_methods(date_format):
    def decorate(cls):
        for method in dir(cls):
            if not method.startswith('__'):
                current_method = getattr(cls, method)
                decorated_method = timer(cls, current_method, date_format)
                setattr(cls, method, decorated_method)
        return cls
 
    return decorate
 
 
@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
 
        return result
 
 
@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")
 
    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
 
        return result
 
 
my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()


# task4
# from typing import Callable 

# def decorator_with_args_for_any_decorator(decorator_example):
#     """
#     Эта функция задумывается как декоратор и для декораторов.
#     Она должна декорировать другую функцию, которая должна быть декоратором.
#     Она даёт возможность любому декоратору принимать произвольные аргументы
#     """

#     def maked_decorator(*args, **kwargs):

#         def wrapper(func):
#             """
#             decorator(func, *args, **kwargs) - модель декоратора по данным условиям
#             """
#             return decorator_example(func, *args, **kwargs)
#         return wrapper
#     return maked_decorator



# @decorator_with_args_for_any_decorator
# def decorated_decorator(func: Callable, *args, **kwargs):
#     def wrapper(arg1, arg2):
#         print('Args: {}, {}'.format(arg1, arg2))
#         return func(arg1,arg2)
#     return wrapper


# @decorated_decorator(100, 'рублей', 200, 'друзей')
# def decorated_function(text: str, num: int) -> None:
#     print("Привет", text, num)


# decorated_function("Юзер", 101)


# task5
# import functools

# def singleton(cls):
    #   """для cls анотация типов не используется"""
#     """из класса в одноэлементный класс"""
#     @functools.wraps(cls)
#     def wrapper(*args, **kwargs):
#         if not wrapper.instance:
#             wrapper.instance = cls(*args, **kwargs)
#         return wrapper.instance
#     wrapper.instance = None
#     return wrapper

# @singleton
# class Example:
#     pass

# my_obj = Example()
# my_another_obj = Example()


# print(id(my_obj))
# print(id(my_another_obj))


# print(my_obj is my_another_obj)


# decorator for decorator
import functools
from typing import Callable

def decorator_with_args_for_any_decorator(decorator_to_enhance: Callable) -> Callable:
    """Декоратор. Дает возможность другому декоратору принимать произвольныее аргументы """
    def decorator_maker(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator_to_enhance(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker

@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
    """Декоратор. Шаблон """
    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs) -> Callable:
        print('Переданные арги и кварги в декоратор:', dec_args, dec_kwargs)
        return func(*func_args, **func_kwargs)
    return wrapper

@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    """пример декорируемой функции"""
    print('Привет', text, num)


decorated_function('Юзер', 101)