# 25.2
# Инкапсуляция - механизм языка, позволяющий объединить данные и методы, 
# работающие с этими данными, в единый объект, и скрыть детали реализации от пользователя

# __ - это соглашение между программистами. Используется только внутри класса. Сокрытие данных!

# print(Person.__count) -> error    BUT   print(Person._Person__count) -> result, but it's uncorrect

# class Person:
#     __count = 0

#     def __init__(self, name, age):
#         self.__name = name
#         self.set_age(age)
#         Person.__count += 1 #приватный атрибут(сокрытие данных, используется только в классе)

#     def __str__(self):
#         return 'Name: {}\tAge:{}'.format(self.format(self.__name, self.__age))

#     # getter
#     def get_count(self):# получение объекта
#         return self.__count

#     def get_age(self):
#         return self.__age

#     # setter
#     def set_age(self, age):#изменение объекта
#         if age in range(1, 90):
#             self.__age = age
#         else:
#             raise Exception('Wrong age')


# misha = Person('Misha', 20)
# tom = Person('Tom', 25)
# print(misha.get_count())
# new_age = 80
# misha.set_age(new_age)
# print(misha.get_age())

# # Person._Person__count выведет результат скрытого элемента класса, но использовать не рекомендуется

# # 25.3
# # Наследование - механизм языка, позволяющий создавать новый класс на основе уже существующего

# class Pet: #базовый класс
#     legs = 4
#     __has_tail = True

#     def __str__(self):
#         tail = 'yes' if self.__has_tail else 'no'
#         return 'Leg: {legs}\nTail: {has_tail}'.format(
#             legs=self.legs,
#             has_tail = tail
#         )


# class Cat(Pet):#подкласс
#     def sound(self):
#         print('Meow')

# class Dog(Pet):#подкласс
#     def sound(self):
#         print('Gaf')

# class Frog(Pet):#подкласс
#     has_tail = False
#     def sound(self):
#         print('Kwa')


# cat = Cat()
# dog = Dog()
# frog = Frog()
# print(cat)
# print(dog)
# print(frog)
# cat.sound()
# dog.sound()
# frog.sound()



# # task 'Ship'
# # выходные данные = экземляры классов
# # Даны два класса кораблей — грузовой и военный. У каждого из этих кораблей есть своя модель, и каждый может сделать два действия: сообщить свою модель и идти по воде. 
# # Грузовой корабль имеет такой атрибут, как заполненность, изначально он равен нулю. У него есть ещё два действия: погрузить и выгрузить груз с корабля. 
# # У военного же корабля нет никаких грузов, есть только оружие, которое передаётся вместе с моделью. Также, вместо погрузки и выгрузки, у него есть другое действие — атаковать.
# # Реализуйте классы грузового и военного кораблей. Для этого выделите общие атрибуты и методы в отдельный класс «Корабль» и используйте наследование. Не забудьте про функцию super в дочерних классах.
# class Ship:
#     def __init__(self, model):
#         self.__model = model#потому что модель не нужно будет изменять

#     def __str__(self): #TODO существует еще функция __repr__
#         return '\n Ship model: {model}'.format(
#             model=self.__model
#         )

#     def sail(self):
#         print('\n Ship is swimming')


# class WarShip(Ship):
#     def __init__(self, model, gun):
#         super().__init__(model)
#         self.gun = gun

#     def attack(self):
#         print('\n Ship attacked with gun', self.gun)


# class CargoShip(Ship):
#     def __init__(self, model):
#         super().__init__(model)
#         self.tonnage_load = 0

#     def load(self):
#         print('\n Loading ship')
#         self.tonnage_load = 1
#         print('Current workload:', self.tonnage_load)

#     def unload(self):
#         print('\n Woarloading ship')
#         if self.tonnage_load > 0:
#             self.tonnage_load -= 1
#         else:
#             print('Ship is workloaded')
#         print('Current workload:', self.tonnage_load)


