""" 
Множественное наследование: MRO 

Diamond problem - то есть схема при таком наследовании имеет форму ромба

            Person
           /      \
        Parent  Employee
           \      /
            Citizen

Method Resolution Order - порядок разрешения методов

                  Main
            /   /   |   \   \
           3A   4B  7C  8D  9E
           \   / \    \  \  /
            2M1   5M2    6М3
               \   |    /
                   1W 

Используемый алгоритм назыввается C3 superclass linearization

"""

from typing import List

class Person:
    """ Базовый класс """

    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def shout(self):
        print('Я - Человек!')

    
class Employee(Person):
    """ Работник. Дочерний класс от Person"""

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.__salary = 20000

    def get_salary(self) -> int:
        return self.__salary

    def shout(self):
        print('Я - Работник!')


class Parent(Person):
    """ Родитель. Дочерний класс от Person """

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.__kids = ['Tom', 'Bob']

    def get_kids(self) -> List[str]:
        return self.__kids

    def shout(self):
        print('Я - Родитель!')


class Citizen(Parent, Employee):
    """ Житель - является и Родителем, и Работником """

    # def shout(self):
    #     print('Я - Житель!')

my_citizen = Citizen(name='Anton', age=30)
print(my_citizen.get_salary())
print(my_citizen.get_kids())
my_citizen.shout()

""" MRO """
print(my_citizen.__class__.__mro__)



""" Множественное наследование: примеси и абстрактные классы """

from abc import ABC, abstractmethod

class Figure(ABC):

    """
    Абстрактный базовый класс Фигура

    Args and attrs:
        pos_x(int): координата X
        pos_y(int): координата Y
        lenght(int): длина фигуры
        width(int): ширина фигуры

    """

    def __init__(self, pos_x: int, pos_y: int, lenght: int, width: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.lenght = lenght
        self.width = width

    """ абстрактный метод """
    """ благодаря данному методу невозможно будет создать инстанс данного класса"""
    # инстанс - это процесс создания на основе класса экземпляра класса
    @abstractmethod 
    def move(self, pos_x: int, pos_y: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y


class ResizableMixin: 
    """ 
    Квадрат и прямоугольник полиморфны в методе move, но не в resize, поэтому функционал выведен в отдельный класс
    это класс-примесь. общий функционал для прямоугольника и квадрата
    Такие классы создаются во избежании создания больших иерархий
    """
    def resize(self, lenght: int, width:int) -> None:
        self.lenght = lenght
        self.width = width

class Rectangle(Figure, ResizableMixin):
    """ Прямоугольник. Родительский класс: Figure """
    pass

class Square(Figure, ResizableMixin):
    """ Квадрат. Родительский класс: Figure """

    def __init__(self, pos_x: int, pos_y: int, size: int) -> None:
        return super().__init__(pos_x, pos_y, size, size)

rect_1 = Rectangle(pos_x=10, pos_y=20, lenght=5, width=6)
rect_2 = Rectangle(pos_x=30, pos_y=40, lenght=10, width=11)
square_1 = Square(pos_x=50, pos_y=70, size=7)

for figure in [rect_1, rect_2, square_1]:
    new_size_x = figure.lenght * 2
    new_size_y = figure.width * 2
    figure.resize(new_size_x, new_size_y)

test = Figure(1,1,1,1)


""" 
контекст - менеджер 

- это объект питона, который следит за инициализацией и финализацией данного контекста,
в частности определяет действия, который должны происходить до и после выполнения блока кода

Example:
with open('file.txt', 'w') as file:
    file.write('hello')

здесь контекст-менеджером выступает open, 
with as это всего лишь помощники для запуска функции open
то есть в функции open уже по сути прописаны try, except, finally
with работает с реализацией контекст-менеджера в каком-то объект, в нашем случае в функции open
"""

import time

class Timer:
    def __init__(self) -> None:
        print('Время рабоыт кода')
        self.start = None

    def __enter__(self) -> 'Timer':
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool: # последние три значения в скобка помогают обработать ошибки
        print(time.time() - self.start)
        """ последующий код блокирует ошибки TypeError, возникающий из-за строки 181 """
        # if exc_type is TypeError:
        #     return True
        # либо просто return True, чтобы избегать все ошибки
        return True



with Timer() as t1:
    print('Первая часть')
    val_1 = 100*100*1000000
    val_1 += 'abc' # для ошибки в exit
    # еще какой-то код

with Timer() as t2:
    print('Вторая часть')
    val_2 = 200*200*2000000
    # еще какой-то код

with Timer() as t3:
    print('Третья часть')
    val_3 = 300*300*3000000
    # еще какой-то код

"""
Контекст - менеджер применяется в следующем:

- синхронизация доступа к общим ресурсам
- настройка среды выполнения
- управление подключением к базе данных
- работа с временными файлами
- обёртка соединений по протоколу и т.д.

"""



"""
Методы класса: декораторы setter и property

"""

class Person:
    """
    Человек 

    Args:
        name(str): имя
        age(int): возраст 

    Attributes:
        _name(str): имя (одно нижнее подчеркивание означет, 
                что данный атрибут можно использовать в дочерних классах)
        _age(int): возраст (от 1 до 100, иначе ошибка)

    property, a.setter для удобства работы с атрибутами класса в основном коде
    """

    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self.age = age

    def __str__(self):
        return 'Name: {}\tAge:{}'.format(self.format(self._name, self.age))

    @property
    def age(self):#меняем get_age на age
        return self.age

    # setter
    @age.setter
    # сначала указывается имя нашего метода, а потом прописывается декоратор
    # и меняем имя с set_age на age
    # теперь в методе __init__ мы можем заменить вызов на нормальную строку
    def age(self, age):#изменение объекта
        if age in range(1, 100):
            self.age = age
        else:
            raise Exception('Wrong age')

    @property
    def name(self):#меняем с get_name на name, потом прописываем декоратор property
        return self._name

    # setter
    @name.setter
    def name(self, name: str):#меняем с 
        if isinstance(name, str):
            self.name = name
        else:
            raise Exception('Wrong name')


tom = Person('Tom', 25)
print(tom)
print(tom.age) # это наш метод, который мы передаем в декоратор
#  то есть после введения декоратора property мы будем обращаться к методам, а не к атрибутам
tom.age(36)
print(tom.age())



""" Методы класса: декоратор classmethod """

class Pet:
    TOTAL_SOUNDS = 0

    def __init__(self) -> None:
        self.__legs = 4
        self.__has_tail = True

    def __str__(self) -> str:
        tail = 'yes' if self.__has_tail else 'No'
        return 'Всего ног: {legs}\n Хвост присутствует - {has_tail}'.format(
            legs=self.__legs,
            has_tail=tail
        )


class Cat(Pet):
    @classmethod # можно было бы использовать @staticmethod, но от него постепенно отказываются
    def sound(cls) -> None:# плюс в данном методе - это наличие cls, он в себе содержит класс, а не экземпляр класса
                            # а значит через него мы можем обращаться ко всему, что есть в классе
        cls.TOTAL_SOUNDS += 1# таким образом мы увеличиваем значение для всего класса, а не для отдельного объекта
        print(cls.TOTAL_SOUNDS)
        print('Meow')

class Dog(Pet):
    @classmethod
    def sound(self) -> None:
        print('Gaf')

Cat.sound()