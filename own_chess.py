
class KingDefeated(Exception):
  def __init__(self):
    pass

# построение доски


empty_string = " ."

def chess_field(board):
  row_number = 8
  print()
  for row in reversed(board):
        print(row_number, end=" ")
        row_number -= 1
        for dot in row:
            if dot == '  ':
                print('  .', end="  ")
            else:
                print(" {} ".format(dot), end=" ")
        print(" ")
  print("  ", end="")
  for num in [1, 2, 3, 4, 5, 6, 7, 8]:
      print("  {}  ".format(num), end="")
  print("")

def create_board():
  board = []

  board.append(["wr","wk","wb","wq","wK","wb","wk","wr"])
  board.append(['wp' for _ in range(8)])
  for i in range(2, 6):
    board.append([empty_string]*8)
  board.append(['bp' for _ in range(8)])
  board.append(["br","bk","bb","bq","bK","bb","bk","br"])

  return board
board = create_board()
chess_field(board)


def change_board(x, y, figure, board):
  b = board[int(x[1])-1][int(x[0])-1]
  board[int(x[1])-1][int(x[0])-1] = ' .'
  board[int(y[1])-1][int(y[0])-1] = figure
  return True

def have_free_space(y,board, color):
  c = board[int(y[1])-1][int(y[0])-1]
  if board[int(y[1])-1][int(y[0])-1] == ' .' or board[int(y[1])-1][int(y[0])-1][0] != color:
    print('Having a free place passed')
    return True
  else:
    if board[int(y[1])-1][int(y[0])-1][0] == color:
      print('There is your figure')
      return False


def within_field(y):
  if 1 <= int(y[0]) <= 8:
    if 1 <= int(y[1]) <= 8:
      print('"Within the field" passed')
      return True

  else:
    print('"Within the field" is not passed')
    return False

def have_enemy(y, board, color, move_figure):
  place = board[int(y[1])-1][int(y[0])-1]
  if place[0] == ' ':
    print('It is not the enemy')
    return False
  if place[0] != color:
      print('It is the enemy')
      if place[1] == 'K' and move_figure:
        raise KingDefeated()
      return True
    

def road_free(x,y, board:list):
  if int(x[1]) == (int(y[1])):#ход по горизонтали
    # ind = (board[int(x[0])]).index(int(y[1]))
    step = 1
    if int(x[0]) > int(y[0]):
      step = -1
    for i in range(int(x[0]) + step, int(y[0]) - step, step):
      if board[int(x[1]) - 1][i - 1] != ' .':
        return False
    return True      


  elif int(x[0]) == int(y[0]):#ход по вертикали
    list_for_vertical = [i[int(x[0])-1] for i in board]
    list_for_vertical_short = list_for_vertical[int(x[1]):int(int(y[1]))]
    if len(list_for_vertical_short) < 1:
      return True
    step = 1
    if int(x[1]) > int(y[1]):
      step = -1
    for i in range(int(x[1]) + step, int(y[1]) - step, step):
      if list_for_vertical[i-1] != ' .':
        return False
    return True      
      
  elif int(x[0])+int(x[1]) == int(y[0])+int(y[1]):#по диагонали 
    isUp = 1
    if int(x[1]) > int(y[1]):
      isUp = -1
    for i in range(int(x[1]) + isUp, int(y[1]) + isUp, isUp):
      new_x = int(x[0]) - isUp * abs(int(x[1]) - i)
      new_y = i
      if board[new_y - 1][new_x - 1] != ' .':
        return False
    return True

  elif int(x[0])-int(x[1]) == int(y[0])-int(y[1]):
    isUp = 1
    if int(x[1]) > int(y[1]):
      isUp = -1
    for i in range(int(x[1]) + isUp, int(y[1]) + isUp, isUp):
      new_x = int(x[0]) +  isUp * abs(int(x[1]) - i)
      new_y = i
      if board[new_y - 1][new_x - 1] != ' .':
        return False
    return True

  return False   

  
