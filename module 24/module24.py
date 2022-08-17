# 1
# class Toyota():
#     color = 'red'
#     price = 1000000
#     speed = 100
#     current_speed = 0

#     def change_speed(self):
#         user = int(input('Введите текущую скорость: '))
#         self.current_speed = user
#         return self.current_speed

#     def print_info(self):
#         print('Color: {}, Price:{}, Speed:{}, Current speed:{}'. format(
#             self.color, self.price, self.speed, self.current_speed
#             )
#         )

# my_car = Toyota()
# my_car.print_info()
# my_car.change_speed()
# print('Current speed: {}'.format(my_car.current_speed))

# 2
# class Family():
#     family_name = 'Common family'
#     money = 200000
#     have_a_house = False

#     def family_info(self):
#         print('Name: {}, Money: {}, House: {}'.format(
#             self.family_name, self.money, self.have_a_house
#             )
#         )

#     def earn_money(self, earned_money):
#         self.money += earned_money 
#         return self.money

#     def buy_a_house(self, house_price):
#         if house_price <= self.money:
#             print('We can buy a house')
#             self.have_a_house = True
#             self.money -= house_price
#             print('Current money: {}'.format(self.money))
#         else:
#             print('Try to earn money')

# my_family = Family()

# while not my_family.have_a_house:

#     my_family.family_info()

#     earned_money = int(input('How much money did you earn: '))
#     total = my_family.earn_money(earned_money)
#     print(total)

#     house_price = int(input('How much does a house cost: '))
#     try_to_buy = my_family.buy_a_house(house_price)


# 3
# class Toyota():

#     def __init__(self, color, price, speed, current_speed):
#         self.color = color
#         self.price = price
#         self.speed = speed
#         self.current_speed = current_speed

#     def info(self):
#         print('Color: {}, price: {}, speed: {}, current_speed: {}'.format(
#             self.color, self.price, self.speed, self.current_speed
#             )
#         )

# my_car = Toyota('red', '1200000', '200', '120')
# my_car.info()


# 4


# class Potato():

#     states = {0: 'Не зрелая', 1: 'Росток', 2: 'Зеленая', 3: 'Выросла'}

#     def __init__(self, index):
#         self.index = index
#         self.state = 0

#     def grow(self):
#         if self.state < 3:
#             self.state += 1
        
#         self.print_state()

#     def is_ripe(self):
#         if self.state == 3:
#             return True
#         return False
    
#     def print_state(self):
#         print('Картошка {}: {}'.format(
#             self.index, Potato.states[self.state])
#         )



# class PotatoGarden():

#     def __init__(self, count):
#         self.potatoes = [Potato(index) for index in range(1, count + 1)]

#     def grow_all(self):
#         print('Картошка проросла!')

#         for i_potato in self.potatoes:
#             i_potato.grow()

#     def are_all_ripe(self):
#         if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
#             print('Картошка не созрела!\n')
#         else:
#             print('Вся картошка созрела. Можно собирать.\n')

# my_garden = PotatoGarden(4)
# for _ in range(3):
#     my_garden.grow_all()
#     my_garden.are_all_ripe()


# task 1
# import random

# class Soldier():

#     name = 'user'
#     health = 100
#     hit = 20

#     def fight(self, first_soldier, second_soldier):
#         while True:
#             random_num = random.randint(1, 2)
#             if random_num == 1:
#                 print('Удар по первому войну!')
#                 first_soldier.health -= 20
#                 print('Здоровье 1го соладата: {}'.format(
#                     first_soldier.health
#                 )) 
            
#             if random_num == 2:
#                 print('Удар по второму войну!')
#                 second_soldier.health -= 20
#                 print('Здоровье 2го соладата: {}'.format(
#                     second_soldier.health
#                     )
#                 ) 

#             elif first_soldier.health == 0 or second_soldier.health == 0:
#                 print('Война закончилась!')
#                 if first_soldier.health == 0:
#                     print('Убит первый солдат {}.'.format(
#                         first_soldier.name
#                         )
#                     )
                
#                 else:
#                     print('Убит второй солдат {}.'.format(
#                         second_soldier.name
#                         )
#                     )
#                 break

# first_soldier = Soldier()
# first_soldier.name = 'Alex'

