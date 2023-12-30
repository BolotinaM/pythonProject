# # # print(123)
# # # print('hello')
# #
# # # first = 11
# # # second = 5
# # # result = 11 * 5
# # # print(result)
# #
# # # a = 4
# # # b = 7
# # # if a > b:
# # #     print(1)
# # # else:
# # #     print(0)
# #
# # # a = 7
# # # P = 7*4
# # # S = 7**7
# #
# #
# #
# # #
# # # print(P)
# # # print(S)
# #
# # # a = 2
# # # result = 2 ** 10
# # # print(result)
# #
# # # a = 101
# # # result = 101 % 10
# # # print(result)
# #
# # # a = 111
# # # student = 19
# # # result = a // student
# # # print(result)
# #
# # # a = 8
# # # b = 18
# # # G = (a * b) ** 0.5
# # # print(G)
# #
# # # a = 5
# # # b = 12
# # # c = (a ** 2) + (b ** 2)
# # # G = c ** 0.5
# # # print(G)
# #
# # # lesson 2
# #
# # # a = int(input())
# # # print(a)
# # # P = a * 4
# # # # S = a * a
# # # S = a ** 2
# # # print(P)
# # # print(S)
# # #
# # # var = int(input())
# # # P = var * 4
# # # S = var*var
# # # print(S, P)
# # # # ЗАДАЧА 1 про обои в замурованной комнате без дверей и окон
# # #
# # # a = float (input("Введите длину комнаты: "))
# # # b = float (input("Введите ширину комнаты: "))
# # # c = float (input("Введите высоту комнаты: "))
# # # d = float (input("Введите длину рулона: "))
# # # e = float (input("Введите ширину рулона: "))
# # #
# # # z = (2 * (a + b)) / e
# # # x = z / (d / c) # искомое число рулонов
# # # y = (x // 1) + 1
# # #
# # # print("Вам понадобится ", y, " рулонов")
# # #
# # # cost = float (input("Введите стоимость одного рулона "))
# # # summ = y * cost
# # #
# # # print("Стоимость Вашего заказа ", summ, "рублей")
# #
# # #
# # # print('Маша\tКатя\tСаша\nMary\tKate\tAlex\nПривет/Hi!')
# #
# # # # Задача с водительским удостоверением
# # #
# # # car = input("Есть ли у Вас действующее водительское удостоверение? ")
# # # if car == "да":
# # #     print("Заполните форму регистрации ")
# #
# # # # Задача про расплату
# # #
# # # card = input("Вы будете оплачивать заказ картой? ")
# # # if card == "да":
# # #     print("Извините, мы не принимаем карты ")
# # # elif card == "нет":
# # #     nal = input("Вы будете оплачивать заказ наличными? ")
# # #     if nal == "да":
# # #         print("Вот Ваш заказ ")
# # #     else:
# # #         print("Вам придется снять наличные средства")
# #
# # # # Задача про День рождения
# # #
# # # date = str(input("Введите день и месяц Вашего рождения в формате XX.YY "))
# # # HB = "С днём рождения! \nСпасибо за предоставление информации!" \
# # # if date == "29.10" else "Cпасибо за предоставление информации!"
# # # print(HB)
# #
# # # # Задание по методам
# # # my_darling_list = []
# # # my_darling_list.append(1000)
# # # my_darling_list.append(200)
# # # my_darling_list.insert(0, 300)
# # # my_darling_list.sort()
# # # print(my_darling_list)
# #
# # # # Задание со словарем
# # #
# # # my_first_dict = {'1':'one', '2':'two', '3':'three'}
# # # print(my_first_dict['2'])
# #
# #
# # # # Задание на преобразование элементов массива
# # #
# # # mass = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # # i = 0
# # # length = len(mass)
# # # while i < length:
# # #     a = mass[i] ** 2
# # #     print(a)
# # #     i += 1
# #
# # # # Задача про языки программирования
# # #
# # # Lan = ["Python", "C++", "C#", "Fortran", "JavaSript"]
# # # i = 0
# # # for lan in Lan:
# # #     lan = Lan[i]
# # #     i = i + 1
# # #     print(lan)
# # # print(Lan)
# #
# # # # задание по изменению списков
# #
# # # random_names = ["Peter", "Ivan", "Mark", "Alex", "Maksim", "Jacob", "Abdula", "John", "Sinji"]
# # # m_names = []
# # # for name in random_names:
# # #     if name[0] == "J":
# # #         m_names.append(name)
# # # print(m_names)
# # #
# # # for i,name in enumerate(random_names):
# # #     if name[0] == "M":
# # #         random_names.pop(i)
# # # print(random_names)
# #
# # # # Напишите код с использованием for и range,
# # # # который будет выводить сумму квадратов чисел от 1 до 10.
# # #
# # # summ = 0
# # # for number in range(10):
# # #     summ += number ** 2
# # # print(summ)
# #
# # # # Задание на написание функции
# # # def email(email_client):
# # #     print('На Ваш электронный адрес,', email_client, 'будет направлено письмо')
# # # e = input('Здравствуйте! Введите Ваш email: ')
# # # email(e)
# #
# # # # Задача с атибутами c модернизацией
# # # class Actors:
# # #     def __init__(self, name, age, description):
# # #         self.name = name
# # #         self.age = age
# # #         self.description = description
# # # Felton = Actors("Felton", 33, "I do not know how old he is")
# # # Depp = Actors("Depp", 55, "Honestly, I do not know how old he is too")
# # # print(Felton.name)
# # # print(Depp.name)
# #
# # # # Практическая работа по  классам
# # #
# # # class Bilds
# # # class Personal
# # # class Person
# # # class WorksTasks
# # # class WorkingAreas
# #
# # # class Bird:
# # #     def fly(self): # тот самый self
# # #         print("летит")
# # # karasu = Bird()
# # # Bird.fly(karasu)
# #
# # # class User:
# # #     def __init__(self, name, money):
# # #         self.name = name
# # #         self.money = money
# # #     def __str__(self):
# # #         return self.name
# # #     def __int__(self):
# # #         return self.money
# # # user = User("Марк", 420)
# # # print(user)
# # # print(int(user))
# #
# # # class UserShop:
# # #     def __init__(self, firstname, lastname, email, adress):
# # #         self.firstname = firstname
# # #         self.lastname = lastname
# # #         self.email = email
# # #         self.adress = adress
# # #     def __str__(self):
# # #         return self.firstname
# # #     def __str__(self):
# # #         return self.lastname
# # #     def __str__(self):
# # #         return self.email
# # #     def __str__(self):
# # #         return self.adress
# # #
# # #     def change_email(new_email):
# # #         if '@' in new_email:
# # #             self.email = new_email
# # #             return True
# # #         return False
# # # user = UserShop("Марк", "Джон", 'xxx@yyy.ru', 'Communalnaia str. 87')
# # # print(user)
# # # print(str(user))
# #
# # # a = int(float(44.44))
# # # b = float(int(55.55))
# # # c = a + b
# # # print(c)
# # #
# # # a = int(float(input()))
# # # b = int(float(input()))
# # # print(a, b)
# # #
# #
# # # a = []
# # # for i in range (3):
# # #     a.append(input())
# # #
# # # print(a[0], a[2])
# #
# # # nums = [1]
# # # step = 2
# # # N = 5
# # # for i in range(N-1):
# # #     nums.append(nums[i] + step)
# # # print(nums)
# #
# # # n = 3
# # # step = 2
# # # a = [1]
# # # for i in range(n - 1):
# # #     a.append(a[i] + step)
# # # print(a)
# #
# # # a = [1, 2, 3, 4]
# # # count = 0
# # # for i in a:
# # #     count += i
# # # avg = count/len(a)
# # # print(avg)
# #
# # # a = float(input())
# # # b = int(a)
# # # print(b)
# #
# # # a = "Привет"
# # # b = 100
# # # c = a * b
# # # print(c)
# #
# # # a = float(input())
# # # b = a * 10
# # # c = int(b % 10)
# # # print(b)
# # # print(c)
# # #
# # # a = 'Иванов'
# # # # c = a[0]
# # # # c = a[:1]
# # # b = "."
# # # d = c + b
# # # print(d)
# #
# # # a = int(input())
# # #
# # # b = int(a % 10)
# # #
# # # print(b)
# #
# # # number = 10
# # # number = 10 * 5
# # # print(number * 5)
# # #
# # #
# # # number2 = 7
# # # print(number + number2)
# #
# # # class Human:
# # #     Min_age = 0
# # #     Max_age = 100
# # #
# # #     @classmethod
# # #     def validate (cls, age):
# # #         return cls.Min_age <= age <= cls.Max_age
# # #
# # #     def __init__(self, age, name, country):
# # #         self.age = 0
# # #         self.name = 'error'
# # #         self.country = 'error'
# # #         if self.validate(age):
# # #             self.age = age
# # #             self.name = "Алексей"
# # #             self.country = "Россия"
# # #
# # #     @staticmethod
# # #     def norm (hieght, weight):
# # #         return (hieght - weight)
# # # print(Human.norm(170, 72))
# # #
# # # h=Human(33, "Alex", "Russia")
# # # print(Human.validate(33))
# # # print(h.__dict__)
# #
# # # a = 100
# # # b = 3
# # # if not not not a:
# # #     b = b + 1
# # # print(b)
# #
# # # a = int(input())
# # # b = a % 2 = 0
# # # if (:
# # #     print(a)
# #
# # # class Animal:
# # #     def __init__(self, animal_type):
# # #         self.animal_type = animal_type
# # #
# # #     def print_type(self):
# # #         print(f"Это {self.animal_type}!")
# # #
# # #
# # # animal = Animal(input('Что за зверь: '))
# # # animal.print_type()
# #
# # # class Animal:
# # #     def __init__(self, name):
# # #         self.name = name
# # #
# # #     def get_name(self):
# # #         print(f'Его зовут {self.name}!')
# # #
# # #
# # # class Cat(Animal):
# # #     def __init__(self, name):
# # #         Animal.__init__(self, name)
# # #         self.get_name()
# # #
# # # # Это создание объекта, его не удаляй
# # # Cat(input('Как его зовут?:'))
# #
# # # class Animal:
# # #     def __init__(self, animal_type):
# # #         self.animal_type = animal_type
# # #
# # #     def print_type(self):
# # #         print(f"Это {self.animal_type}!")
# # #
# # #
# # # animal = Animal(input('Что за зверь: '))
# # # animal.print_type()
# #
# # # a = int (input())
# # # if a > 0:
# # # 	print(a + 3)
# # # else:
# # #     if a < 0:
# # # 	    print(a - 2)
# # #     else:
# # #         print(a + 1)
# #
# # # a = int(input())
# # #
# # # b = int(input())
# # #
# # # c = int(input())
# # #
# # # d = int(input())
# # #
# # # e = 10
# # #
# # #
# # #
# # # if a < e:
# # #
# # # 	if b< e:
# # #
# # # 		if c < e:
# # #
# # # 			if d < e:
# # # 				print(1)
# # # else:
# # # 	print(0)
# #
# # # a = 'дaход'
# # #
# # # if a [0] == a[-1]:
# # # 	if a [1] == a[-2]:
# # # 		print(1)
# # # #
# # # # else:
# # # 	print(0)
# #
# # # a = 1.234
# # # b = a * 100
# # # print (b)
# # # c  = int(b %  10)
# # # print(c)
# # # a = "int - это целочисленный тип данных"
# # # b = a.count(" ")
# # # print(b)
# #
# # # a = str(input("Введите фамилию "))
# # # b = str(input("Введите имя "))
# # # c = str(input("Введите отчество "))
# # # d = str(".")
# # # e = a [0]
# # # f = b [0]
# # # g = c [0]
# # # h = e + d + f + d + g
# # # print(h)
# #
# # # a = int(input())
# # # b = a ** 0.5
# # # if a % b == 0:
# # # 	b = int(b + 1) ** 2
# # # else:
# # # 	print(-1)
# # # print(b)
# #
# # # a = 10
# # # b = 10.0
# # # if a == b:
# # #     print(1)
# # # elif int(a) == int(b):
# # #     print(2)
# # # else:
# # #     print(0)
# #
# # # a = int(input())
# # # b = int(input())
# # # c = int(input())
# # count = 0
# # if a == b or a == c:
# # 	count = count + 2
# # elif b ==c:
# #  	count = count + 2
# # else:
# # 	print(0)
# #
# # print(count)
# #
# # # a = int(input())
# # # b = int(input())
# # # c = int(input())
# # # max = 0
# # #
# # # if a > min:
# # #     max = a
# # # if b > max:
# # #     max = b
# # # if c > max:
# # #     max = c
# # # print(max)
# #
# # # class Fruit:
# # #     def __init__(self, name):
# # #         self.name = name
# # #         self.sell_f = 80
# # #     def get_name(self):
# # #         print(f'Купи {self.name}!')
# # #     def get_sell(self):
# # #         print(f'Яблоко стоит {self.sell_f}!')
# # #
# # #     def sell(self, sell_f):
# # #         Fruit.__init__(self, sell_f)
# # #         self.get_sell()
# # # class apple(Fruit):
# # #     def __init__(self, name):
# # #         Fruit.__init__(self, name)
# # #         self.get_name()
# # #
# # #
# # #
# # # apple(input())
# # # Fruit.get_sell()
# # # #
# # # # class Animal:
# # # #     def __init__(self, animal_type):
# # # #         self.animal_type = animal_type
# # # #
# # # #     def print_type(self):
# # # #         print(f"Это {self.animal_type}!")
# # # #
# # # #
# # # # animal = Animal(input('Что за зверь: '))
# # # # animal.print_type()
# #
# # # class Fruits:
# # #
# # #     def __init__(self):
# # #         fruit = {'apple': 56, 'orange': 93, 'banana': 76}
# # #         print("Список покупок (фрукты) : " + str(fruit))
# # #
# # #         res = []
# # #         for key in fruit.keys():  # надо было указать ключ
# # #             res.append(fruit[key])
# # #         sell = res[0] + res[1] + res[2]
# # #         print("Итого, мне нужно взять с собой: " + str(sell) + " рублей")
# # #
# # # f = Fruits()
# # # print(f)
# # # #
# # # alfavit =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# # # # Создаем алфавит
# # #
# # # alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# # # alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# # # smeshenie = int(input('Шаг шифровки: '))
# # # message = input("Сообщение для шифровки: ").upper()
# # # itog = ''
# # # lang = input('Выберите язык RU/EU: ')   #Добавляем возможность выбора языка
# # #
# # # if lang == 'RU':
# # #     for i in message:
# # #         mesto = alfavit_RU.find(i)   # Алгоритм для шифрования сообщения на русском
# # #         new_mesto = mesto + smeshenie
# # #         if i in alfavit_RU:
# # #             itog += alfavit_RU[new_mesto]
# # #         else:
# # #             itog += i
# # # else:
# # #     for i in message:
# # #         mesto = alfavit_EU.find(i)		# Алгоритм для шифрования сообщения на английском
# # #         new_mesto = mesto + smeshenie
# # #         if i in alfavit_EU:
# # #             itog += alfavit_EU[new_mesto]
# # #         else:
# # #             itog += i
# # #
# # # print(itog)
# #
# # # class Fruits:
# # #
# # #  def __init__(self):
# # #   fruit = {'apple': 56, 'orange': 93, 'banana': 76}
# # #   print("Список покупок (фрукты) : " + str(fruit))
# # #   res = []
# # #   for key in fruit.keys(): # надо было указать ключ
# # #    res.append(fruit[key])
# # #    sell = res[0] + res[1] + res[2]
# # #    print("Итого, мне нужно взять с собой: " + str(sell) + " рублей")
# #
# # # class Fruits:
# # #
# # #     def __init__(self):
# # #         fruit = {'apple': 56, 'orange': 93, 'banana': 76}
# # #         print("Список покупок (фрукты) : " + str(fruit))
# # #
# # #         r = []
# # #         for key in fruit.keys(): # надо было указать ключ
# # #             r.append(fruit[key])
# # #         sell2 = r[0] + r[1] + r[2]
# # # print("Итого, мне нужно взять с собой: " + str(sell2) + " рублей")
# # #
# # # class Drinks:
# # #
# # #  def __init__(self):
# # #
# # #     drinks = {'cola': 65, 'fanta': 60, 'sprite': 70}
# # #     print("Список покупок (напитки) : " + str(drinks))
# # #
# # #     resurs = []
# # #     for key in drinks.keys(): # надо было указать ключ
# # #         resurs.append(drinks[key])
# # #
# # #     sell1 = resurs[0] + resurs[1] + resurs[2]
# # #     print("Итого, мне нужно взять с собой: " + str(sell1) + " рублей")
# # #
# # # d = Drinks()
# # # print(d)
# # # f = Fruits()
# # # print(f)
# #
# # class Animal():
# #     def __init__(self, name):
# #         self.name = name
# #     def b_d(self):
# #         print(f'{self.name} что-то сломал')
# # class dog(Animal):
# #     def __init__(self, name):
# #         super().__init__(name)
# #     def _make_sueta(self):
# #         print(f'{self.name} играет с диваном')
# #
# # class cat(Animal):
# #     def __init__(self, name):
# #         super().__init__(name)
# #     def _make_sueta(self):
# #         print(f'{self.name} тыгыдыкает в 5 утра по лицу')
# #
# # Dog = dog('барбос')
# # Cat = cat('елкалаз')
# #
# # # Animal.b_d()
# # Dog.b_d()
# # Cat.b_d()
# # Dog._make_sueta()
# # Cat._make_sueta()
#
# # a = float(35.97)
# #
# # b = int( a*10)
# #
# # c = b%10
# #
# # print(c)
# #
# # a = float(1.234)
# #
# # b = int (a*10)
# #
# # c = b%10
# #
# # d = int( a*100)
# #
# # e = d%10
# #
# # print(c+e)
#
# # name ="Артемий меня зовут Артемий"
# # print(name)
# #
# # print("мне семь лет ")
# #
# # print(2+3)
# #
# # print(900000+2000000000000000)
#
# # print(99000000000000000000000000-19000000000000000000000000000000000)
#
# class Fruits:
#
#     def __init__(self):
#         fruit = {'apple': 56, 'orange': 93, 'banana': 76}
#         print("Список покупок (фрукты) : " + str(fruit))
#
#         r = []
#         for key in fruit.keys():
#             r.append(fruit[key])
#             s = r[0] + r[1] + r[2]
#
#         print("Итого, мне нужно взять с собой: " + str(s) + " рублей")