# warship = WarShip('zxc', 'Gun')
# print(warship.__str__())
# warship.attack()
# cargoship = CargoShip('wert')
# cargoship.load()



# # Полиморфизм - принцип, предполагающий способность к изменению функционала, 
# # унаследованного от базового класса
# # 25.4

# class Pet:
#     legs = 4
#     __has_tail = True

#     def __str__(self):
#         tail = 'yes' if self.__has_tail else 'no'
#         return 'Leg: {legs}\nTail: {has_tail}'.format(
#             legs=self.legs,
#             has_tail = tail
#         )

#     def walk(self):
#         # полиморфизм - единая функция для дочерних классов
#         print('Гуляет')

# class Cat(Pet):
#     def sound(self):
#         print('Meow')

# class Dog(Pet):
#     def sound(self):
#         print('Gaf')

# class Frog(Pet):
#     has_tail = False
#     def sound(self):
#         print('Kwa')

#     def walk(self):
#         # полиморфизм
#         print('Плавает')


# cat = Cat()
# dog = Dog()
# frog = Frog()
# print(cat)
# print(dog)
# print(frog)
# cat.sound()
# dog.sound()
# frog.sound()

# # опять с классом персон + документация(docstring)
# # проверка кода производится линетрами, опирающиеся на стандарты качества кода

# class Person:
#     """
#     Базовый класс, описывающий человека

#     __count: общее количество человек

#     Args:
#         name(str): передается имя человека
#         age(int): передаётся возраст человека

#     """
#     __count = 0

#     def __init__(self, name, age):
#         self.__name = name
#         self.set_age(age)
#         self.__location = 'Moscow'
#         if Person.__count > self.max_count:
#             raise Exception('So a lot of people')
#         Person.__count += 1

#     def __str__(self):
#         return 'Name: {}\tAge:{}'.format(self.format(self.__name, self.__age))

#     # getter
#     def get_count(self):
#         return self.__count

#     def get_age(self):
#         """
#         Геттер для получения возраста

#         :return: __age
#         :rtype: int
#         """
#         return self.__age

#     # setter
#     def set_age(self, age):
#         """
#         Сеттер для установления возраста
#         :param age: возраст
#         :type age: int
#         :raise Exception: если возраст не в границах от 1 до 90, то вызывается исключение
#         """
#         if age in range(1, 90):
#             self.__age = age
#         else:
#             raise Exception('Wrong age')

# class Student(Person):
#     def __init__(self, name, age, university):
#         super().__init__(name, age)
#         self.university = university

#     def __str__(self):
#         info = super().__str__()
#         info = '\n'.join(
#             (
#                 info,
#                 'Student studies in university {}'.format(self.university)
#             )
#         )
#         return info
#         # return 'Student {} studies in university {}'.format(self.get_name(), self.university)


# class Employee(Person):
#     """
#     Класс Работник. Родитель: Person

#     Args:
#         name(str):передается имя человека
#         age(int):передается возраст человека

#     Attributes:
#         job(str): должность работника
#     """

#     def __init__(self, name, age, company, salary):
#         super().__init__(name, age)
#         self.company = company
#         self.salary = salary

#     def __str__(self):
#         info = super().__str__()
#         info = '\n'.join(
#             (
#                 info,
#                 'Company: {}\tSalary: {}'.format(self.company, self.salary)
#             )
#         )
#         return info

# my_student = Student(name='Tom', age=24, university='MSU')
# print(my_student)
# my_employee = Employee(name='Bob', age=25, salary=10000, company='Google')

# # docstring
# print(Person.__doc__)

# task 1

# class Property:

#     """
#     Базовый класс, где хранятся параметры объектов

#     Args:
#     worth - стоимость объекта
#     money - кол-во денег у человека
    
#     Attributes:
#     tax - полученный налог

#     """

#     def __init__(self, worth, money:int):
#         self.worth = worth
#         self.money = money

#     def cost_calculation(self, object):

#         """
#         Вычисление налогов на определенный объект

