# task 1
# class Iter:
#
#     def __init__(self, list_num) -> None:
#         self.list_num = list_num
#         self.__counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         for i in self.list_num:
#             if self.__counter < len(self.list_num):
#                 self.__counter += 1
#                 print(i ** 2)
#             else:
#                 raise StopIteration
#
#
# user = int(input('Введите число: '))
# itr = Iter([i for i in range(1, user + 1)])


# def num_gen(number):
#     for i in number:
#         yield i**2
#
#
# user = int(input('Введите число: '))
# result = num_gen([i for i in range(1, user+1)])
# for j in result:
#     print(j)


# user = int(input('Введите число: '))
#
# num_gen = (num ** 2 for num in range(1, user+1))
# for i_num in num_gen:
#     print(i_num, end=' ')



# task 2
# def search_couple(first, second, num):
#     for x in first:
#         for y in second:
#             yield x, y
#             result = x * y
#             if result == num:
#                 return


# list_1 = [2, 5, 7, 10]
# list_2 = [3, 8, 4, 9]
# to_find = 56
# result_couple = search_couple(list_1, list_2, to_find)
# for i in result_couple:
#     print(i, end=' ')

# task 3
# import os
# from collections.abc import Iterable

# def gen_files_path(link: str, search: str):
#     for links, dirs, files in list(os.walk(link)):
#         for file in files:
#             yield links + '\\' + file
#             if links + '\\' + file == search:
#                 return                

# tree = gen_files_path("D:\Soft\Skillbox\Python exercises\module 26", 'D:\Soft\Skillbox\Python exercises\module 26\module26.py')

# for i in tree:
#     print(i)

# task 4

# class Task:
#     def __init__(self, num: list):
#         self.num = num[:]

#     def __iter__(self):
#         return self

#     def __next__(self):
#         try:
#             answer = self.num[-self.num[-1]] + self.num[-self.num[-2]]
#             self.num.append(answer)
#             return answer
#         except IndexError:
#             raise StopIteration


# result = Task([1, 1])
# for i in range(10):
#     print(next(result))

# task 5

# import os
# from collections.abc import Iterable
 
 
# def gen_files_dir(path: str, depth=1):
#     """Рекурсивно перебираем файлы и каталоги до определенной глубины"""
#     depth -= 1
#     with os.scandir(path) as p:
#         for entry in p:
#             yield entry.path
#             if entry.is_dir() and depth > 0:
#                 yield from gen_files_dir(entry.path, depth)
 
 
# if __name__ == '__main__':
#     directory = "D:\Soft\Skillbox\Python exercises\module 26" 
#     files = list(gen_files_dir(directory))
#     line_count = 0
 
#     for file_dir in files:
#         if not os.path.isfile(file_dir):
#             continue
 
#         files_filtered = [x for x in files if x.endswith('.py')]
#         for i in files_filtered:
#             file = open(i,"r",encoding='utf-8')
#             count = 0
#             for line in file.read().split('\n'):
#                     if (not line.strip() == '') and (not line.strip().startswith("#")) and (not line.strip().startswith('"')):
#                         count += 1                
#                         print('{} - {} строка'.format(file_dir, count))
#                     line_count += count
#                     file.close()

#     print("Всего строк  - ", line_count)

# task 6

class LinkedList:
    head = None

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node = None):
            self.element = element
            self.next_node = next_node

    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            return element
        node = self.head

        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)

        return element

    def assign(self, element, index):
        node = self.head
        i = 0

        while i < index:
            node = node.next_node
            i += 1

        node.element = element

    def insert(self, element, index):
        i = 0 
        node = self.head
        prev_node = self.head

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = self.Node(element, next_node=node)

        return element

    def get(self, index):
        i = 0 
        node = self.head
        prev_node = self.head

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        return node.element

    def out(self):
        node = self.head

        while node.next_node:
            print(node.element)
            node = node.next_node
        print(node.element)

    def delete(self, index):
        if index == 0:
            self.head = self.head.next_node

        node = self.head
        i = 0
        prev_node = node

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = node.next_node
        element = node.element 

        del node

        return element  

linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

linked_list.delete(0)
linked_list.append(10)
linked_list.assign(35, 0)
linked_list.out()