# name = input ('ввелите имя : ')
# age = int (input("ввелите свой возраст : " ))
# print('этот далбаеб', name, "дожил до", age)
#
# ego_imya = 'Robeet Polson'
          
# print (ego_imya[0], ego_imya[7])
# print (ego_imya[1])
# # if 13>4:
#     print('nifiga sebe')
# elif 33>5:
#     print('age 2')
# else:
#     print('fig tebe')
# person = int(input('сколько тебе лет?'))
# if person < 18:
#     print('еще недо рос')
# elif person >= 18 and person < 40:
#     print('идем гулять')
# elif person >= 40 and person < 70:
#     print('старый уже')
# elif person >= 70 and person <= 140:
#     print('не туда ноги привели')
# else:
#     print('ошибка')
# number = int(input('введите любое число :'))
# if number % 2 == 0:
#     print('четное')
# elif number % 2 != 0:
#     print('нечетное')
# a = [12, 'sdas', 123.2, True, 'edzen', 12]
# a[0] = '11'
# a[1] = 'duck'
# a[4] = 'python'
# print(a)
# a. append(False)
# b = [12 ,200 ,321 ,444]
# a.extend(b)
# a.insert(1,'Alex')
# a[-1] = '555'
# print(a)
# my_list = ['один ,два ,три ,четыре ,пять']
# for elem in my_list:
#     print(elem)
  
# contact_name = ['aziret', 'azamat', 'almaz', 'tariel', 'zaman']

# name = input("введите имя для поиска : ").title()

# name = name.capitalize()

# for i in contact_name : 
    # if i == name:
    #  print("контакт найден")
    #  break
    # elif i != name:
    #  print("нет такого контакта")

# if name in contact_name:
#        print(f"контакт {name} найден")
# elif name not in contact_name:
#        print("нет такого контакта")
# else:
#        print("error")

# todo=['закончить пятый класс', 'почистить зубы', 'принять душ']

# while True: 

#     destvie = input('выберите действие:/n1 - это добавление/n2 - это удаление/n3 - это просмотр/n: ')
#     if destvie =='3':
#         for i in todo:
#             print(i)
#     elif destvie == '1':
#         delo = input ("добавляй дело: ")
#         todo.append(delo)
#         print(f"успешно добавлено: {delo}")
#     elif destvie == '2':
#         del_delo = input("удалить дело: ")

# contact_name = {
#     'наима' : 996996996,
#     'абдулкадыр' : 996996997,
#     'дегион' : 996996998,
#     }
# destvie = input('выберите действие:/n1 - добавить номер/n2 - удалить номер/n3 - поиск номера/n4 - просмотр контактов/n: ' )
# if destvie == '1'


# num = 3384456779
# num_str = str(num)
# max_num = 0
# for i in num_str:
#     if int(i) > max_num:
#         max_num = int(i)
# print(max_num)


# name = input('ваше имя: ')
# print(f'hello my friend , {name} /n'*5)
 
# name = input('как вас зовут: ')
# age = input('сколько вам лет: ')
# job = input('где вы работаете: ')
# it = input('какая сфера IT вас интересует: ')
# language = input('на каком языке вы програмируете: ')
# print('')\




# newstr = input('введите строку: ')
# print(newstr* len(newstr))

# def ispalindrom(txt):
#     if  txt[::-1] == txt:
#         print(True)
#     else: 
#         print(False)


# ispalindrom('rex')

# list = ['один', 'два', 'три' , 'четыре' ]
# print(list[0], list[-1])

# number = (1, 2, 3, 4, 5, 6, 7, 8, 9,)

# number = str(123456789)
# print(number[::2])
# print(number[1::2])

# name=input('введите свое имя:')
# surname=input('введите свою фамилию:')
# age=int(input('введите свой возраст:'))
# print("привет", name, surname, "тебе уже", age)

# language = ('python')
# print(language[3])

# r = 'last day on earth'
# print(r[::2])

# num = 12.23
# print '%d' %(num)


# Роберт Полсон, [
# 1. Вам дается текст:

# stribg = """Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colourful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next programme in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colourless.
# But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money."""
# print(stribg.count('s'))
# print(stribg.count('t'))
# - Посчитайте количество букв  `s`  и  `t` .
# - Найдите все слова, которые начинаются с корня  `advert (регистр не должен учитываться) и превратите их все в верхний регистр

