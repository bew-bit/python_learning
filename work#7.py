# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку
#конструктора класса (метод __init__()), который должен принимать
#данные (список списков) для формирования матрицы.
class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):
            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

my_matrix = Matrix([[1, 2, 3],
                    [6, 5, 4],
                    [4, 2, 5]],
                   [[3, 6, 1],
                    [6, 5, 3],
                    [2, 4, 1]])

print(f'1.\n{my_matrix.__add__()}\n')

#2. 2. Реализовать проект расчета суммарного расхода ткани на
#производство одежды. Основная сущность (класс) этого проекта
#— одежда, которая может иметь определенное название. К типам
#одежды в этом проекте относятся пальто и костюм. У этих типов
#одежды существуют параметры: размер (для пальто) и рост (для костюма).
#Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать
#формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
#Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани. Проверить на практике
#полученные на этом уроке знания: реализовать абстрактные классы
#для основных классов проекта, проверить на практике работу декоратора
#@property.
class Cut:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_coat(self):
        return self.size / 6.5 + 0.5

    def get_suit(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return (self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)

class Coat(Cut):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.coat = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Отрез на пальто: {self.coat}'


class Suit(Cut):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.suit = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Отрез на костюм: {self.suit}'

coat = Coat(8, 12)
suit = Suit(4, 12)
print(f'2.\n{coat}\n{suit}\n')

#3. Реализовать программу работы с органическими клетками.
#Необходимо создать класс Клетка. В его конструкторе инициализировать
#параметр, соответствующий количеству клеток (целое число). В классе
#должны быть реализованы методы перегрузки арифметических операторов:
#сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
#деление (__truediv__()).Данные методы должны применяться только
#к клеткам и выполнять увеличение, уменьшение, умножение и обычное
#(не целочисленное) деление клеток, соответственно. В методе деления
#должно осуществляться округление значения до целого числа.
#class Cell:
#    def __init__(self, qty):
#        self.qty = int(qty)
#
#    def __add__(self, other):
#        return self.qty + other.qty
#
#    def __sub__(self, other):
#        return self.qty - other.qty
#
#    def __mul__(self, other):
#        return int(self.qty * other.qty)
#
#    def __truediv__(self, other):
#        return round(self.qty // other.qty)
#
#    def make_order(self, cell_row):
#        row = ''
#        for i in range(int(self.qty / cell_row)):
#            row += f'{"*" * cell_row}\n'
#        row += f'{"*" * (self.qty % cell_row)}'
#        return row

#cell_1 = Cell(2)
#cell_2 = Cell(8)
#print(cell_1)