# second_soldier = Soldier()
# second_soldier.name = 'Nick'

# total = second_soldier.fight(first_soldier, second_soldier)


# task 2

# class Student:

#     def __init__(self, name_and_surname, num_of_group, marks):
#         self.name_and_surname = name_and_surname
#         self.num_of_group = num_of_group
#         self.marks = marks

#     def info(self):
#         print('name: {}, group: {}, marks: {}'.format(
#             self.name_and_surname, self.num_of_group, self.marks
#         ))

#     def ascanding(self, dict_of_sum):
        
#         num_list = [int(i) for i in self.marks]
#         dict_of_sum[self.name_and_surname] = sum(num_list) // len(self.marks)
#         print('Unsorted dictionary: {}'.format(dict_of_sum))
#         return dict_of_sum

#     def sorted_values(self, dict_of_sum):
#         sort_values = sorted(dict_of_sum.values())
#         sorted_dict = {}

#         for i in sort_values:
#             for k in dict_of_sum.keys():
#                 if dict_of_sum[k] == i:
#                     sorted_dict[k] = dict_of_sum[k]
#                     break

#         return sorted_dict

        
# dict_of_sum = {}

# while True:
#     name_and_surname = input('Введите имя и фамилию: ')
#     num_of_group = int(input('Введите номер группы: '))
#     marks = (input('Введите оценки: ')).split(' ')

#     user1 = Student(name_and_surname, num_of_group, marks)
#     user1.info()
#     user1.ascanding(dict_of_sum)
#     print('Sorted dictionary: {}'.format(user1.sorted_values(dict_of_sum)))

# task3
# import math

# class Circle:
#     def __init__(self, radius, coord_x1, coord_y1):
#         self.radius = radius
#         self.coord_x1 = coord_x1
#         self.coord_y1 = coord_y1
        
#     def info(self):    
#         print('Радиус окружности {}, координаты {} {}'.format(
#             self.radius, self.coord_x1, self.coord_y1
#                 )
#             )
#     def search_area(self):
#         area = math.pi * (self.radius ** 2)
#         print('Площадь окружности: {}'.format(
#             area
#             )
#         )
        
#         return area
    
#     def search_perimeter(self):
#         perimeter = self.radius * math.pi * 2 
#         print(perimeter)
    
#     def increase_in_sev_times(self):
#         times = int(input('Введите количество раз: '))
#         increase = self.radius * times
#         print('Увеличенный радиус: {}'.format(increase))

# def crossing_the_border(d, first_radius, second_radius):
#         if d > first_radius + second_radius:
#             print('Окружности пересекаются')
#         else:
#             print('Не пересекаются')

# print('Первая окружность')
# x1, y1, r1 = [int(input('Введите координаты и радиус первой окружности ')) for i in range(3)]
# x_coord = Circle(r1, x1, y1)
# x_coord.info()
# x_coord.search_area()
# x_coord.increase_in_sev_times()


# print('Вторая окружность')
# x2, y2, r2 = [int(input('Введите координаты и радиус второй окружности ')) for _ in range(3)]
# y_coord = Circle(r2, x2, y2)
# y_coord.info()
# y_coord.search_area()
# y_coord.increase_in_sev_times()

# d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# cross_border = crossing_the_border(d, x_coord.radius, y_coord.radius)

# task4

# class Parent:

#     def __init__(self, name: str, age: int, child_list: list):
#         self.name = name
#         self.age = age
#         self.child_list = child_list

#     def info(self):
#         print('Parent name: {} and {}. She has children: {} '.format(
#             self.name, self.age, self.child_list
#         ))

#     def take_care_of_child(self, condition):

#         if condition == False:
#             be_quite = input('Ребенок не спокоен. Успокоить? ')

#             if be_quite == 'да':
#                 condition = True
#                 return condition

#             else:
#                 print('Ребенок продолжает быть неспокойным')
    
#     def feed_baby(self, be_hungry):

#         if be_hungry == False:
#             to_feed = input('Покормить ребенка? ')

#             if to_feed == 'да':
#                 print('Ребенок сыт')
#                 be_hungry == True
#                 return be_hungry
            
#             else:
#                 print('Ребенок остался без еды. Хнык')

# class Child:

#     condition = False
#     be_hungry = False

