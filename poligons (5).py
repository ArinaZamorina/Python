import itertools
from math import pi, sin, cos, tan

import matplotlib.pyplot as plt

class Figure():

	def __init__(self, count: int = 10, start: int = 0, step: int = 2, step_y = 0, hight: int = 0, size: int = 1):
		self.count = count
		self.start = start
		self.step = step + size
		self.step_y = step_y
		self.hight = hight
		self.size = size
		self.index = -1

	def _step_y(self):
		return self.step_y * self.index

	def _gen(self, figure_gen):
		l1 = map(lambda x: figure_gen(x), itertools.count(self.start, self.step))
		i = 0
		list_coor = []
		for t in l1:
			if i >= self.count:
				print(f"Сгенерированно {i} фигур")
				break
			else:
				i += 1
				list_coor.append(t)
		return list_coor
	
	def gen(self):
		pass

	def translate(figure: tuple, distance: int = 5) -> tuple:
		first = figure[0]
		last = figure[-2]
		sin_my = (last[1]-first[1]/(((last[1]-first[1]) ** 2 + (last[0]-first[0]) ** 2)) ** 0.5)
		cos_my = (last[0]-first[0]/(((last[1]-first[1]) ** 2 + (last[0]-first[0]) ** 2)) ** 0.5)
		figure_new = map(lambda x: (x[0] - distance * sin_my, x[1] + distance * cos_my), figure)
		return tuple(figure_new)

	# поворот
	def rotate(figure: tuple, angle: int = 45, dot: tuple = (0, 0)) -> tuple:
		sin_my = round(sin(pi*angle/180), 7)
		cos_my = round(cos(pi*angle/180), 7)
		figure_new = map(lambda x: (dot[0] + (x[0] - dot[0]) * cos_my - (x[1] - dot[1]) * sin_my,
							dot[1] + (x[0] - dot[0]) * sin_my + (x[1] - dot[1]) * cos_my), figure)
		return tuple(figure_new)

	def __get_center(figure: tuple) -> tuple:
		first = figure[0]
		last = figure[-2]
		angle_count = len(figure)
		angle = pi * (angle_count - 2)/(2 * angle_count)
		sin_my = round(sin(angle), 7)
		cos_my = round(cos(angle), 7)
		x_center = first[0] + (last[0]- first[0]) * cos_my/((2*cos_my) ) - (last[1]- first[1]) * sin_my/((2*cos_my) )
		y_center = first[1] + (last[0]- first[0]) * sin_my/((2*cos_my) ) + (last[1]- first[1]) * cos_my/((2*cos_my))
		return (x_center, y_center)


	# sym
	def symmetry(figure: tuple, distance: int = 5) -> tuple:
		figure_new_1 = Figure.translate(figure=figure, distance=distance)
		dot = Figure.__get_center(figure=figure_new_1)
		figure_new_2 = Figure.rotate(figure=figure_new_1, angle=180, dot=dot)
		return figure_new_2

	# get parametr
	def __get_line(vector: tuple, dot: tuple) -> tuple():
		a = - vector[1]
		b = vector[0]
		c = dot[0] * vector[1] - dot[1] * vector[0]
		return a, b, c

	# sign
	def __sign(num: float) -> int: #положительное и отрицательное
		if (round(num, 7) == 0):
			return 0
		if num > 0:
			return 1
		elif num < 0: 
			return -1
		else:
			return 0 

	# гомотетия после параллельного переноса
	def __homothety(coord: tuple, angle: int , dot: tuple , vector: tuple, vect: tuple) -> tuple:
		a, b, c = Figure.__get_line(vector=vect, dot=coord)
		distance = - (a * dot[0] + b * dot[1] + c)/(((a ** 2) + (b ** 2)) ** 0.5)
		a, b, c = Figure.__get_line(vector=vector, dot=dot)
		sign = Figure.__sign(- (a * coord[0] + b * coord[1] + c)/(((a ** 2) + (b ** 2)) ** 0.5))
		distance_n = (distance) * round(tan(pi*angle/180), 7)
		dot_new = (dot[0] + vector[0] * (distance) + sign * vect[0] * distance_n,
					dot[1] + vector[1] * (distance) + sign * vect[1] * distance_n)
		return dot_new
	
	def __make_line(figure: tuple, a: float, b: float, c: float) -> tuple:
		list_my = []
		i=0
		for dot in figure:
			if round(dot[0] * a + dot[1] * b + c, 7) == 0:
				if i>=len(figure)/2:
					list_my.append((dot[0] + 0.02, dot[1] + 0.03))
					list_my.append((dot[0] - 0.02, dot[1] - 0.03))
				else:
					list_my.append((dot[0] - 0.02, dot[1] - 0.03))
					list_my.append((dot[0] + 0.02, dot[1] + 0.03))
			else:
				list_my.append(dot)
			i+=1
		return tuple(list_my)

	
	def homothety(figure: tuple, angle: int = 45, dot: tuple = (0, 0)) -> tuple:
		first = figure[0]
		last = figure[-2]
		vector = (last[0] - first[0]/((((last[0] - first[0]) ** 2) + ((last[1] - first[1]) ** 2)) ** 0.5),
				 last[1] - first[1]/((((last[0] - first[0]) ** 2) + ((last[1] - first[1]) ** 2)) ** 0.5))
		a, b, c = Figure.__get_line(vector=vector, dot=dot)
		center = Figure.__get_center(figure=figure)
		distance = - (a * center[0] + b * center[1] + c)/(((a ** 2) + (b ** 2)) ** 0.5)
		figure_new_1 = Figure.translate(figure=figure, distance=distance)
		figure_new_2 = Figure.__make_line(figure=figure_new_1, a=a, b=b, c=c)
		vect = (last[1] - first[1]/((((last[0] - first[0]) ** 2) + ((last[1] - first[1]) ** 2)) ** 0.5), 
					first[0] - last[0]/((((last[0] - first[0]) ** 2) + ((last[1] - first[1]) ** 2)) ** 0.5))
		figure_new_3 = list(map(lambda x: Figure.__homothety(
										coord=x, angle=angle, dot=dot, vector=vector, vect=vect), figure_new_2))
		figure_new_3[-1] = figure_new_3[0]
		return figure_new_3