def can_pawn_go(x, y, board, count, color, move_figure):
  step = 2 if int(x[1]) == 2 and color == "w" or int(x[1]) == 7 and color == "b" else 1
  direction = 1 if color == 'w' else -1
  if int(y[1]) - int(x[1]) * direction < 0:
    return False
  
  if within_field(y) == True:
    if int(x[0]) == int(y[0]) and abs(int(y[1]) - int(x[1])) <= step: # ход вперед 
      if have_free_space(y, board, color):
        print('Can go" passed')
        if have_enemy(y, board, color, move_figure) and move_figure:
          count += 1
          print(f'There is the enemy. Score: {count}')
        if not move_figure:
          return True
        if color == 'w':
          change_board(x, y, 'wp', board)
          return True
        if color == 'b':
          change_board(x, y, 'bp', board)
          return True
        
      else:
        return False


    elif  int(y[0]) - int(x[0]) == direction and abs(int(x[1]) - int(y[1])) == direction:  #ход по диагонали, возможно только если есть противник на данной точке
        print('Can go" passed')
        if have_enemy(y, board, color, move_figure) and move_figure:
          count += 1
          print(f'There is the enemy. Score: {count}')
        if not move_figure:
          return True
        if color == 'w':
          change_board(x, y, 'wp', board)
          return True
        if color == 'b':
          change_board(x, y, 'bp', board)
          return True

  else:
    print('Off the field. Try again')
    return False

def can_khight_go(x, y, board, count, color, move_figure):
  dx = abs(int(x[0]) - int(y[0]))
  dy = abs(int(x[1]) - int(y[1]))
  if within_field(y):
    if have_free_space(y, board, color):
      if dx == 1 and dy == 2 or dx == 2 and dy == 1:
        if move_figure:
          print('Can go" passed')
        if have_enemy(y, board, color, move_figure) and move_figure:
          count += 1
          print(f'There is the enemy. Score: {count}')
        if not move_figure:
          return True
        if color == 'w':
          change_board(x, y, 'wk', board)
          return True
        if color == 'b':
          change_board(x, y, 'bk', board)
          return True
      else:
          return False
    else:
          return False


def can_rook_go(x, y, board, count, color, move_figure):
  if within_field(y):
    if have_free_space(y, board, color) and road_free(x, y, board):
      if int(x[0]) == int(y[0]) or int(x[1]) == int(y[1]):
        print('Can go" passed')
        if have_enemy(y, board, color, move_figure) and move_figure:
          count += 1
          print(f'There is the enemy. Score: {count}')
        if not move_figure:
          return True
        if color == 'w':
          change_board(x, y, 'wr', board)
          return True
        if color == 'b':
          change_board(x, y, 'br', board)
          return True
      else:
          return False
    else:
        return False

  else:
    return False


def can_bishop_go(x, y, board, count, color, move_figure):
  if within_field(y):
    if have_free_space(y, board, color):
      if abs(int(x[0]) - int(y[0])) == abs(int(x[1]) - int(y[1])):
        if road_free(x, y, board):
          print('"Can go" passed')
          if have_enemy(y, board, color, move_figure) and move_figure:
            count += 1
            print(f'There is the enemy. Score: {count}')
          if not move_figure:
            return True
          if color == 'w':
            change_board(x, y, 'wb', board)
            return True
          if color == 'b':
            change_board(x, y, 'bb', board)
            return True
        else:
          return False
    else:
          return False



def can_queen_go(x, y, board, count, color, move_figure):
  if road_free(x,y, board):
    if within_field(y):
        if have_free_space(y, board, color):
          if abs(int(x[0]) - int(y[0])) == abs(int(x[1]) - int(y[1])) or int(x[0]) == int(y[0]) or int(x[1]) == int(y[1]):
            print('"Can go" passed')
            if have_enemy(y, board, color, move_figure) and move_figure:
              count += 1
              print(f'There is the enemy. Score: {count}')
            if not move_figure:
              return True
            if color == 'w':
              change_board(x, y, 'wq', board)
              return True
            if color == 'b':
              change_board(x, y, 'bq', board)
              return True
          else:
            return False
        else:

            return False
    else:
      return False