#         :return: tax 

#         """

#         if object == 'car':
#             return self.worth//200
#         if object == 'flat':
#             return self.worth//1000
#         if object == 'cottage':
#             return self.worth//500
    
#     def have_money(self, money, tax):

#         """
#         Проверка на возможность оплаты налогов

#         :rtype: str

#         """
        
#         if money > tax:
#             return 'Enough money'
#         else:
#             return 'Not enough money. Debt: {}'.format(
#                 tax - money
#             )

# class Car(Property):

#     def __init__(self, worth, money):
#         super().__init__(worth, money)

# def check(object):

#     """
#     Общая вычисляющая функция для объекта, полученного от пользователя
    
#     """

#     worth = (input('Price and money: ')).split(',')
#     client = Car(int(worth[0]), int(worth[1]))
#     tax = client.cost_calculation(object)
#     print(f'Taxes: {tax}')
#     money = client.have_money(int(worth[1]), tax)
#     print(money)

# client_object = input('Type of object: ')
# check(client_object)

# task 3

# class MyDict:

#     def __init__(self, dict: dict):
#         self.dict = dict

#     def return_zero(self):
#         """
#         Функция возвращения 0 в связи с отсутствием ключа в словаре

#         """
#         key = input('Enter key: ')
#         return self.dict.get(key, 0)

# own_dict = {}
# num_param = int(input('Number of parametrs: '))
# for i in range(1, num_param+1):
#     own_dict[i] = input('Enter value: ')

# my_dict = MyDict(own_dict)
# result = my_dict.return_zero()
# print(result)


# task 2
# import random

# class Life:

#     """
#     Основной класс для игры в симулятор

#     Args:
#     __count - количество очков кармы, которого нужно достичь
    
#     Attributes:
#     sum - текущее кол-во очков кармы
    
#     """

#     count = 500
#     def __init__(self, count, sum):
#         self.__count = count
#         self.sum = sum

#     def get_count(self):
#         return self.__count

#     def one_day(self):
#         if random.randint(1,10) == 1:
#             with open("karma.log", 'r') as file:
#                 log = file.readlines()
#             log += (random.choice(["KillError", "DrunkError", "CarCrashError", "GluttonyError", "DepressionError"])+'\n')
#             with open("karma.log", 'r') as file:
#                 for line in log:
#                     file.write(line)

#         return random.randint(1,7)

# class OwnLife(Life):

#     def __init__(self, count, sum):
#         super().__init__(count, sum)

#     """
#     Проверка на достижение заданных очков кармы
    
#     """

#     def check_karma(self):
#         count = Life.get_count(self)
#         if count < 500:
#             self.sum += Life.one_day()

# karma = OwnLife(500, 0)
# while karma.sum < 500:
#     karma.check_karma()


# task 4
# import random

# class Person:

#     """
#     Основной класс 

#     Arg:
#     name - имя сотрудника
#     surname - фамилия сотрудника
#     age - возраст сотрудника

#     """

#     def __init__(self, name, surname, age):
#         self.__name = name
#         self.__surname = surname
#         self.__age = age


# class Employee(Person):


#     def __init__(self, name, surname, age, salary):
#         super().__init__(name, surname, age)
#         self.salary = salary

#     def get_salary(self, salary):
#         return salary

# class Manager(Employee):

#     """
#     Класс для менеджеров

#     Attribute:
#     salary - итоговая зарплата за месяц
    
#     """
    
#     def __init__(self, name, surname, age, salary):
#         super().__init__(name, surname, age, salary)

#     def get_salary(self, ):
#         return super().get_salary(self.salary)

# class Agent(Employee):

#     """
#     Класс для агентов

#     Arg:
#     price_product - цена продукта
#     sale - количество продаж

#     Attribute:
#     salary - итоговая зарплата за месяц
    
#     """

#     def __init__(self, name, surname, age, sale, price_product):
#         super().__init__(name, surname, age)
#         self.price_product = price_product
#         self.sale = sale

