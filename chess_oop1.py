class Coordinate():
    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)

class Score():
    def __init__(self):
        self.white = 0
        self.black = 0

class Board:
    def __init__(self):
        self.create_board()
        self.count = Score()

    def chess_field(self):
        row_number = 8
        print()
        for row in reversed(self.board):
                print(row_number, end=" ")
                row_number -= 1
                for point in row:
                    if point == None:
                        print('  .', end="  ")
                    else:
                        print(" {} ".format(point), end=" ")
                print(" ")
        print("  ", end="")
        for num in [1, 2, 3, 4, 5, 6, 7, 8]:
            print("  {}  ".format(num), end="")
        print("")

    def create_board(self):
        self.board = []

        self.board.append([Rook('w'),Knight("w"),Bishop("w"),Queen("w"),King("w"),Bishop("w"),Knight("w"), Rook('w')])
        self.board.append([Pawn('w') for _ in range(8)])
        for i in range(2, 6):
            self.board.append([None]*8)
        self.board.append([Pawn('b') for _ in range(8)])
        self.board.append([Rook('b'), Knight("b"),Bishop("b"),Queen("b"),King("b"),Bishop("b"),Knight("b"),Rook('b')])

    def change_board(self, from_where: Coordinate, to_where: Coordinate):
        figure = self.board[int(from_where.y)-1][int(from_where.x)-1]
        self.board[int(from_where.y)-1][int(from_where.x)-1] = None
        self.board[int(to_where.y)-1][int(to_where.x)-1] = figure

    def get_figure(self, from_where: Coordinate): 
        return self.board[from_where.y-1][from_where.x-1]

    def increase_score(self, color):
        if color == 'w':
            self.count.white += 1
        else:
            self.count.black += 1
        self.print_score()
    
    def print_score(self):
        print(f'There is the enemy. Score [W:B]: ({self.count.white}:{self.count.black})')    


    def have_free_space(self, coordinate: Coordinate, color):
        c = self.board[int(coordinate.y)-1][int(coordinate.x)-1]
        if self.board[int(coordinate.y)-1][int(coordinate.x)-1] == None or self.board[int(coordinate.y)-1][int(coordinate.x)-1].color != color:
            print('Having a free place passed')
            return True
        else:
            return False


class KingDefeated(Exception):
  def __init__(self):
    pass

class Figure:
    def __init__(self, color):
        self.color = color
        self.name = ""

    def __str__(self):
        return f"{self.color}{self.name}"

    def can_go(self, from_where: Coordinate, to_where: Coordinate, board: Board, move_figure: bool):
        pass

    def within_field(self, coordinate: Coordinate):
        if 1 <= int(coordinate.x) <= 8:
            if 1 <= int(coordinate.y) <= 8:
                # print('"Within the field" passed')
                return True

        else:
            # print('"Within the field" is not passed')
            return False
    
    def have_enemy(self, coordinate: Coordinate, board: Board, move_figure = True):
        figure: Figure = board.board[int(coordinate.y)-1][int(coordinate.x)-1]
        if figure == None:
            # print('It is not the enemy')
            return False
        if figure.color != self.color:
            # print('It is the enemy')
            if figure is King and move_figure:
                raise KingDefeated()
            return True
    

    def road_free(self, from_where: Coordinate, to_where: Coordinate, board: Board):
        if from_where.y == to_where.y:#ход по горизонтали
            step = 1
            if int(from_where.x) > int(to_where.x):
                step = -1
            for i in range(int(from_where.x) + step, int(to_where.x) - step, step):
                if board.board[int(from_where.y) - 1][i - 1] != None:
                    return False
            return True      


        elif int(from_where.x) == int(to_where.x):#ход по вертикали
            list_for_vertical = [i[from_where.x-1] for i in board.board]
            list_for_vertical_short = list_for_vertical[from_where.y:to_where.y]
            if len(list_for_vertical_short) < 1:
                return True
            step = 1
            if int(from_where.y) > int(to_where.y):
                step = -1
            for i in range(int(from_where.y) + step, int(to_where.y) - step, step):
                if list_for_vertical[i-1] != None:
                    return False
            return True      
            
        elif int(from_where.x)+int(from_where.y) == int(to_where.x)+int(to_where.y):
            isUp = 1
            if int(from_where.y) > int(to_where.y):
                isUp = -1
            for i in range(from_where.y + isUp, to_where.y + isUp, isUp):
                new_x = int(from_where.x) - isUp * abs(int(from_where.y) - i)
                new_y = i
                if board.board[new_y - 1][new_x - 1] != None:
                    return False
            return True

        elif int(from_where.x)-int(from_where.y) == int(to_where.x)-int(to_where.y):
            isUp = 1
            if int(from_where.y) > int(to_where.y):
                isUp = -1
            for i in range(int(from_where.y) + isUp, int(to_where.y) + isUp, isUp):
                new_x = int(from_where.x) +  isUp * abs(int(from_where.y) - i)
                new_y = i
                if board.board[new_y - 1][new_x - 1] != None:
                    return False
            return True

        return False