def can_do_castling(board, from_p, to_p, color):
  possible_to_positions = [
    white_left_rook_start_pos,
    white_right_rook_start_pos,
    black_left_rook_start_pos,
    black_right_rook_start_pos
  ]
  if to_p in possible_to_positions:
    if get_color(board, from_p) == 'w':
      if not castling_conditions['white_king']:
        return False
      if get_figure(board, to_p) == "rook" and get_color(board, to_p) == color:
        rook = "white_left_rook" if to_p == white_left_rook_start_pos else "white_right_rook"
        return castling_conditions[rook]
    else:
      if not castling_conditions['black_king']:
        return False
      if get_figure(board, to_p) == "rook" and get_color(board, to_p) == color:
        rook = "black_left_rook" if to_p == black_left_rook_start_pos else "black_right_rook"
        return castling_conditions[rook]

def do_castling(board, king_pos, rook_pos):
  if get_color(board, king_pos) == "w":
    king = "wK"
    rook = "wr"
    if rook_pos == white_left_rook_start_pos:
      change_board(king_pos, ["3","1"], king, board)
      change_board(rook_pos, ["4","1"], rook, board)
    if rook_pos == white_right_rook_start_pos:
      change_board(king_pos, ["7","1"], king, board)
      change_board(rook_pos, ["6","1"], rook, board)
  else:
    king = "bK"
    rook = "br"
    if rook_pos == black_left_rook_start_pos:
      change_board(king_pos, ["3","8"], king, board)
      change_board(rook_pos, ["4","8"], rook, board)
    if rook_pos == black_right_rook_start_pos:
      change_board(king_pos, ["7","8"], king, board)
      change_board(rook_pos, ["6","8"], rook, board)

def can_king_go(x, y, board, count, color, move_figure):
  if road_free(x,y, board):
    if within_field(y):
        if can_do_castling(board, x, y, color):
          do_castling(board, x, y)
          return True
        if have_free_space(y, board, color):
          if abs(int(x[0]) - int(y[0])) <= 1 and abs(int(x[1]) - int(y[1])) <= 1:
            print('"Can go" passed')
            if have_enemy(y, board, color, move_figure) and move_figure:
              count += 1
              print(f'There is the enemy. Score: {count}')
            if color == 'w':
              if move_figure:
                change_board(x, y, 'wK', board)
              return True
            if color == 'b':
              if move_figure:
                change_board(x, y, 'bK', board) 
              return True
          else:
            return False
        else:
            return False
      
    else:
      return False

def get_color(board, position):
  value = board[int(position[1]) - 1][int(position[0]) - 1]
  return value[0]


def get_figure(board, position):
  value = board[int(position[1]) - 1][int(position[0]) - 1]
  figure = value[1]
  if figure == 'b':
    return "bishop"
  if figure == 'p':
    return "pawn"
  if figure == 'r':
    return "rook"
  if figure == 'k':
    return 'knight'
  if figure == 'q':
    return "queen"
  if figure == 'K':
    return "king"

def right_place(x,board,figure):
  if board[int(x[1])-1][int(x[0])-1] == figure:
    return True
  else:
    print('Figure is not here')
    return False

def figure_definition(figure, x, y, board, count, color, move_figure = True):
  if figure == 'rook':
    figure = color + figure[0]
    if right_place(x,board,figure):
      return can_rook_go(x, y, board, count,color, move_figure)
    else:
      return False
  if figure == 'knight':
    figure = color + figure[0]
    if right_place(x,board,figure):
      return can_khight_go(x, y, board, count,color, move_figure)
    else:
      return False
  if figure == 'bishop':
    figure = color + figure[0]
    if right_place(x,board,figure):
      return can_bishop_go(x, y, board, count,color, move_figure)
    else:
      return False
  if figure == 'queen':
    figure = color + figure[0]
    if right_place(x,board,figure):
      return can_queen_go(x, y, board, count,color, move_figure)
    else:
      return False
  if figure == 'king':
    figure = color + "K"
    if right_place(x,board,figure):
      return can_king_go(x, y, board, count,color, move_figure)
    else:
      return False
  if figure == 'pawn':
    figure = color + figure[0]
    if right_place(x,board,figure):
      return can_pawn_go(x, y, board, count,color, move_figure)
    else:
      return False