#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def info(self):
#         print('Имя: {} {} лет, состояне покоя:'.format(self.name, self.age)
#          + ('Спокоен' if self.condition else 'Раздражен') + ('Сыт' if self.be_hungry else 'Голоден'))

# def check_age(age_father, name_father, age_child, name_child):
#         if age_child < age_father - 16:
#             print('{} - ребенок {}'.format(name_child, name_father))
#             return True
#         else:
#             print('{} - не ребенок {}'.format(name_child, name_father))
#             return False


# father = Parent('Vasya', 32, ['Oleg'])

# child_oleg = Child('Oleg', 3)

# while True:
#     if check_age( father.age, father.name, child_oleg.age, child_oleg.name):
#         pass
#     else:
#         user_answer = input('Изменить возраст: ')
#         if user_answer == 'да':
#             child_oleg.age = int(input('Введите возраст: '))
#         else:
#             break

#     if father.take_care_of_child(child_oleg.condition):
#         child_oleg.condition = True
#     else:
#         pass

#     if father.feed_baby(child_oleg.be_hungry):
#         child_oleg.be_hungry = True
#     else:
#         pass

#     child_oleg.info


# task 5

# class Gardener:

#     list_harvest = []

#     def __init__(self, name: str, garden_bed: int):
#         self.name = name
#         self.garden_bed = garden_bed

#     def take_care_potato(self):
#         self.take_care = input('Поухаживать за картошкой: ')
#         if self.take_care == 'да':
#             return True
#         else:
#             return False
    
#     def get_harvest(self, index):

#         self.list_harvest.append(index)
#         for i in self.list_harvest:
#             get_potato = input(f'Собрать картошку на грядке {i}? ')
#             if get_potato == 'да':
#                 print('Картошка под номером {} собрана'.format(
#                     i
#                 ))

#                 self.state = 0
#                 self.list_harvest.remove(i)


        

# class Potato():

#     states = {0: 'Не зрелая', 1: 'Росток', 2: 'Зеленая', 3: 'Выросла'}

#     def __init__(self, index):
#         self.index = index
#         self.state = 0

#     def grow(self):
#         if self.state < 3:
#             self.state += 1
        
#         self.print_state()

#     def is_ripe(self):
#         if self.state == 3:
#             return True
#         return False
    
#     def print_state(self):
#         print('Картошка {}: {}'.format(
#             self.index, Potato.states[self.state])
#         )



# class PotatoGarden():

#     def __init__(self, count):
#         self.potatoes = [Potato(index) for index in range(1, count + 1)]

#     def grow_all(self):
#         print('Картошка проросла!')

#         for i_potato in self.potatoes:
#             if Gardener.take_care_potato(self):
#                 i_potato.grow()

#     def are_all_ripe(self):
#         list_ind_potato = [i_potato.is_ripe() for i_potato in self.potatoes]
#         if not all(list_ind_potato):
#             print('Картошка не созрела!\n')
#             for i in list_ind_potato:
#                 if i == True:
#                     Gardener.get_harvest(self, list_ind_potato.index(i))

#         else:
#             print('Вся картошка созрела. Можно собирать.\n')

# my_garden = PotatoGarden(4)

# for _ in range(3):
#     my_garden.grow_all()
#     my_garden.are_all_ripe()


# task6

# class Water:

#     def __str__(self):
#         return 'Water'

#     def __add__(self, other):
#         if isinstance(other, Air): #ПРОВЕРКА НА ПРИНАДЛЕЖНОСТЬ ЭКЗЕМПЛЯРА К КЛАССУ
#             return Storm()
#         elif isinstance(other, Fire):
#             return Steam()
#         elif isinstance(other, Earth):
#             return Dirt()
        
# class Dirt:

#     def __str__(self):
#         return 'Dirt'

# class Air:

#     def __str__(self):
#         return 'Air'

#     def __add__(self, other): # СЛОЖЕНИЕ 
#         if isinstance(other, Earth):
#             return Dust()
#         if isinstance(other, Water):
#             return Storm()
#         elif isinstance(other, Fire):
#             return Lightning()
    

# class Fire:
    
#     def __str__(self):
#         return 'Fire'

#     def __add__(self, other): # СЛОЖЕНИЕ 
#         if isinstance(other, Earth):
#             return Lawa()
#         elif isinstance(other, Water):
#             return Steam()