# class Drinks:
#     def __init__(self):
#         drinks = {'cola': 65, 'fanta': 60, 'sprite': 70}
#         print("Список покупок (напитки) : " + str(drinks))
#
#         resurs = []
#         for key in drinks.keys(): # надо было указать ключ
#             resurs.append(drinks[key])
#
#         sell1 = resurs[0] + resurs[1] + resurs[2]
#         print("Итого, мне нужно взять с собой: " + str(sell1) + " рублей")
#
# d = Drinks()
# print(d)
# f = Fruits()
# print(f)

# class Shop():
#     def items (self, name, amount, rarety):
#         self.name = name
#         self.amount = amount
#         self.rarety = rarety
#         print(f'у нас есть {self.name}  количестве {self.amount} шт , и он {self.rarety} редкий!')
#
#     def help (self, answer):
#         answer  = input("Вы хотели бы приобрести что-то еще?")
#         self.answer = answer
#         if answer == "да":
#             televisor = Shop()
#             televisor.items('телик', "2", 'очень')
#         else:
#             print("Ждём Вас снова!")
#
# televisor = Shop()
# televisor.items('телик', "2", 'очень')
# televisor.help('да')

# # a = input()
# # b = a[0]
# # c = a[1]
# # d = a[2]
# # b = int(b)
# # c = int(c)
# # d = int(d)
# # count = 0
# #
# # if b % 2 == 0:
# #     count = count + 1
# # if c % 2 == 0:
# #     count = count + 1
# # if d % 2 == 0:
# #     count = count + 1
# # print(count)
#
# # a = int(input())
# # b = int(input())
# # c = int(input())
# # d = int(input())
# #
# # if a == b:
# #     if b == c:
# #         if c == d:
# #             print("все числа равны")
# #         else:
# #             print(d)
# #     else:
# #         print(c)
# # else:
# #     if b == c:
# #         print(a)
# #     else:
# #         print(b)
#
# # x = int(input())
# # y = int(input())
# # a = int(input())
# # b = int(input())
# # if 0 < x < 9 and 0 < y <9:
# # 	if a == x + 1:
# # 		if b == y + 1:
# # 			print(1)
# # 		else:
# # 			print(0)
# # 	else:
# # 		print(0)
# # else:
# # 	print('не работает')
#
#
#
#
#
#
#
#
#
#
#
#
# print(7)
# print ("Cава ")
# print ("пицца")
#
# print ( "Маша, 25 лет, мороженое "  )
#
# print ("Барселона")