class Rectangle(Figure):
	def __init__(self, count: int = 10, start: int = 0, step: int = 2, step_y: int = 0, hight: int = 0, size: int = 1, width: int = 1):
		super().__init__(count, start, step, step_y, hight, size)
		self.width = width
		self.step = step + width

	def gen(self) -> list:
		def __rectangle(x) -> tuple:
			self.index += 1
			return ((x, self.hight + self._step_y()), (x, self.size + self.hight + self._step_y()) , (x + self.width, self.size + self.hight + self._step_y()), (x + self.width, self.hight + self._step_y()), (x, self.hight + self._step_y()))
		list_my = self._gen(__rectangle)
		return list_my


class Hexagon(Figure):
	def __init__(self, count: int = 10, start: int = 0, step: int = 2, step_y: int = 0, hight: int = 0, size: int = 1, width: int = 2):
		super().__init__(count, start, step, step_y, hight, size)

	def gen(self) -> list:
		def __hexagon(x) -> tuple:
			self.index += 1
			return ((x, self.hight + self._step_y()), (x - 1/2 * self.size, ((3 ** 0.5) / 2) * self.size + self.hight + self._step_y()), (x, (3 ** 0.5) * self.size + self.hight + self._step_y()), 
					(x + self.size, (3 ** 0.5) * self.size + self.hight + self._step_y()), (x + 3/2 * self.size, ((3 ** 0.5) / 2) * self.size + self.hight + self._step_y()) , (x + self.size, self.hight + self._step_y()),(x, self.hight + self._step_y()))
		list_my = self._gen(__hexagon)
		return list_my


class Triangle(Figure):
	def __init__(self, count: int = 10, start: int = 0, step: int = 2, step_y: int = 0, hight: int = 0, size: int = 1, width: int = 2):
		super().__init__(count, start, step, step_y, hight, size)

	def gen(self) -> list:
		def __triangle(x) -> tuple:
			self.index += 1
			return ((x, self.hight + self._step_y()), (x + 1/2 * self.size, ((3 ** 0.5) / 2) * self.size + self.hight + self._step_y()) , (x + self.size, self.hight + self._step_y()),(x, self.hight + self._step_y()))
		list_my = self._gen(__triangle)
		return list_my


