# 8.2 Создайте словарь из строки 'pythonist’ следующим образом:
# Ключи – символы строки, Значения – количество вхождений символа в строку
# РЕШАЛИ НА ЗАНЯТИИ
# str = "pythonist"
# dic = {a: str.count(a) for a in str}
# print(dic)


# 8.3 На вход программе поступает целое число N.
# Необходимо создать словарь, который будет включать в себя ключи от 1 до N,
# а значениями будут значение ключа в квадрате.
# n = int(input())
# dic = {a : a**2 for a in range(1, n+1)}
# print(dic)

# 8.4 Дан словарь: dic = {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}
# Выведите на экран произведение всех значений словаря.
# dic = {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}
# result = 1
# for v in dic.values():
#     result *= v

# 8.5 Пол, Анна и Алекс писали контрольную.
# Пол и Анна получили 4, а умничка Алекс 5.
# Напишите программу, которая по имени показывает оценку.
# На вход программа получает имя.
# a = input("Имя: ")
# dic = {"Пол": 4, "Анна": 4, "Алекс": 5}
# print(dic[a])

# H_T8.1 Создайте словарь person, в котором будут ключи name, age, city. Выведите значение возраста.
# person = {"name": input("Имя: "), "age": input("Возраст: "), "city": input("Город: ")}
# print(person["age"])

# H_T8.2 Программа принимает список из трех слов. Создать словарь, в котором ключ — слово,
# значение — количество символов в слове

# lst = [input("Слово1: "), input("Слово2: "), input("Слово3: ")]
# print(lst)
# dic = {a: len(a) for a in lst}
# print(dic)

# H_T8.3 На вход подается список чисел. Создать словарь, в котором ключ — число,
# значение — число на 10% больше. Значение должно быть округленное
# lst = [float(i) for i in input("Число: ").split()]
# print(lst)
# dic = {a: round(a * 1.1, 2) for a in lst}
# print(dic)

# H_T8.4. Создайте следующий словарь: ключи – BMW, Tesla; значения – список из 3х моделей.
# Выведите 1ое и последнее значения каждого из ключей.
# dic = {"BMW": ['a', 'b', 'c'], "Tesla":['x', 'y', 'z']}
# print(dic["BMW"][0], dic["BMW"][2])
# print(dic["Tesla"][0], dic["Tesla"][2])

# 8.9 Катя с Анной собрались поболтать о своем о женском. Какие посиделки без вина?
# Катя пьет красное, а Анна белое. \
# Программа принимает на вход 2 числа:
# сколько бутылок выпила каждая. Выведи сколько денег они потратили.
# wine = {'red wine': 42, 'white wine': 37}
# kate_wine = int(input("Kate: "))
# an_wine = int(input("Ann: "))
# # result = kate_wine * wine['red wine'] + an_wine * wine['white wine']
# print(kate_wine * wine['red wine'] + an_wine * wine['white wine'])

# HT_8_6 Создать словарь, который в качестве ключа будет использовать страну,
# а в качестве значения - ее столицу.
# Внеси в него следующие страны:
# Россия (Москва), Украина ('Киев'), Италия (Рим), Испания (Мадрид), Болгария (София).
# Программа должна запрашивать у пользователя, столицу какой страны он хочет узнать и выдавать результат.
# dic = {}
# dic = dict(Россия = 'Москва', Украина = 'Киев', Италия = 'Рим', Испания = 'Мадрид', Болгария = 'София')
# a = input("Столицу какой страны Вы хотите узнать? ")
# print(dic[a])

# HT_8_7 Создать словарь, ключи — числа, значения — слова.
# Удалить из него все пары с нечетными ключами. Вывести на печать
# В этом вам может помочь статья, что сбрасывала ранее.

# lst_1 = [int(i) for i in input().split()]
# lst_2 = input().split()
# print(lst_1, lst_2)
# dic = dict(zip(lst_1, lst_2))
# print(dic)
# for k in list(dic.keys()):
#     if k % 2 != 0:
#         del dic[k]
# print(dic)


# 10/1
# import random
# #
# lst = [random.randint(1,10) for i in range(10)]
# print(lst)
# with open("file.txt", "w") as f:
#     f.write(str(len(lst)) + "\n")
#     for i in lst:
#         f.write(str(i) + " ")

# 10.2 Прочитать из файла числа, сформировать список и напечатать его
# Out: [10, 91, 76, 48, 11, 89, 65, 56, 81, 94, 36]
# lst = []
# with open("file.txt") as f:
#     lst = [int(i) for i in f.read().split()]
# print(lst)

# 10.3
# days = { 1:'Sun', 2:'Mon', 3:'Tue',4:'Wed', 5:'Thu', 6:'Fri', 7:'Sat'}
# with open("file.txt", "w") as f:
#         for k, v in days.items():
#                 s = str(k) + ":" + v
#                 f.write(s + "\n")

# 10.4 Прочитать предыдущий файл, сформировать из него словарь, распечатать его.
# Out: {'1': 'Sun', '2': 'Mon', '3':'Tue', '4': 'Wed', '5': 'Thu', '6':'Fri', '7': 'Sat'}
# days = {}
# with open('file.txt') as f:
#     for line in f.readlines():
#         days[line[0]] = line[2:5]
#     print(days)
#
# 10.5 Создать множество отрицательных и положительных чисел.
# Записать его в файл построчно.
#
# import random
#
#
# s_1 = set([random.randint(-50, 50) for i in range(5)])
# print(s_1)
# with open("file.txt", "w") as f:
#     for i in s_1:
#         f.write(str(i) + "\n")

# 10.6 Прочитать предыдущий файл, сформировать из него множество, распечатать его.
# Out: {1, 2, 4, 5, 6, 7, 8}
# with open("file.txt") as f:
#     set = set([int(i) for i in f.read().split()])
# print(set)

# 10.7 Пользователь вводит слова. Записать их в файл: каждое слово на отдельной строке
# c = int(input("Количество слов: ")) # что-то не получается через while
# with open('file.txt', 'w') as f:
#        for i in range(c):
#            f.write(input() + "\n")

# word = input("введите слово ").split()
# with open("file2.txt", "w") as file:
#     for i in word:
#         file.write(i + "\n")
# word = input("введите слово ").split()

# while True:
#     word = input("введите слово ")
#     with open("file2.txt", "a") as file:
#         file.write(word + "\n")


# 10.8 Дан список [5, True, ‘abc’].  Записать его в файл
# lst = [5, True, "abc"]
# with open("file.txt", "w") as f:
#     for i in lst:
#            f.write(str(i) + "\n")
#
# 10.9 Создать список чисел. Записать каждое нечетное число в файл
# lst = [int(i) for i in input().split()]
# print(lst)
# with open("file.txt", "w") as f:
#     for i in lst:
#         if i % 2 > 0:
#             f.write(str(i) + "\n")