# year_1 = int(input("Введите Ваш год рожденияd" ))
# month_1 = int (input("Введите Ваш месяц рождения"))
# day_1 = int (input("Введите Ваш день рождения"))
# year_2 = int(input("Введите год рождения Вашего друга"))
# month_2 = int (input("Введите месяц рождения Вашего друга"))
# day_2 = int (input("Введите день рождения Вашего друга"))
#
#
# if year_1 < year_2:
# 	print(1)
# elif month_1 < month_2:
#     print(1)
# elif day_1 < day_2:
# 	print(1)
# elif day_1 == day_2:
# 	print("Вы родились в один день!")
# else:
# 	print(2)

# a = int(input())
# a = a ** 0.5
# if a % 2 == 0:
# 	a = (a + 1) ** 2
# 	print(a)
# else:
# 	print(-1)

# year = int(input())
#
# if year % 4 == 0 and not year % 100 == 0:
#     print(1)
# elif year % 400 == 0:
#     print(1)
# else:
#     print(0)

# a = str("10")
# b = str ("15")
# c = str((a + b)*2)
# print(c)

# a = 1
# b = 1
# x = int(input())
# y = int(input())
#
# if (x > 0 and x == a + 2) or (x > 0 and x == a + 1):
#     if (y > 0 and y == b + 2) or (y > 0 and y == b + 1):
#         print(1)
#     else:
#         print(0)
# else:
#     print(0)

