#1. Создать класс TrafficLight (светофор) и определить у него один атрибут
#color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
#В рамках метода реализовать переключение светофора в режимы: красный, желтый,
#зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
#второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
#Переключение между режимами должно осуществляться только в указанном порядке
#(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и
#вызвав описанный метод. Задачу можно усложнить, реализовав проверку порядка
#режимов, и при его нарушении выводить соответствующее сообщение и завершать
#скрипт.
print('1.')
from time import sleep
#import turtle as t
#t.down()
#t.color('red', 'red')
#t.begin_fill()
#t.circle(100)
#t.end_fill()
#t.mainloop()
class TrafficLight:
    __color = ['Red', 'Yellow', 'Green', 'Yellow']

    def running(self):
        i = 0
        while i < 4:
            print(f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(3)
            elif i == 3:
                sleep(2)
            i += 1
TrafficLight = TrafficLight()
TrafficLight.running()

#2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина),
#width (ширина). Значения данных атрибутов должны передаваться при создании
#экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы
#асфальта, необходимого для покрытия всего дорожного полотна. Использовать
#формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги
#асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
#Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

class MassCount(Road):
    def __init__(self, _length, _width, kgxm, height):
        super().__init__(_length, _width)
        self.kgxm = kgxm
        self.height = height

    def mass(self):
        return self._length * self._width * self.kgxm * self.height

weight = MassCount(5000, 20, 25, 0.005)
print(f'\n2.\nМасса асфальта: {int(weight.mass())} тонн')

#3. Реализовать базовый класс Worker (работник), в котором
#определить атрибуты: name, surname, position (должность),
#income (доход). Последний атрибут должен быть защищенным и
# ссылаться на словарь, содержащий элементы: оклад и премия,
#например, {"wage": wage, "bonus": bonus}. Создать класс
#Position (должность) на базе класса Worker. В классе Position
#реализовать методы получения полного имени сотрудника (get_full_name)
#и дохода с учетом премии (get_total_income). Проверить работу
#примера на реальных данных (создать экземпляры класса Position,
#передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

a = Position('Igor', 'Smith', 'Driver', 40000, 100000)
print(f'\n3.\nФИО: {a.get_full_name()}\nДолжность: {a.position}\nДоход: {a.get_total_income()}')

#4. Реализуйте базовый класс Car. У данного класса должны быть
#следующие атрибуты: speed, color, name, is_police (булево).
#А также методы: go, stop, turn(direction), которые должны сообщать,
#что машина поехала, остановилась, повернула (куда). Опишите
#несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#Добавьте в базовый класс метод show_speed, который должен
#показывать текущую скорость автомобиля. Для классов TownCar и
#WorkCar переопределите метод show_speed. При значении скорости
#свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
#о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов.
#Выполните доступ к атрибутам, выведите результат. Выполните
#вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начинает движение'

    def stop(self):
        return f'{self.name} останавливается'

    def turn_right(self):
        return f'{self.name} поворачивает направо'

    def turn_left(self):
        return f'{self.name} поворачивает налево'

    def show_speed(self):
        return f'Скорость {self.name}: {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name}:  {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} превышает допустимую для TownСar'
        else:
            return f'Скорость {self.name} допустимая для TownСar'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name}: {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышает допустимую для WorkCar'
        else:
            return f'Скорость {self.name} допустимая для WorkCar'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская'
        else:
            return f'{self.name} не полицейская'


Aston_Martin_Vanquish = SportCar(200, 'Red', 'Aston Martin', False)
Kia_Rio = TownCar(30, 'Yellow', 'Kia', False)
Citroen_Jumpy = WorkCar(65, 'White', 'Citroen', False)
Chevrolet_Camaro_SS = PoliceCar(90, 'Black', 'Chevrolet', True)

print('\n4.')
print(Aston_Martin_Vanquish.show_speed())
print(Kia_Rio.show_speed())
print(Citroen_Jumpy.show_speed())
print(Chevrolet_Camaro_SS.show_speed())