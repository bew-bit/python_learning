#1. Создать программно файл в текстовом формате, записать
#в него построчно данные, вводимые пользователем. Об окончании
#ввода данных свидетельствует пустая строка.
file = open(r'C:\sveta_file.txt', 'w', encoding='utf-8')
while True:
    row = input('Введите строку или просто Enter для окончания:')
    if row == '': break
    file.write(row + '\n')
file.close()
#2. Создать текстовый файл (не программно), сохранить в нем
#несколько строк, выполнить подсчет количества строк, количества
#слов в каждой строке.
print('\n2.')
with open('C:\sveta_file.txt', encoding='utf-8') as f:
    rows = f.readlines()
    counter = 0
with open('C:\sveta_file.txt', 'w', encoding='utf-8') as f:
    for i, value in enumerate(rows):
        words_number = len(value.split())
        counter +=1
        #f.write(f'Длина {i + 1}-й строки: {words_number} слов(а).\n') - перезапись в файл
        print(f'Длина {i + 1}-й строки: {words_number} слов(а).')
    print('Всего строк: ', counter)
f.close()
#3. Создать текстовый файл (не программно), построчно записать
#фамилии сотрудников и величину их окладов. Определить, кто
#из сотрудников имеет оклад менее 20 тыс., вывести фамилии
#этих сотрудников. Выполнить подсчет средней величины дохода
#сотрудников.
import numpy as np
with open('text_3.txt', 'r', encoding='utf-8') as f:
    s_sum = []
    less = []
    line = f.read().split('\n')
    for i in line:
        i = i.split()
        if float(i[1]) < 20000:
            less.append(i[0])
        s_sum.append(int(i[1])) #убрать int() для обработки закомментированного print()
#print(f'Зарплата меньше 20000 {less}. Средняя зарплата: {sum(map(float, s_sum))/len(s_sum)}')
print(f'\n3.\nЗарплата меньше 20000 у {less}. Средняя зарплата: {np.mean(s_sum)}')
f.close()
#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и
#считывающую построчно данные. При этом английские числительные
#должны заменяться на русские. Новый блок строк должен записываться
#в новый текстовый файл.
rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_text = []
with open('text_4.txt', 'r') as f:
    for i in f:
        i = i.split(' ', 1)
        new_text.append(rus[i[0]] + '  ' + i[1])
    print(f'\n4.\nТекст{new_text}\nзаписан в {f.name}\n')
with open('text_4_new.txt', 'w') as f_new:
    f_new.writelines(new_text)
f.close()
f_new.close()
#import requests
#import json
#token = 'trnsl.1.1.20200416T132512Z.0bdb58c00f70557b.b1aec4ed1dc72e76cc6c08980f7ed0c2de92ae86'
#url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
#with open('task_4_text_yandex.txt', 'w', encoding='utf-8') as f_result:
#    with open('text_4.txt', encoding='utf-8') as f_4:
#        for line in f_4:
#            eng_text = line
#            trans_option = {'key': token, 'lang': 'en-ru', 'text': eng_text}
#            webRequest = requests.get(url_trans, params=trans_option)
#            trabs_dict = json.loads(webRequest.text)
#            line_to_result = "".json(trans_dict["text"])
#            f_result.write(line_to_result)
#        print(f'Текст из {f_4.name} переведен и записан в {f_result.name}')

#5. Создать (программно) текстовый файл, записать в него
#программно набор чисел, разделенных пробелами. Программа
#должна подсчитывать сумму чисел в файле и выводить ее на экран.
with open('text_5.txt','w', encoding='utf-8') as f:
    f.write('22 33 11')
with open ('text_5.txt','r', encoding='utf-8') as f:
    nums = f.read()
    nums = list(map(int, nums.split()))
    sum = 0
    for i in nums:
        sum += i
print(f'5.\nСумма чисел в {f.name}:\n{sum}\n')
f.close()
#from random import randint
#sum_el = 0
#with open('text_5.txt', 'w', encoding='utf-8') as f:
#    for i in range(100):
#        el = randint(1, 100)
#        sum_el += el
#        f.write(str(el) + ' ')
#print(f'5.\nСумма элементов: {sum_el}\n')

#6. Необходимо создать (не программно) текстовый файл, где
#каждая строка описывает учебный предмет и наличие лекционных,
#практических и лабораторных занятий по этому предмету и
#их количество. Важно, чтобы для каждого предмета не обязательно
#были все типы занятий. Сформировать словарь, содержащий
#название предмета и общее количество занятий по нему.
#Вывести словарь на экран.
t_table = dict()
with open('text_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        subject, remains = line.split(': ')
        for i in remains.split():
            if i != '-':
                t_table[subject] = t_table.get(subject, 0) + int(i.split('(')[0])
print(f'6.\nОбщее количество часов по предмету:\n{t_table}\n')
f.close()
#7. Создать (не программно) текстовый файл, в котором каждая строка должна
#содержать данные о фирме: название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
#а также среднюю прибыль. Если фирма получила убытки, в расчет средней
#прибыли ее не включать. Далее реализовать список. Он должен содержать
#словарь с фирмами и их прибылями, а также словарь со средней прибылью.
#Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл. Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджеры контекста.
import json
result = []
profit = {}
plus = 0
i = 0
with open('text_7.txt', 'r') as f:
    for line in f:
        name, legal, revenue, expense = line.split()
        profit[name] = int(revenue) - int(expense)
        if profit.setdefault(name) >= 0:
            plus = plus + profit.setdefault(name)
            i += 1
    if i != 0:
        av_prof = plus / i
        print(f'7.\nСредняя прибыль: {av_prof:.2f}')
    else:
        print(f'Прибыли нет')
    result.append(profit)
    result.append({'average_profit': round(av_prof)})
    print(f'Прибыль по компаниям: {result}')
with open('text_7.json', 'w') as js:
    json.dump(result, js)
    js_str = json.dumps(result)
    print(f'Файл {js.name}\n{js_str}')

