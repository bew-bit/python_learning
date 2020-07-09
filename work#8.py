#1. Реализовать класс «Дата», функция-конструктор которого
#должна принимать дату в виде строки формата «день-месяц-год».
#В рамках класса реализовать два метода. Первый, с декоратором
#@classmethod, должен извлекать число, месяц, год и преобразовывать
#их тип к типу «Число». Второй, с декоратором @staticmethod,
#должен проводить валидацию числа, месяца и года
#(например, месяц — от 1 до 12). Проверить работу полученной
#структуры на реальных данных.
class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return f'{int(my_date[0])}.{int(my_date[1])}.{int(my_date[2])}'

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                return 'дата существует'
            else:
                return 'месяц указан неверно'
        else:
            return 'число указано неверно'

    def __str__(self):
        return f'дата {Date.extract(self.day_month_year)}'


today = Date('31 - 1 - 3020')
print(f'1.\n{today}')
print(Date.valid(11, 11, 2022))
print(Date.extract('11 - 11 - 2011'))
print(today.extract('11 - 11 - 2020'))
print(Date.valid(1, 11, 1675))

#2. Создайте собственный класс-исключение, обрабатывающий
#ситуацию деления на нуль. Проверьте его работу на данных,
#вводимых пользователем. При вводе пользователем нуля в качестве
#делителя программа должна корректно обработать эту ситуацию
#и не завершиться с ошибкой.
class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return 'На ноль делить нельзя'


print('\n2.')
a = int(input('введите делимое: '))
b = int(input('введите делитель: '))
print(DivisionByNull.divide_by_null(a, b))

#3. Создайте собственный класс-исключение, который должен проверять
#содержимое списка на наличие только чисел. Проверить работу
#исключения на реальном примере. Необходимо запрашивать у пользователя
#данные и заполнять список. Класс-исключение должен контролировать
#типы данных элементов списка.
class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = float(input('Введите число и нажмите Enter: '))
                self.my_list.append(val)
                print(f'Список: {self.my_list}\n')
            except:
                print(f'Не допустимы элементы типа строка и булево')
                y_or_n = input(f'Продолжить? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'завершение ввода'
                else:
                    return f'завершение ввода'

try_except = Error(1)
print('\n3.')
print(try_except.my_input())

#4. Начните работу над проектом «Склад оргтехники». Создайте
#класс, описывающий склад. А также класс «Оргтехника», который
#будет базовым для классов-наследников. Эти классы — конкретные
#типы оргтехники (принтер, сканер, ксерокс). В базовом классе
#определить параметры, общие для приведенных типов. В классах-наследниках
#реализовать параметры, уникальные для каждого типа оргтехники.
#5. Продолжить работу над первым заданием. Разработать методы,
#отвечающие за приём оргтехники на склад и передачу в определенное
#подразделение компании. Для хранения данных о наименовании и
#количестве единиц оргтехники, а также других данных, можно использовать
#любую подходящую структуру, например словарь.
#6. Продолжить работу над вторым заданием. Реализуйте механизм
#валидации вводимых пользователем данных. Например, для указания
#количества принтеров, отправленных на склад, нельзя использовать
#строковый тип данных.
#Подсказка: постарайтесь по возможности реализовать в проекте
#«Склад оргтехники» максимум возможностей, изученных на уроках
#по ООП.
class Storage:

    def __init__(self, name, price, qty, lists, *args):
        self.name = name
        self.price = price
        self.qty = qty
        self.lists = lists
        self.a_store_full = []
        self.a_store = []
        self.a_unit = {'Модель': self.name, 'Цена за ед': self.price, 'Кол-во': self.qty}

    def __str__(self):
        return f'{self.name} цена {self.price} кол-во {self.qty}'

    def reception(self):
        try:
            unit = input(f'Введите модель: ')
            unit_p = int(input(f'Введите цену за ед: '))
            unit_q = int(input(f'Введите количество: '))
            unique = {'Модель': unit, 'Цена за ед': unit_p, 'Кол-во': unit_q}
            self.a_unit.update(unique)
            self.a_store.append(self.a_unit)
            print(f'Текущий перечень:\n{self.a_store}')
        except:
            return f'Ошибка ввода'

        print(f'Для выхода - q, продолжить - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.a_store_full.append(self.a_store)
            print(f'Склад:\n{self.a_store_full}')
            return f'Выход'
        else:
            return Storage.reception(self)


class Printer(Storage):
    def to_print(self):
        return f'напечатать {self.lists} листа(ов)'


class Scanner(Storage):
    def to_scan(self):
        return f'сканировать {self.lists} листа(ов)'


class Copier(Storage):
    def to_copier(self):
        return f'копировать {self.lists} листа(ов)'


unit_1 = Printer('Brother', 20000, 10, 10)
unit_2 = Scanner('hp', 5000, 1, 10)
unit_3 = Copier('Xerox', 150000, 5, 20)
print('\n4.;5.;6.')
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())

#7. Реализовать проект «Операции с комплексными числами».
#Создайте класс «Комплексное число», реализуйте перегрузку
#методов сложения и умножения комплексных чисел. Проверьте
#работу проекта, создав экземпляры класса (комплексные числа)
#и выполнив сложение и умножение созданных экземпляров.
#Проверьте корректность полученного результата.
class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.n = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма n1 и n2:')
        return f'{self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение n1 и n2:')
        return f'{self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'n = {self.a} + {self.b} * i'

n1 = ComplexNumber(1, 2)
n2 = ComplexNumber(-3, 4)
print('\n7.')
print(n1)
print(n1 + n2)
print(n1 * n2)