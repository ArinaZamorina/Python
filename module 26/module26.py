# iterator
# итерируемый объект (iterable) - объект, который способен возвращать элементы по одному с помощью цикла. 
# итерируемый объект содержит итератор
# 
# итератор - объект который позволяет перебирать элементы коллекции
# 
items = [10,20,30] #<- итерируемый объект
for i in items: # цикл for для работы с итератором объекта items
  print(i) 

iterator = items.__iter__()
iterator = iter(items)
# используются для обхода элементов различных структур данных
# идея итератора состоит в том, чтобы вынести поведение от кода коллекции из самой коллекции в отдельный класс

import random

class RandomNumbers:
    def __init__(self, limit):
        self.__limit = limit
        self.__counter = 0

    def __iter__(self): #вызывается, когда питону нужно начать цикл прохождения по элементам, вызывает метод нэкст при каждом проходе цикла
        return self

    def __next__(self):
        if self.__counter < self.__limit:
            self.__counter += 1
            return random.randint(0,10)
        else:
            raise StopIteration #цикл прекращается, когда элементы заканчиваются при совместной работе с методом итер

my_iter = RandomNumbers(limit=3)
for num in my_iter:
    print(num)


# fibonacci
# lazy evaluation
class Fibonacci:
    """ Итератор последовательности фибоначчи из n элементов """

    def __init__(self, number):
        self.counter = 0
        self.cur_val = 0
        self.next_val = 1
        self.number = number

    def __iter__(self):
        self.counter = 0 # инициализируем заново, чтобы итератор не был пуст при выводе результата
        self.cur_val = 0
        self.next_val = 1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > 1:
            if self.counter > self.number:
                raise StopIteration
            self.cur_val, self.next_val = self.next_val, self.cur_val + self.next_val

        return self.cur_val


fib_iterator = Fibonacci(10)
for i_value in fib_iterator:
    print(i_value)
print(8 in fib_iterator)



# generator
# генераторы - итераторы, реализованные в виде функции и по которым можно итерироваться только один раз
# генераторы - это функции, которые используют выражение yield(выдача элементов по готовности)
# __iter__ __next__ реализуются автоматически
#  итераторы используются для итерируемых объектов, которые уже загружены в память
# генераторы используются для генерации данных "налету"
# yield замораживает состояние функции вместе со значениями в ней

def fibonacci(number):
    cur_val = 0
    next_val = 1
    for _ in range(number):
        yield cur_val
        cur_val, next_val = next_val, cur_val + next_val
        if cur_val > 10**6:
            return # для завершения генерации (похож на raise StopIteration)

def square(nums):
    for num in nums:
        yield num**2

fib_seq = fibonacci(number=10**9)
for i_value in fib_seq:
    print(i_value, end=' ')
print('\n')
# генератор от генератора
print(sum(square(fibonacci(number=5000))))

# генератор кубов чисел
print()
cubes_gen = (num ** 3 for num in range(10))
for i_num in cubes_gen:
    print(i_num, end=' ')

# аннотация типов
from collections.abc import Iterable


class Person:
    __count = 0

    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.set_age(age)
        Person.__count += 1 #приватный атрибут(сокрытие данных, используется только в классе)

    def __str__(self) -> str:
        return 'Name: {}\tAge:{}'.format(self.format(self.__name, self.__age))

    # getter
    def get_count(self) -> int:# получение объекта
        return self.__count

    def get_age(self) -> int:
        return self.__age

    # setter
    def set_age(self, age) -> int:#изменение объекта
            self.__age = age



def fibonacci(number: int) -> Iterable[int]:
    cur_val = 0
    next_val = 1
    for _ in range(number):
        yield cur_val
        cur_val, next_val = next_val, cur_val + next_val
        if cur_val > 10**6:
            return