# class Shop():
#
#     def __init__(self):
#         items_list = {'телик': 1000, 'арбуз': 50, 'книга Гарри Поттер': 100}
#         # print('Список товаров: ' + str(items_list))
#         items_titles = {1:'телик', 2: 'арбуз', 3: 'книга Гарри Поттер'}
#
#         items_names = []
#         for key in items_titles.keys():
#             items_names.append(items_titles[key])
#             TV_name = str(items_names[0])
#             watermellon_name = str(items_names[1])
#             book_Harry_Potter_name = str(items_names[2])
#
#         items_cost = []
#         for key in items_list.keys():
#             items_cost.append(items_list[key])
#             TV_cost = str(items_cost[0])
#             watermellon_cost = str(items_cost[1])
#             book_Harry_Potter_cost = str(items_cost[2])
#
#             print('Товар ' + TV_name + ' стоит ' + TV_cost)
#             print('Товар ' + watermellon_name + ' стоит ' + watermellon_cost)
#             print('Товар ' + book_Harry_Potter_name + ' стоит ' + book_Harry_Potter_cost)
#
# # def items(self, name, amount, rarety):
# # self.amount=amount
# # self.rarety=rarety
# # print(f'у нас есть {self.name 'в количестве {self.amount}шт , и он {self.rarety} редкий.')
#
#     def selling(self, cost):
#         self.cost = cost
#         find_cost = input('Чью цену вы хотите узнать?\n')
#         if find_cost == 'телик':
#             print(f'Он стоит {self.cost} рублей')
#         else:
#             print(f'У нас нет товара {find_cost}.')
#
#     def buy(self):
#         buying = input('Вы хотите его купить?\n')
#         if buying == 'да' and self.amount > 0:
#             print('поздравляем вас с покупкой')
#             self.amount -= 1
#         elif self.amount == 0 and buying == 'да':
#             print('Извините, но этого товара пока нет.')
#         elif buying == 'нет':
#             someting_else = input('вы хотите приобрести другой товар?\n')
#             if someting_else == 'да':
#                 televisor.selling('1000')
#
# televisor = Shop()
# televisor.items('телик', 2, 'очень')
# televisor.selling('1000')
# televisor.buy()
#
# class Televosor():
#     def types(self, firma, model, version, color, cost_TV):
#         self.firma = firma
#         self.model = model
#         self.version = version
#         self.color = color
#         self.cost_TV = cost_TV
#
# apple = Televosor()
# apple.types('samsung', 'алиса', 2023, 'black', 1000)