#2. Дана строка нечетной длины больше 7 символов, вернуть строку, состоящую из трех средних символов данной строки

# Пример: 


# some_string = "Adverts"

# Output: "ver"

#3. Дается 2 строки "Aidana" и  "Adilet" .  Вам нужно в результате получить смешанную строку из двух имен, буква за буквой.

# a = 'aidana'
# b = 'adilet'
# res = ''
# if len(a) != len(b):
# for i in range 


#  Результат: "AAiddialneat"

#4. Используйте текст с первого задания. Отделите каждое слово в отдельный элемент списка. Уберите точки, запятые, тире и кавычки. Удалите похожие слова (регистр не учитывается) и отсортируйте по алфавиту.

# from dataclasses import replace


# text_new = (
#     stribg.replace(',','') /
#         .replace('-','') /
#         .replace('"','') /
#         .replace('.','') /
#         .replace(''','') / 
# )

#5. aTuple = ("Orange", [10, 20, 30], (5, 15, 2t
#6.  Найдите сумму цифр четырехзначного числа 3456 ( int )

#7 . Напишите программу, которая проверяет текст с первого задания и выводит два слова: наиболее часто встречающееся и самое длинное.




############################################################################################
############################################################################################
############################################################################################
# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ РАУНД 2 №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
############################################################################################
############################################################################################
############################################################################################

# Роберт Полсон, [27/9/22 16:09]


# У вас есть словарь студентов  IT Academy:
# students = [a = []
# for i in range(0,101):
#     a.append(i)
# print(a)
#     {'name': 'John', 'age': 15, 'course': 'python', 'gender': 'Male'},
#     {'name': 'Andrew', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
#     {'name': 'Marcus', 'age': 25, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Agnes', 'age': 40, 'course': 'python', 'gender': 'Female'},
#     {'name': 'Doe', 'age': 42, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Michael', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
#     {'name': 'Jennifer', 'age': 16, 'course': 'java', 'gender': 'Female'},
#     {'name': 'Angela', 'age': 16, 'course': 'python', 'gender': 'Female'},
#     {'name': 'Eniston', 'age': 34, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Albert', 'age': 33, 'course': 'javascript', 'gender': 'Male'},
#     {'name': 'Nash', 'age': 28, 'course': 'python', 'gender': 'Male'},
#     {'name': 'Nicolas', 'age': 19, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Alex', 'age': 21, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Martin', 'age': 22, 'course': 'python', 'gender': 'Male'},
#     {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
#     {'name': 'Mikkel', 'age': 24, 'course': 'python', 'gender': 'Male'},
#     {'name': 'Susann', 'age': 25, 'course': 'javascript', 'gender': 'Female'},
#     {'name': 'Steve', 'age': 26, 'course': 'python', 'gender': 'Male'},
#     {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Johnathan', 'age': 15, 'course': 'python', 'gender': 'Male'},
#     {'name': 'Aidin', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
#     {'name': 'Mirbek', 'age': 25, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Aidana', 'age': 40, 'course': 'python', 'gender': 'Female'},
#     {'name': 'Atay', 'age': 42, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Chyngyz', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
#     {'name': 'Aigerim', 'age': 16, 'course': 'java', 'gender': 'Female'},
#     {'name': 'Jyldyz', 'age': 16, 'course': 'python', 'gender': 'Female'},
#     {'name': 'Emir', 'age': 34, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Emirlan', 'age': 12, 'course': 'javascript', 'gender': 'Male'},
#     {'name': 'Nursultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
#     {'name': 'Aliaskar', 'age': 19, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Aktan', 'age': 21, 'course': 'java', 'gender': 'Male'},
#     {'name': 'Adyl', 'age': 14, 'course': 'python', 'gender': 'Male'},
#     {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
#     {'name': 'Janyl', 'age': 16, 'course': 'python', 'gender': 'Female'},
#     {'name': 'Meerim', 'age': 12, 'course': 'javascript', 'gender': 'Female'},
#     {'name': 'Sultan', 'age': 13, 'course': 'python', 'gender': 'Male'},


#1) высните процентное соотношение мужского пола и женского.

#2) выведите всех студентов с курса python

#3) уберите дубликаты

#4) выведите студентов, которые старше 30 и найдите процент их количества относительно других

