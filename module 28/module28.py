# Задача 1. Работа с файлом 2
# Что нужно сделать

# Реализуйте модернизированную версию контекст-менеджера File: 

# теперь при попытке открыть несуществующий файл менеджер автоматически создаёт и открывает этот файл в режиме записи; 
# на выходе из менеджера подавляются все исключения, связанные с файлами.

# from math import radians


# class File:
#     """
#     Модернизированная версия контекст-менеджера File — теперь при попытке
#     открыть несуществующий файл менеджер автоматически создаёт и открывает этот файл в режиме записи.
#     """
 
#     def __init__(self, file_name: str, mode: str):
#         self.file_name = file_name
#         self.mode = mode
#         self.file = None
 
#     def __enter__(self):
#         self.file = open(self.file_name, self.mode)
#         return self.file
 
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
 
 
# if __name__ == '__main__':
#     with File('example.txt', 'w+') as file:
#         file.write('Hello World!!')


# Ирина использует в своей программе очень много различных математических вычислений, связанных с фигурами. Например, нахождение их площадей или периметров.
# Поэтому, чтобы не захламлять код огромным количеством функций, она решила выделить для них отдельный класс, подключить как модуль и использовать по аналогии с модулем math.

# Реализуйте класс MyMath, состоящий как минимум из следующих методов (можете бонусом добавить и другие методы):

# вычисление длины окружности,
# вычисление площади окружности,
# вычисление объёма куба,
# вычисление площади поверхности сферы.

# import math

# class MyMath:

#     def __init__(self, lenght) -> None:
#         self.lenght = lenght

#     def circle_len(self):
#         return self.lenght * math.pi

#     def circle_sq(self):
#         return (self.lenght ** 2) * math.pi 

#     def cube_volume(self):
#         return self.lenght ** 3

#     def sphere_area(self):
#         return self.lenght**2 * (4 * math.pi)

# res_1 = MyMath(lenght=5)
# res_2 = MyMath(lenght=6)
# print(res_1.circle_len())
# print(res_2.cube_volume())


# В проекте по 3D-моделированию используются две фигуры — куб и пирамида. 
# Для моделирования этих фигур используются соответствующие 2D-фигуры, а именно квадрат и треугольник. 
# Вся поверхность 3D-фигуры может храниться в виде списка. Например, для куба это будет [Square, Square, Square, Square, Square, Square].
# Квадрат инициализируется длинами сторон, а треугольник — основанием и высотой. 
# Каждая из 2D-фигур умеет находить свои периметр и площадь, а 3D-фигуры, в свою очередь, могут находить площадь своей поверхности.
# Используя входные данные о фигурах и знания математики, реализуйте соответствующие классы и методы. Для базовых классов также реализуйте геттеры и сеттеры. 

# import math

# class Figure:

#     def __init__(self, figure_name) -> None:
#         self._figure_name = figure_name

#     @property
#     def name(self):
#         return self._figure_name

#     @name.setter
#     def name(self, new_name):
#         self._figure_name = new_name
#         return self._figure_name

    
# class Square(Figure):

#     def __init__(self, figure_name, lenght) -> None:
#         super().__init__(figure_name)
#         self.lenght = lenght

#     def get_square(self):
#         return self.lenght**2

#     def sq_perimeter(self):
#         return self.lenght * 4


# class Triangle(Figure):

#     def __init__(self, figure_name, high, base) -> None:
#         super().__init__(figure_name)
#         self.high = high
#         self.base = base

#     def get_square(self):
#         return 0.5 *self.high * self.base

#     def tr_perimeter(self):
#         return 2 * math.sqrt((self.high**2 + (self.base/2)**2))


# class Cube(Figure):

#     def __init__(self, figure_name, lenght) -> None:
#         super().__init__(figure_name)
#         self.lenght = lenght

#     def get_space(self):
#         return 6 * self.lenght**2

# class Pyramid(Figure):
#     def __init__(self, figure_name, high, base) -> None:
#         super().__init__(figure_name)
#         self.high = high
#         self.base = base  

#     def get_sq_space(self):
#         trian_sq = 4 * 0.5 * self.base * self.high
#         square_sq = self.base ** 2
#         return trian_sq + square_sq     

# square = Square('Square', 4)
# square.get_square()
# triangle = Triangle('Triangle', 4, 3)
# triangle.get_square() 




# Реализуйте класс Date, который должен:

# проверять числа даты на корректность;
# конвертировать строку даты в объект класса Date, состоящий из соответствующих числовых значений дня, месяца и года.
# Оба метода должны получать на вход строку вида ‘dd-mm-yyyy’.

# При тестировании программы объект класса Date должен инициализироваться исключительно через метод конвертации, например: date = Date.from_string('10-12-2077').

# Неверный вариант: date = Date(10, 12, 2077).


class Date:

    def __init__(self, *args) -> None:
        self.day, self.month, self.year = args

    @classmethod
    def parse_string(cls, string: str):
        return tuple(map(int, string.split('-')))

    @classmethod
    def is_valid_string(cls, string):
        day, month, year = cls.parse_string(string)
        return 0 < day <= 31 and 0 < month <= 12 and year > 0

    @classmethod
    def from_string(cls, string):
        assert cls.is_valid_string(string), 'Date is not correct'
        return cls(*cls.parse_string(string))

    def __str__(self) -> str:
        return 'Date: {date}   Month: {month}   Year: {year}'.format(
            date=self.day, month=self.month, year=self.year
        )

date = Date.from_string('10-12-2077')
print(date)