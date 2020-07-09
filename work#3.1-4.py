#1. Реализовать функцию, принимающую два числа
#(позиционные аргументы) и выполняющую их деление.
#Числа запрашивать у пользователя, предусмотреть
#обработку ситуации деления на ноль.
def division(var_1, var_2):
    try:
        return var_1/var_2
    except ZeroDivisionError:
        return 'делитель равен 0'
res=division(float(input('1. введите делимое: ')), float(input('введите делитель: ')))
print(f'Результат деления: {res}')
#2. Реализовать функцию, принимающую несколько
#параметров, описывающих данные пользователя: имя, фамилия,
#год рождения, город проживания, email, телефон. Функция
#должна принимать параметры как именованные аргументы.
#Реализовать вывод данных о пользователе одной строкой.
def user_data(name, surname, b_year, location, email, phone_n):
    print(f'2. name - {name}, surname - {surname}, b_year - {b_year}, location - {location}, email - {email},'
          f'phone_n - {phone_n}')
user_data(name='Ivan', surname='Ivanov', b_year='1979', location='Sochi', email='i.ivanov@job.com', phone_n='+12354561')
#3. Реализовать функцию my_func(), которая принимает
#три позиционных аргумента, и возвращает сумму
#наибольших двух аргументов.
def summ(var_1, var_2, var_3):
    if var_1 <= var_2 and  var_1 <= var_3:
        return var_2+var_3
    elif var_2 < var_1 and var_2 < var_3:
        return var_1+var_3
    else:
        return var_1+var_2
print(f'Сумма двух наибольших чисел - '
      f'{summ(float(input("3. Введите число ")), float(input("Введите 2е число ")), float(input("Введите 3е число ")))}')
#4.Программа принимает действительное положительное
#число x и целое отрицательное число y. Необходимо
#выполнить возведение числа x в степень y. Задание
#необходимо реализовать в виде функции my_func(x, y).
#При решении задания необходимо обойтись без встроенной
#функции возведения числа в степень.
#Способ 1:
def my_func(x, y):
    return 1 / x ** abs(y)
print(f'4.1. X(3) в степени Y(-5) = {my_func(3,-5)}')
#Способ 2:
def exe_41(x, y):
    var = 1
    for i in range(abs(y)):
        var *= x
    return 1 / var
print(f'4.2. X(3) в степени Y(-5) = {exe_41(3,-5)}')