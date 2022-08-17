# task 1
from typing import Callable

def how_are_you(func:Callable) -> Callable:
    user = input('Как дела? ')
    print('А у меня не очень! Ладно, держи свою функцию.')
    result = func()
    return result


@how_are_you
def test():
    print('<Тут что-то происходит...>')

test


# task 2
import time
from typing import Callable

def wrapped_func(func) -> Callable:
        time.sleep(2)
        print('Прошло две секунды')
        result = func()
        return result

@wrapped_func
def to_do():
    print('Hello')

to_do

# task 3
from typing import Callable, Any

def logging(func: Callable) -> Callable:
        """Декоратор, логирующий работу кода"""
        from datetime import datetime
        def wrapped_func() -> Any: 
            try:
                print('\n Вызывается функция {func}\t'
                'Документация: {doc}'.format(
                    func=func.__name__, doc = func.__doc__
                ))
                result = func()
                print('Функция успешно завершила работу')
                return result
            except Exception as e:
                e = f'{datetime.now()} - {func.__name__} - {e}'
                with open('logging.log', 'a+', encoding="utf-8") as f:
                    f.write(e)
        return wrapped_func 

@logging
def name():
    """'hello'"""

@logging
def zero():
    x = 1/0

name()
zero()

# task 4

from typing import Callable, Any

def debug(func: Callable) -> Callable:

    def debug_internal(*args, **kwargs) -> Any:
        
        print(' Вызывается {func},\n {name_func} вернула значение {value},\n {result}'.format(
            func=repr(func.__name__), name_func=func.__name__, value=repr(func(*args, **kwargs)), result = func(*args, **kwargs)
        ))
    return debug_internal

@debug
def greeting(name: str, **kwargs):
    if len(kwargs) == 0:
        return f'Привет, {name}'
    if "age" in kwargs:
        return f'Ого, {name}! Тебе уже {kwargs["age"]}, быстро растешь'

greeting('Tom', age=15)


# task 5

def counter(func):
    
    def wrapped_func(*args, **kwargs):
        wrapped_func.count += 1
        return func(*args, **kwargs)
    
    wrapped_func.count = 0
    return wrapped_func


@counter
def func():
    print("Hello")

func()
func()

print(func.count)