#5) отсортируйте студентов по:
        # имени
        # курсу
        # полу
        # возрасту

#6) все студенты курса  javascript  перешли на курс  python.  Как вы поменяете это в словаре ?
# Напишите код

#7) Добавьте по 5 новых студентов на курсы  java  и  python

#8) Отчислите всех студентов младше 15 лет

#9) Написать программу, которая проверяет пароль. До тех пор пока пароль не совпадет,
# программа должна спрашивать пароль. Причем, пароли могут быть равны одному из
# элементов списка `password_list = [‘password’, ‘12 3456’, ‘12345678’, ‘qwerty’, ‘abc123’, ‘monkey’, ‘1234567’]`. Нужно использовать бесконечный цикл, а также операторы break и continue

#10) Распечатать числа от 23 до 87 включительно с шагом итерации 8, используя цикл for и функцию range

# #2) Необходимо удалить пустые строки из списка строк.
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Пользовательские функция 

# def b103():  вызов функции
#     print("hello")

#     return("hello")

#  b103()

#  print(b103())

# def b104 (message): вызов функции 
    # print("привет", message)

# b104("ilim")

# def sum2(a,b):
    # print(a*b)

# sum2(21,8)

# def isPositive(x):
#     if x > 0:
#         return True

# p = []
# for i in range(-15, 15):
#     isPositive(i):
#         p.append(i)

# print(p)



# total = 0

# def calc():
#     global total
#     operation = input("+, - , *, /\nОчистить историю\n")
#     if operation == 'Очистить историю':
#         total = 0
#     elif total != 0:
#         num1 = input("введите число: ")
#         try:
#             float(num1)
#         except ValueError:
#             print('Введите только числа')
#         else:
#             try:
#                 num1 = float(num1)
#                 if operation == '+':
#                     total += num1
#                     print(total)
#                 elif operation == '-':
#                     total -= num1
#                     print(total)
#                 elif operation == '*':
#                     total *= num1
#                     print(total)
#                 elif operation == '/':
#                     total /= num1
#                     print(total)
#                 else:
#                     print("ошибка")
#             except ZeroDivisionError:
#                 print('На нуль делить нельзя!')

#     elif operation in ('+', '-' , '*', '/') and total == 0:
#         num1 = input("введите число: ")
#         num2 = input("введите число: ")
#         try:
#             float(num1)
#             float(num2)
#         except ValueError:
#             print('Введите только числа')
#         else:
#             try:
#                 num1 = float(num1)
#                 num2 = float(num2)
#                 if operation == '+':
#                     total += num1 + num2
#                     print(total)
#                 elif operation == '-':
#                     total += num1 - num2
#                     print(total)
#                 elif operation == '*':
#                     total += num1 * num2
#                 elif operation == '/':
#                     total += num1 / num2
#                 else:
#                     print("ошибка")
#             except ZeroDivisionError:
#                 print('На нуль делить нельзя!')
#         finally:
#             print("___________________________")
#     else:
#         print("тебя же просят ввести символ! совсем!")

# while True:
#     print(calc())




# max = a if a > b else b  # тернарный оператор
# print(max)
 ####
# is_fast = True
# if is_fast:
#     car = "Ferrari"
# else:
#     car = "tico"
# print(car)
# car = 'fer' if is_fast else 'tico'
####
# a, b, c = 13, 66, 32
# max = a if a > b and a >c else b if b > c else c 
# print(max)

# a=[]
# for i in range(1,101):
#     a.append(i)
# print(a)

# a2 = [i**2 for i in range(1,11)]
# print(a2)

# def sum_two 

# my_pets = ['macentosh', 'acer', 'lenovo', 'asus', 'mac', 'samsung']
# my_pets = str(my_pets).upper()
# print(my_pets)

# print(list(map(len, my_pets)))



# circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.50013]
# print(list(map(round, circle_areas, range(1,6))))

# print(list(map(lambda a: a*2, my_pets)))


# Ниже приведен список баллов 10 студентов на экзамене по химии. Давайте отфильтруем тех, кто сдал с баллом выше 75. используя filter.
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# def score(x):
#     if x > 70 :
#         return True
#     return False 
# print(list(filter(score, [66, 90, 68, 59, 76, 60, 88, 74, 81, 65])))