#     def get_salary(self):
#         return 5000*((self.sale*5)/100)
    
# class Worker(Employee):

#     """
#     Класс для агентов

#     Arg:
#     time - рабочие часы

#     Attribute:
#     salary - итоговая зарплата за месяц
    
#     """

#     def __init__(self, name, surname, age, time):
#         super().__init__(name, surname, age)
#         self.time = time

#     def get_salary(self):
#         return self.time*100

# list_obj = ['Manager', 'Manager', 'Manager', 'Agent', 'Agent', 'Agent', 'Worker', 'Worker', 'Worker',]

# all_salary = 0
# for i in list_obj:
#     if i == "Manager":
#         manager = Manager(input(), input(), random.randint(20,40), 130000)
#         manager_sal = manager.get_salary()
#         all_salary += manager_sal

#     if i == "Agent":
#         agent = Agent(input(), input(), random.randint(20,40), random.randint(20,30), 3000)
#         agent_sal = agent.get_salary()
#         all_salary += agent_sal

#     if i == "Worker":
#         worker = Worker(input(), input(), random.randint(30,40))
#         worker_sal = worker.get_salary()
#         all_salary += worker_sal

# print(all_salary)

# task 5   
# import math
  
# class Car:
    
#     def __init__(self, x, y, fi):
    
#         self.x = x
#         self.y = y
#         self.fi = fi
    
#     def move(self, dist):
#         self.x = self.x + dist * math.cos(self.fi)
#         self.y = self.y + dist * math.sin(self.fi)
 
 
# class Bus(Car):
#     ticket_coef = 0.1
#     limit_passengers = 20

    
#     def __init__(self, x, y, direction):
#         super().__init__(x, y, direction)
#         self.passengers = 0
#         self.money = 0
    
    
#     def move(self, distance):
#         self.money += Bus.ticket_coef * self.passengers * distance
#         super().move(distance)
    
    
#     def enter(self, passengers):
#         if passengers + self.passengers > Bus.limit_passengers:
#             print('Достигнута максимальная вместимость автобуса')    
#             passengers = Bus.limit_passengers - self.passengers
#         return passengers
    
    
#     def exit(self, passengers):
#         if passengers > self.passengers:
#             print('Вам придется выйти')
#             passengers = self.passengers

#         return passengers
    
    
#     def __str__(self):
#         lines = [
#             super().__str__(),
#             f'В автобусе {self.passengers} пассажиров',
#             f'У водителя {self.money} денег',
#         ]
#         return '\n'.join(lines)


# task 6
# import random

# class Human:

#     def __init__(self, name, level_satiety, happiness):

#         self.__name = name
#         self.level_satiety = level_satiety
#         self.happiness = happiness

#     def pet_cat(self):
        
#         self.happiness += 5
#         return self.happiness

#     def to_eat(self,  unit_of_food):
#         print('I want to eat')
#         self.level_satiety +=  unit_of_food
#         home.food -= unit_of_food
#         return self.level_satiety

    

# class Home:

#     def __init__(self, money, food, food_for_cat, dirty):

#         self.money = money
#         self.food = food
#         self.food_for_cat = food_for_cat
#         self.dirty = dirty

#     def get_dirty(self):
#         self.dirty += 5
#         return self.dirty

# class Husband(Human):

#     def __init__(self, name, level_satiety, happiness, money_for_furcoat):
#         super().__init__(name, level_satiety, happiness)
#         self.money_for_furcoat = money_for_furcoat


#     def get_name(self):
#         return self.__name

#     def play_game(self):
#         self.happiness += 20
#         self.level_satiety -= 10
#         return self.happiness

#     def go_to_work(self):
#         home.money += 120
#         self.money_for_furcoat +=30
#         self.level_satiety -= 10
#         return ('Money after work: {money}').format(
#             money=home.money
#         )

#     def do_random(self):
#         todo_list = ['eat','go to work', 'play game', 'pet cat']