def get_coordinate(message, source, index, isFrom):
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
        return coordinates
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
  return coordinates

def check_if_exit(command, record_file):
  if command == "exit":
    record_file.close()
    exit()

    

count_first_player = 0
count_second_player = 0
count_game = [0, 0]
black_king_position = ["5","8"]
white_king_position = ["5","1"]
black_king_moved = False
white_king_moved = False
castling_conditions = { 
  "white_king": True,
  "black_king": True,
  "white_left_rook": True,
  "white_right_rook": True,
  "black_left_rook": True,
  "black_right_rook": True
 }

white_left_rook_start_pos = '1,1'.split(',')
white_right_rook_start_pos = '8,1'.split(',')
black_left_rook_start_pos = '1,8'.split(',')
black_right_rook_start_pos = '8,8'.split(',')
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
  
new_record = open("game_record.txt", "w")
print('Белые ходят первые.')
while not game_over:
  while not game_over:
    print(f'Count game: [{count_game[0], count_game[1]}]')
    print('White move')
    current_position_white = get_coordinate('Введите координату ваше положения(белый):', input_source, index, True)
    check_if_exit(current_position_white, new_record)
    white_player = get_figure(board, current_position_white)
    future_position_white = get_coordinate('Введите координату, куда вы хотите сходить: ', input_source, index, False)
    check_if_exit(current_position_white, new_record)
    new_record.write(f"{current_position_white[0]},{current_position_white[1]}-{future_position_white[0]},{future_position_white[0]}\n")
    if input_source != 'keyboard' and len(commands) == index + 1:
      input_source = "keyboard"
    index += 1
    try:
      if figure_definition(white_player, current_position_white, future_position_white, board, count_first_player, color = 'w'):
        count_game[0] += 1
        if white_player == "king":
          white_king_position = future_position_white
          castling_conditions['white_king'] = False
        if white_player == 'rook':
          rook = "white_left_rook" if current_position_white == white_left_rook_start_pos else "white_right_rook"
          castling_conditions[rook] = False
        chess_field(board)
        if figure_definition(white_player, future_position_white, black_king_position, board, count_first_player, color = 'w', move_figure = False):
          print("МАТ!")
        break
      else:
        chess_field(board)
        continue
    except KingDefeated:
      print("Король побеждён! Вы выйграли")
      game_over = True
      new_record.close()

  while not game_over:
    print('\n Black move')
    current_position_black = get_coordinate('Введите координату ваше положения(черный):', input_source, index, True)
    check_if_exit(current_position_black, new_record)
    black_player = get_figure(board, current_position_black)
    future_position_black = get_coordinate('Введите координату, куда вы хотите сходить: ', input_source, index, False)
    check_if_exit(current_position_black, new_record)
    new_record.write(f"{current_position_black[0]},{current_position_black[1]}-{future_position_black[0]},{future_position_black[0]}\n")
    if input_source != 'keyboard' and len(commands) == index + 1:
      input_source = "keyboard"
    index += 1
    try:
      if figure_definition(black_player, current_position_black, future_position_black, board, count_first_player, color = 'b'):
        count_game[1] += 1
        chess_field(board)
        if black_player == "king":
          black_king_position = future_position_black
          castling_conditions['black_king'] = False
        if black_player == 'rook':
          rook = "black_left_rook" if current_position_black == black_left_rook_start_pos else "black_right_rook"
          castling_conditions[rook] = False
        if figure_definition(black_player, future_position_black, white_king_position, board, count_first_player, color = 'b', move_figure = False):
          print("МАТ!")
        break
      else:
        print('You cannot go here')
        chess_field(board)
        continue
    except KingDefeated:
      print("Король побеждён! Вы выйграли")
      game_over = True
      new_record.close()

if not new_record.closed:
  new_record.close()