# # Пример №2 / мы ищем в городе заведения с названием мак и мы должны их отфильтровать, чтобы выходило только "мак"
# mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
# mac = "мак"Создайте список из 10 четных чисел и выведите его с помощью цикла for.

# mixed = [x for x in mac if 'мак' in x]
# print(list(filter(mixed, ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак'])))
# # Пример №3 / Следующим примером будет детектор палиндрома. «Палиндром» - это слово, фраза или последовательность, которые читаются одинаково в обе стороны. Давайте отфильтруем слова, являющиеся палиндромами, из набора (iterable) oподозреваемых палиндромов.
# dromes = ("анна", "жанна", "rewire", "madam", "freer", "anutuna", "kiosk")
# print(list(filter(lambda world: world == world[::-1], dromes)))
# # Пример №4 / четные числа
# numbers = [2, 1, 3, 4, 7, 11, 18]

# def new_order():
#     answer = input('будете делать заказ? /n y/n')
#     if answer == 'y':
#         return True
#     elif answer =='n':
#         exit()
        
# def main():
#     ingredients = ['майонез', 'кетчуп', 'ананас', 'сыр', 'колбаса', 'травка', 'зелень']
#     new_order()
    

# list_game = ['Aza', 'Kuma', 'Bama', 'Anna', 'Vika']
# get_game = ['Kuma', 'Anna', 'Adilet', 'Sasha']
# # list = list(set(list_game + get_game))
# # print(list)

# my_str = "frg5gth57ubdfh67 sbf4dsbdrodxbf 2"

# lst, list = [int (i) for i in my_str if i.isdigit()], list(set(list_game + get_game))
# lst  = []
# for i in my_str:
#     if i.isdecimal():
#         lst.append(int(i))
        
# print(lst, list)

# num_1 = int(input('введите число :'))
# num_2 = int(input('введите число :'))
# num_3 = num_1 + num_2
# print(num_3)

# stribg = ("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
# print(stribg.count('i'))
# print(stribg.count('s'))


# lst = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]
# print(lst[::-1])

# number = 12312123432153454534212
# for i in % 2 == 0:
# print('четное')



# num = 3384456779
# num_str = str(num)
# max_num = 0
# for i in num_str:
#     if int(i) > max_num:
#         max_num = int(i)
# print(max_num)

# some_string = 'mercedes'
# print(some_string[3]+some_string[4]+some_string[5])

# sec = int(input('введите секунды :'))
# min = int(input('введите минуты :'))
# hour = int(input('введите часы :'))
# sec_2 = hour * 60 * 60 + min * 60 + sec
# print(sec_2)

# a = []
# for i in range(0,101):
#     a.append(i)
# print(a)


# s =('снег идет')
# s2 = ('идет снег давно')
# s,s2 = ' '.join(input().split(' ')[::-1])
# print(s)



# a= ('снег идет')
# lst = a.split()
# lst[-1], lst[0] = lst[0], lst[-1]
# print(' '.join(lst))

# print('здравствуйте ')
# person = int(input('сколько тебе лет?'))
# if person > 18 and person <=50:
#     person = int(input('сколько тебе лет?'))
# else: 
#     print('стоп')
# elif person >= 18 and person  <27:
#     print('вы годный')
# elif person >= 27:
#     print('истек срок службы')







# year = int(input('введите год :'))
# if year > 0 and year < 2023 :
#     month = int(input('введите месяц :'))
# elif month > 0 and month < 13 :
#     day = int(input('введите день :'))
# elif day > 0 and month < 31: 
    

# for i in range(10):
#     if i %2==1:
#         print(i)




# auto = ['BMW', 'Mercedes', 'Tesla', 'Volvo', 'Audi']
# last_name = len(auto)
# for i in range(last_name):
#     print(str(i + 1) + '.' + '{}'.format(auto[i]))



# my_passwords = ["qwerty", "12345678"]
# user_input = input("введите пороль: ")
# print("Пароль верный" if user_input in my_passwords else "Неправильный пароль")

# 1.1
# lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# l = 0
# for i in lst:
#     if i < 30 and i %3==0:
#         l += i
# print(l)

1.2
# lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# lst_2 = [i for i in lst if i < 30 and i %3==0 else lst_2.append(i) for i ]



# l = 0
# for i in lst:
#     if i < 30 and i %3==0:
#         l += i
# print(l)