class Pawn(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'p'

    def can_go(self, from_where: Coordinate, to_where: Coordinate, board: Board, move_figure: bool):
        step = 2 if from_where.y == 2 and self.color == "w" or from_where.y == 7 and self.color == "b" else 1
        direction = 1 if self.color == 'w' else -1
        if abs(to_where.y - from_where.y) > step:
            return False
        
        if self.within_field(from_where) and self.within_field(to_where):
            if from_where.x == to_where.x and abs(to_where.y - from_where.y) <= step: # ход вперед 
                if board.have_free_space(to_where, self.color):
                    print('Can go" passed')
                    if self.have_enemy(to_where, board, move_figure) and move_figure:
                        board.increase_score(self.color)    
                    return True
                else:
                    return False

            elif  int(to_where.x) - int(from_where.x) == direction and abs(int(from_where.y) - int(to_where.y)) == direction:  #ход по диагонали, возможно только если есть противник на данной точке
                print('Can go" passed')
                if self.have_enemy(to_where, board, move_figure) and move_figure:
                    board.increase_score(self.color)
                return True
        else:
            print('Off the field. Try again')
            return False

class Knight(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'k'
    def can_go(self, from_where: Coordinate, to_where: Coordinate, board: Board,move_figure: bool):
        dx = abs(int(from_where.x) - int(to_where.x))
        dy = abs(int(from_where.y) - int(to_where.y))
        if self.within_field(from_where) and self.within_field(to_where):
            if board.have_free_space(to_where, self.color):
                if dx == 1 and dy == 2 or dx == 2 and dy == 1:
                    if move_figure:
                        print('Can go" passed')
                    if self.have_enemy(to_where, board,move_figure) and move_figure:
                        board.increase_score(self.color)
                    return True
            #         if not move_figure:
            #         return True
            #         if color == 'w':
            #         change_board(x, y, 'wk', board)
            #         return True
            #         if color == 'b':
            #         change_board(x, y, 'bk', board)
            #         return True
            # else:
                # return False
        else:
            return False
        


class Bishop(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'b'

    def can_go(self, from_where: Coordinate, to_where: Coordinate, board: Board, move_figure: bool):
         if self.within_field(from_where) and self.within_field(to_where):
            if board.have_free_space(to_where, self.color):
                if abs(from_where.x - to_where.x) == abs(from_where.y - to_where.y):
                    if self.road_free(from_where, to_where, board):
                        print('"Can go" passed')
                    if self.have_enemy(to_where, board, move_figure) and move_figure:
                        board.increase_score(self.color)
                    return True
            else:
                return False




class Rook(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'r'
    def can_go(self, from_where: Coordinate, to_where: Coordinate, board: Board, move_figure: bool):
        if self.within_field(to_where):
            if board.have_free_space(to_where, self.color) and self.road_free(to_where, from_where, board):
                if from_where.x == to_where.x or from_where.y == to_where.y:
                    print('Can go" passed')
                if self.have_enemy(to_where, board, move_figure) and move_figure:
                    board.increase_score(self.color)
                return True
        else:
            return False

    


class Queen(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'q'

    def can_go(self, from_where: Coordinate, to_where: Coordinate, board: Board, move_figure: bool):
        if self.road_free(to_where, from_where, board):
            if self.within_field(from_where) and self.within_field(to_where):
                if board.have_free_space(to_where, self.color):
                    if abs(from_where.x - to_where.x) == abs(from_where.y - to_where.y) or from_where.x == to_where.x or from_where.y == to_where.y:
                        print('"Can go" passed')
                    if self.have_enemy(to_where, board, move_figure) and move_figure:
                        board.increase_score(self.color)
                    return True
            else:
                return False    


class King(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'K'

    def can_go(self, from_where: Coordinate, to_where: Coordinate, board: Board, move_figure: bool):
        if self.road_free(to_where, from_where, board):
            if self.within_field(from_where) and self.within_field(to_where):
                if board.have_free_space(to_where, self.color):
                    if abs(from_where.x - to_where.x) <= 1 or abs(from_where.y - to_where.y) <= 1:
                        print('"Can go" passed')
                    if self.have_enemy(to_where, board, move_figure) and move_figure:
                        board.increase_score(self.color)
                    return True            
            else:
                return False


def make_move(figure: Figure, from_where, to_where, board: Board, move_figure = True):
    if figure.can_go(from_where, to_where, board, move_figure):
        if move_figure:
            board.change_board(from_where, to_where)
        return True
    else:
        return False


def get_coordinate(message, source, index, isFrom) -> Coordinate:
  coordinates = []
  if source == "keyboard":
    while True:
      try:
        coordinates = input(message).split(',')
        if coordinates[0] == "exit":
          return "exit"
        x = int(coordinates[0])
        y = int(coordinates[1])
        if x > 8 or x < 1 or y > 8 or y < 0:
          print("Invalid input")
          continue
        return Coordinate(x,y)
      except:
        print("Invalid input")
  else:
    try:
      command = source[index].split('-')
      if isFrom:
        coordinates = command[0].split(',')
      else:
        coordinates = command[1].split(',')
      if coordinates[0] == "exit":
          return "exit"

      x = int(coordinates[0])
      y = int(coordinates[1])
    except:
      raise ValueError("record file is invalid")
    if x > 8 or x < 1 or y > 8 or y < 0:
      raise ValueError("record file is invalid")
    return Coordinate(x,y)

def check_if_exit(command, record_file):
  if command == "exit":
    record_file.close()
    exit()

count_first_player = 0
count_second_player = 0
count_game = [0, 0]
black_king_position = Coordinate(5,8)
white_king_position = Coordinate(5,1)
game_over = False
index = 0

game_mode = input("Выберете режим игры (realtime, record): ")
input_source = "keyboard"
commands = []
if game_mode == "record":
  print("Выбран режим работы с записью игр")
  record_file = input("введите путь до файла с записью: ")
  with open(record_file, 'r') as record:
    raw = record.readlines()
    for line in raw:
      commands.append(line.rstrip("\n").rstrip())
  input_source = commands

board = Board()
board.chess_field()
 
new_record = open("game_record.txt", "w")
print('Белые ходят первые.')

while not game_over:
  while not game_over:
    print(f'Count game: [{count_game[0], count_game[1]}]')
    print('White move')
    while True:
        current_position_white = get_coordinate('Введите координату ваше положения(белый):', input_source, index, True)
        check_if_exit(current_position_white, new_record)
        white_player = board.get_figure(current_position_white)
        if white_player != None:
            break
        print("В выбранной точке нет фигуры.")
    future_position_white = get_coordinate('Введите координату, куда вы хотите сходить: ', input_source, index, False)
    check_if_exit(current_position_white, new_record)
    new_record.write(f"{current_position_white.x},{current_position_white.y}-{future_position_white.x},{future_position_white.y}\n")
    if input_source != 'keyboard' and len(commands) == index + 1:
      input_source = "keyboard"
    index += 1
    try:
      if make_move(white_player, current_position_white, future_position_white, board):
        count_game[0] += 1
        if white_player == "king":
          white_king_position = future_position_white
        board.chess_field()
        if make_move(white_player, future_position_white, black_king_position, board, move_figure = False):
          print("МАТ!")
        # break
      else:
        board.chess_field()
        continue
    except KingDefeated:
      print("Король побеждён! Вы выйграли")
      game_over = True
      new_record.close()

  while not game_over:
    print(f'Count game: [{count_game[0], count_game[1]}]')
    print('\n Black move')
    while True:
        current_position_black = get_coordinate('Введите координату ваше положения(белый):', input_source, index, True)
        check_if_exit(current_position_black, new_record)
        black_player = board.get_figure(current_position_black)
        if black_player != None:
            break
        print("В выбранной точке нет фигуры.")
    future_position_black = get_coordinate('Введите координату, куда вы хотите сходить: ', input_source, index, False)
    check_if_exit(current_position_black, new_record)
    new_record.write(f"{current_position_black.x},{current_position_black.y}-{future_position_black.x},{future_position_black.y}\n")
    if input_source != 'keyboard' and len(commands) == index + 1:
      input_source = "keyboard"
    index += 1
    try:
      if make_move(black_player, current_position_black, future_position_black, board):
        count_game[1] += 1
        board.chess_field()
        if black_player == "king":
          black_king_position = future_position_black
        if make_move(black_player, future_position_black, white_king_position, board, move_figure = False):
          print("МАТ!")
        break
      else:
        print('You cannot go here')
        board.chess_field()
        continue
    except KingDefeated:
      print("Король побеждён! Вы выйграли")
      game_over = True
      new_record.close()