# функция отрисовки множества фигур
def show(figures):
	plt.grid()
	for figure in figures:
		preppare_one(figure)
		
	plt.show()

def preppare_one(figure):
	plt.plot(*zip(*figure))
	plt.plot(*zip(figure[0]))
	plt.fill_between(list(dot[0] for dot in figure), list(dot[1] for dot in figure))


# 2.1
show(Rectangle(count=4, start=5, hight=3, width=2, size=4, step_y= 2).gen())
preppare_one(Rectangle(count=4, start=5, hight=3).gen()[0])
plt.show()

# 2.2
show(Triangle(count=3, start=3, hight=10, size=4, step_y = 2).gen())

# 2.3
show(Hexagon(count=5, step=4, size=1.5, step_y=2).gen())

# 2.4
figure_7 = itertools.chain(Hexagon(count=1, step=4).gen(), Triangle(count=1, start=18).gen(),
Rectangle(count=2, hight=2).gen(), Hexagon(count=3,  start=1, step=4, hight=2).gen())
show(figure_7)

# 3.1
tr_translate = list(itertools.chain(Hexagon(count=5).gen(),
list(map(lambda x: Figure.translate(x, distance=-10), Hexagon(count=5).gen()))))
show(tr_translate)


# 3.2
tr_rotate = list(itertools.chain(Hexagon(count=5, step=3, size=1.5).gen(),
list(map(lambda x: Figure.rotate(x), Hexagon(count=5, step=3, size=1.5).gen()))))
show(tr_rotate)

# 3.3
tr_symmetry = list(itertools.chain(Rectangle(count=5).gen(),
list(map(lambda x: Figure.symmetry(x), Rectangle(count=5).gen()))))
show(tr_symmetry)
symmetry_list = list(itertools.chain(list(map(lambda x: Figure.rotate(x), Triangle(count=5).gen())),
list(map(lambda x: Figure.symmetry(x, distance=2.5), list(map(lambda x: Figure.rotate(x), Triangle(count=5).gen()))))))
show(tr_symmetry)

# 3.4 
# tr_homothety = list(itertools.chain(Hexagon(count=5, step=2.2).gen(),
# list(map(lambda x: Figure.homothety(x,dot=(5, 1)), Hexagon(count=5, step=2).gen()))))
# show(tr_homothety)
# tr_homothety = list(itertools.chain(list(map(lambda x: Figure.rotate(x), Rectangle(count=2).gen())),
# list(map(lambda x: Figure.homothety(x, dot=(0, 3)), list(map(lambda x: Figure.rotate(x), Rectangle(count=2).gen()))))))
# show(tr_homothety)

# 4.1
tr_translate = list(itertools.chain(list(map(lambda x: Figure.rotate(x), Rectangle(count=10).gen())),
list(map(lambda x: Figure.translate(x, distance=5), list(map(lambda x: Figure.rotate(x, angle=45), Rectangle(count=10).gen())))),
list(map(lambda x: Figure.translate(x, distance=-5), list(map(lambda x: Figure.rotate(x), Rectangle(count=10).gen()))))))
show(tr_translate)

# 4.2
tr_rotate = list(itertools.chain(list(map(lambda x: Figure.translate(x), Rectangle().gen())),
list(map(lambda x: Figure.rotate(x, dot=(5,0)), Rectangle().gen()))))
show(tr_rotate)

# 4.3
tr_symmetry = list(itertools.chain(Triangle().gen(),
list(map(lambda x: Figure.symmetry(x), Triangle().gen()))))
show(tr_symmetry)

# 4.4
tr_homothety = list(map(lambda x: Figure.homothety(x, angle=30), list(map(lambda x: Figure.rotate(x), Rectangle(count=5, start=1).gen()))))
tr_homothety1 = list(itertools.chain(list(map(lambda x: Figure.rotate(x, angle=180), tr_homothety)),
tr_homothety))
show(tr_homothety1)