# class Dust:

#     def __str__(self):
#         return 'Dust'

# class Lightning:

#     def __str__(self):
#         return 'Lightning'

# class Lawa:
    
#     def __str__(self):
#         return 'Lawa'

# class Earth:
    
#     def __str__(self):
#         return 'Earth'

# class Storm:

#     def __str__(self): #СТРОКОВОЕ ПРЕДСТАВЛЕНИЕ ОБЪЕКТОВ КЛАССА
#         return 'Storm'  

# class Steam:

#     def __str__(self):
#         return 'Steam'  

# water = Water()
# fire = Fire()
# print(water + fire)


# task 7 !
# import random

# class Human():

#     food_in_fridge = 50
#     money_in_case = 0
#     be_hungry = 50
#     house = True

#     def info(self):
#         print('Human codition now: \n Satiety: {} \n Money: {} \n Food in a fridge: {} '.format(
#             self.be_hungry, self.money_in_case, self.food_in_fridge))

#     def __init__(self, name):
#         self.name = name

#     def eat_food(self):
#         self.be_hungry +=10
#         self.food_in_fridge -= 10

#     def work_hard(self):
#         self.be_hungry -= 10
#         self.money_in_case += 10

#     def go_to_market(self):
#         self.food_in_fridge += 10
#         self.money_in_case -+ 10

#     def play_game(self):
#         self.play_game -= 10

# user_name = Human(input('Your name: '))
# count = 0

# while True:
#     count += 1

#     if count >=365:
#         random_num = random.randint(1,6)

#         if user_name.be_hungry < 20:
#             user_name.eat_food
#         elif user_name.food_in_fridge < 10:
#             user_name.go_to_market
#         elif user_name.money_in_case < 50:
#             user_name.work_hard
#         elif random_num == 1:
#             user_name.work_hard
#         elif random_num == 2:
#             user_name.eat_food
#         else:
#             user_name.play_game

#     else:
#         break

# user_name.info()

# task 8
# Black Jack

# import random

# class General_actions:

#     total = 0

#     def __init__(self, dict_cards:dict):
#         self.dict_cards = dict_cards

#     def count(self, number):
#            self.total += number
#            return self.total
        
#     def get_card(self):
#         random_cards = random.choice(list((self.dict_cards).keys()))
#         return random_cards

#     def add_to_dict(self, dict_personal_cards: dict):
#         while True:
#             new_card = self.get_card()
#             print('Value card: {}'.format(new_card))
#             if new_card not in list(dict_personal_cards.keys()):
#                 if new_card == 'ace':
#                     if (self.total + self.dict_cards[new_card][1]) > 21: 
#                         self.total += 1
#                         dict_personal_cards[new_card] = 1
#                     else:
#                         self.total += 11
#                         dict_personal_cards[new_card] = 11
#                 else:
#                     dict_personal_cards[new_card] = self.dict_cards[new_card]
#                     self.total += self.dict_cards[new_card]

#                     break

#             return dict_personal_cards
        



# class Player(General_actions):
#     dict_of_cards_user = {}
    
#     def info(self):
#         if len(self.dict_of_cards_user) == 0:
#             print('Empty here.(User)')
#         else:
#             print('User arm: {}. Total: {}'.format(self.dict_of_cards_user, self.total))

#     def return_dict(self):
#         result_user = self.add_to_dict(self.dict_of_cards_user)
#         return result_user


# class Croupier(General_actions):
    
#     dict_of_cards_croupier = {}


#     def info(self):
#         if len(self.dict_of_cards_croupier) == 0:
#             print('Empty here.(Croupier)')
#         else:
#             print('Croupier arm: {}'.format(self.dict_of_cards_croupier, self.total)) 

#     def return_dict(self):
#         result_croupier = self.add_to_dict(self.dict_of_cards_croupier)
#         return result_croupier



# dict_cards = {
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9,
#     '10': 10,
#     'jack': 10,
#     'lady': 10,
#     'king': 10,
#     'ace': (1, 11)
# }

# user = Player(dict_cards)
# for_class = General_actions(dict_cards)
# croup = Croupier(dict_cards)

# user.info()
# croup.info()