#         while True:
#             print('Husband to-do list')
#             random_action = random.choice(todo_list)
#             if random_action == 'go to work':
#                 self.go_to_work()
#                 print('interesting work')
#                 break
#             if random_action == 'play game':
#                 self.play_game()
#                 print('interesting game')
#                 break
#             if random_action == 'eat':
#                 if self.level_satiety == 30:
#                     print('Satiety is full')
#                     todo_list.remove('eat')
#                     continue
#                 else:
#                     level_hungry = 30 - self.level_satiety 
#                     if home.food > level_hungry:
#                         self.to_eat(level_hungry)
#                         print('its so delicuos')
#                         break
#             if random_action == 'pet cat':
#                 print('a fluffy cat')
#                 self.pet_cat()
            
#             return True




# class Wife(Human):

#     def __init__(self, name, level_satiety, happiness, count_furcoat):
#         super().__init__(name, level_satiety, happiness)
#         self.count_furcoat = count_furcoat

#     def get_name(self):
#         return self.__name

#     def buy_fur_coat(self):
#         self.happiness += 60
#         self.count_furcoat += 1
#         self.level_satiety -= 10
#         return self.happiness

#     def buy_food(self, count_food):
#         home.money -= count_food
#         home.food += count_food
#         self.level_satiety -= 10
#         return ('Money now: {money}, food now: {food}').format(
#             money=home.money, food=home.food
#         )

#     def clean_home(self):
#         home.dirty = 0
#         self.level_satiety -= 10
#         return home.dirty

#     def buy_catfood(self, count_catfood):
#         home.money -= count_catfood
#         home.food_for_cat += count_catfood
#         self.level_satiety -= 10
#         return ('Money now: {money}, food now: {food}').format(
#             money=home.money, food=home.food_for_cat 
#         )

#     def do_random(self):
#         todo_list = ['eat', 'buy product', 'buy a fur coat', 'clean the house', 'buy a catfood', 'pet cat']

#         while True:
#             print('Wife to-do list')
#             random_action = random.choice(todo_list)
#             if random_action == 'eat':
#                 if self.level_satiety == 30:
#                     print('Satiety is full')
#                     todo_list.remove('eat')
#                     continue
#                 else:
#                     level_hungry = 30 - self.level_satiety 
#                     if home.food > level_hungry:
#                         self.to_eat(level_hungry)
#                         break
#                     else:
#                         if home.money > level_hungry:
#                             result = self.buy_food()
#                             print(result)
#                             break
#                         else:
#                             husband.go_to_work()

#             if random_action == 'buy product':
#                 if home.food == 70:
#                     print('Fridge is full')
#                     todo_list.remove('buy product')
#                     continue
#                 else:
#                     not_enough_product = 70 - home.food
#                     if home.money > not_enough_product:
#                         result = self.buy_food(not_enough_product)
#                         print('I have bought products')
#                         print(result)
#                         break
#                     else:
#                         husband.go_to_work()

#             if random_action == 'buy a fur coat':
#                 if husband.money_for_furcoat == 350:
#                     self.buy_fur_coat()
#                     print('I have bought a new fur coat')
#                     break
#                 else:
#                     print('I will do smth else')
#                     todo_list.remove('buy a fur coat')
#                     continue
            
#             if random_action == 'clean the house':
#                 if home.dirty > 0:
#                     self.clean_home()
#                     break
#                 else:
#                     print('Cleaning is not needed')
#                     continue

#             if random_action == 'buy a catfood':
#                 if home.food_for_cat == 40:
#                     print('Catfood is not needed')
#                     todo_list.remove('buy a catfood')
#                     continue
#                 if home.food_for_cat < 30:
#                     not_enough_food = 40 - home.food_for_cat
#                     result = self.buy_catfood(not_enough_product)
#                     print(result)
#                     print('Catfood is bought')
#                     break

#             if random_action == 'pet cat':
#                 self.pet_cat()
#                 print('Cute cat')
#                 break