# alfavit =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# # Создаем алфавит
#
# alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# smeshenie = int(input('Шаг шифровки: '))
# message = input("Сообщение для шифровки: ").upper()
# itog = ''
# lang = input('Выберите язык RU/EU: ')   #Добавляем возможность выбора языка
#
# if lang == 'RU':
#     for i in message:
#         mesto = alfavit_RU.find(i)   # Алгоритм для шифрования сообщения на русском
#         new_mesto = mesto + smeshenie
#         if i in alfavit_RU:
#             itog += alfavit_RU[new_mesto]
#         else:
#             itog += i
# else:
#     for i in message:
#         mesto = alfavit_EU.find(i)		# Алгоритм для шифрования сообщения на английском
#         new_mesto = mesto + smeshenie
#         if i in alfavit_EU:
#             itog += alfavit_EU[new_mesto]
#         else:
#             itog += i
#
# c = 'Воробьёв Андрей Олегович'
#
# c1 = c[0]
#
# c2 = c[9:10]
#
# c3 = c[16:17]
#
# print(c1+"."+c2+"."c3)

# year1 = 2005
#
# year2 = 2009
#
# month1 = 11
#
# month2 = 12
#
# day1 = 25
#
# day2 = 19
#
# if year1 < year2:
#
# 	print(1)
#
# elif month1 < month2:
#
# 	print(1)
#
# elif day1 < day2:
#
#     print(1)

a = 0
b = 1
for i in range(101):
    a = a + b
    b = b + 1
    print(a)

# result = 0
# for i in range(101):
#     if i % 2 == 0:
#         result += i
# print(result)

a = 0
b = 0
for i in range(100):
    a = a + b
    for i in range(100):
        b = b + 1
a = int(a)
print(a // 2)# ответ: 2550