# for i in range(2):
#     result_user = user.return_dict()
#     result_croupier = croup.return_dict()

# print("User total:", user.total)
# choice = input('Take an extra card or finish? 1/2  ')
# if choice == '1':
#         result_user = user.return_dict()
# elif choice == '2':
#         if user.total > croup.total:
#             print('User win')
#         else:
#             print('\n')
#             print("Croupier total:", croup.total, '\n')
        

# print('User result', result_user)
# print('Croupier result', result_croupier)

# task 9

class Coordinate():
    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)

class Board:
    def __init__(self):
        self.create_board()
        # self.board = board

    def field(self):
        row_number = 3
        print()
        for row in self.board:
                print(row_number, end=" ")
                row_number -= 1
                for dot in row:
                    if dot == '  ':
                        print('  .', end="  ")
                    else:
                        print(" {} ".format(dot), end=" ")
                print(" ")
        print("  ", end="")
        for num in [1, 2, 3]:
            print("  {}  ".format(num), end="")
        print("")

    def create_board(self):
            self.board = []
            for _ in range(1,4):
                self.board.append([" ."]*3)
            print(self.board)

    def change_board(self, to_where: Coordinate, figure):
        self.board[int(to_where.y)-1][int(to_where.x)-1] = figure

    def have_free_space(self, coordinate: Coordinate):
        c = self.board[int(coordinate.y)-1][int(coordinate.x)-1]
        if self.board[int(coordinate.y)-1][int(coordinate.x)-1] == ' .':
            print('Having a free place passed')
            return True
        else:
            return False

    def check_win(self):
        # win_coord = (((1,3),(2,3),(3,3)), ((1,2),(2,2),(3,2)), ((1,1),(2,1),(3,1)), ((1,3),(1,2),(1,1)), ((2,3),(2,2),(2,1)), ((3,3),(3,2),(3,1)), ((3,1),(2,2),(1,3)), ((3,3),(2,2),(1,1)))
            if self.board[0][2] == self.board[1][2] == self.board[2][2] != ' .':
                return True
            if self.board[0][1] == self.board[1][1] == self.board[2][1] != ' .':
                return True                
            if self.board[0][0] == self.board[1][0] == self.board[2][0] != ' .':
                return True
            if self.board[0][2] == self.board[0][1] == self.board[0][0] != ' .':
                return True
            if self.board[1][2] == self.board[1][1] == self.board[1][0] != ' .':
                return True
            if self.board[2][2] == self.board[2][1] == self.board[2][0] != ' .':
                return True
            if self.board[2][0] == self.board[1][1] == self.board[0][2] != ' .':
                return True
            if self.board[2][2] == self.board[1][1] == self.board[0][0] != ' .':
                return True
            else:
                return False

class Figure:
    def __init__(self, figure):
        self.figure = figure

    def get_figure(self):
        if self.figure == 'circle':
            return 'o'
        if self.figure == 'cross':
            return 'x'            


def get_coordinate(message) -> Coordinate:
    coordinates = []
    while True:
        try:
            coordinates = input(message).split(',')
            x = int(coordinates[0])
            y = int(coordinates[1])
            if x > 3 or x < 1 or y > 3 or y < 1:
                print("Invalid input")
                continue
            return Coordinate(x,y)
        except:
            print("Invalid input")

first_player = Figure(input('Введите фигуру игрок 1: '))
first_figure = Figure.get_figure(first_player)
second_player = Figure(input('Введите фигуру игрок 2: '))
second_figure = Figure.get_figure(second_player)
board_class = Board()
game_over = False

while not game_over:
  while not game_over:
    print('First move')
    while True:
        future_position_first = get_coordinate('Введите координату положения(1):')
        if board_class.have_free_space(future_position_first):
            board_class.change_board(future_position_first, first_figure)
            if board_class.check_win():#проблема
                print('Win')
                game_over = True
            else:
                break
        else:
            continue
    break
    
  while not game_over:
        print('Second move')
        while True:
            future_position_first = get_coordinate('Введите координату положения(2):')
            if board_class.have_free_space(future_position_first):
                board_class.change_board(future_position_first, second_figure)
                if board_class.check_win():#проблема
                    print('Win')
                    game_over = True
                else:
                    break
            else:
                continue
        break
        