#             break



    

# class Cat:

#     def __init__(self, name, level_satiety_cat):
#         self.__name = name
#         self.level_satiety_cat = level_satiety_cat

#     def get_name(self):
#         return self.__name

#     def cat_eat(self):
#         unit_of_food = 30 - self.level_satiety_cat
#         self.level_satiety_cat += unit_of_food*2
#         self.level_satiety_cat -= unit_of_food

#     def spoil_wallpaper(self):
#         home.dirty +=5
#         self.level_satiety_cat -= 10
#         return home.dirty

#     def do_random(self):
#         while True:
#             print('Cat to-do list')
#             todo_list = ['eat', 'spoil wallpaper']
#             random_action = random.choice(todo_list)

#             if random_action == 'eat':
#                 if home.food_for_cat > 30 - self.level_satiety_cat:
#                     self.cat_eat()
#                     print('Cat ate')
#                     break
#                 else:
#                     wife.buy_catfood()
            
#             if random_action == 'spoil wallpaper':
#                 self.spoil_wallpaper()
#                 print('House is a bit dirty')
#                 break

#             return True


# husband = Husband('Ivan', 30, 100, 0)
# wife = Wife('Mary', 30, 100, 0)
# cat = Cat('Jo', 30)
# home = Home(100, 50, 30, 0)

# def full_satiety():
#     global man, woman , kitten  
#     if husband.level_satiety > 10 and wife.level_satiety > 10 and cat.level_satiety_cat > 10:
#         return True
#     else:
#         if husband.level_satiety <= 10:
#             husband.to_eat()
#             man = True
#         if wife.level_satiety <= 10:
#             wife.to_eat()
#             woman = True
#         if cat.level_satiety_cat <= 10:
#             cat.cat_eat()
#             kitten = True
#         return woman, man, kitten        

# for i in range(1, 4):
#     print('Day {day}'.format(day=i))
#     woman = False
#     man = False
#     kitten = False
#     while woman != True and man != True and kitten != True:

#             if  full_satiety():
#                 pass

#             if home.money < 30:
#                 husband.go_to_work()
#                 man = True
#             if home.food < 10:
#                 wife.buy_food()
#                 woman = True
#             if home.food_for_cat < 10:
#                 wife.buy_catfood()
#                 woman = True
#             if kitten == False:
#                 cat.do_random()
#                 kitten = True
#             if woman == False:
#                 wife.do_random()
#                 woman = True
#             if man == False:
#                 husband.do_random()
#                 man = True                
        

# print('Earned money: {money}, fur coat: {furcoat}'.format(money=Home.money, furcoat=Wife.count_furcoat))             
    

# task 7

# class Stack:

#     def __init__(self):
#         self.stack = {}

#     def push(self, key, value):
#         if key not in self.stack:
#             self.stack[key] = value
#         else:
#             new_value = ','.join([self.stack[key], value])
#             self.stack[key] = new_value
#         return self.stack


#     def pop(self, object):
#         if len(self.stack) == 0:
#             return None
#         else:
#             for i in list(self.stack.keys()):
#                 if i == list:
#                     for j in i:
#                         if j == object:
#                             i.remove(object)
#                 else:
#                     self.stack.pop(object)


# class TaskManager(Stack):

#     def __init__(self):
#         super().__init__()

#     def new_task(self, command, object):
#         if command == 'pop':
#             Stack.pop(self, object[0])
#             return self.stack
#         if command == 'push':
#             result = Stack.push(self, object[1], object[0])
#             return result


# manager = TaskManager()
# manager.new_task('push',("сделать уборку", 4))
# manager.new_task('push', ("помыть посуду", 4))
# manager.new_task('push', ("отдохнуть", 1))
# manager.new_task('push', ("поесть", 2))
# manager.new_task('push', ("сдать дз", 2))
# result_list = [manager.stack[key] for key in sorted(list(manager.stack.keys()))]
# print(result_list)