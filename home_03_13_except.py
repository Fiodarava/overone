# 11.4 Решить задачу с обработкой исключений.
# Вызвать ошибку ValueError и сообщить, что пользователь ввел не число:
# Задача hometask_4_3:
# Написать калькулятор. Пользователь вводит 2 числа и одно из мат действий. В
# зависимости от действия, вывести результат.
# In: 4
# f
# +
# Out: Вы ввели не число!

# 11.5 Вызвать ошибку TypeError в предыдущем задании.

# number_1 = input("Введите число: ")
# number_2 = input("Введите число: ")
# done = input("Укажите действие: ")
# #
# try:
#     if done == "+":
#         print(float(number_1) + float(number_2))
#     elif done == "-":
#         print(float(number_1) - float(number_2))
#     elif done == "*":
#         print(float(number_1) * float(number_2))
#     elif done == "/" and float(number_2) != 0:
#         print(number_1 / float(number_2))
#     elif done == "/" and float(number_2) == 0:
#         print("can't divide by zero")
#
# except ValueError:
#     print("Вы ввели не число!")
# except TypeError:
#     print("Математические операции не поддерживаются между строкой и числом!")

# 11.6 Решить задачу с обработкой исключений.
# Вызвать ошибку KeyError и вернуть программу к исполнению команд. Укажите
# пользователю какое вино он может выбрать.
# Немного изменим задачу 8.9:
# Катя с Анной пьют вино. Программа
# принимает сколько бутылок вина выпьет
# каждая. Еще программа принимает какое вино пьет Катя, а Анна всегда пьет белое.
# In: 2
# 5
# pink wine
# Out: Есть только ['red wine', 'white wine'], выберите из них

# while True:
#     kate_wine = int(input("Kate: "))
#     kate_sortwine = input("Sort: ")
#     ann_wine = int(input("Ann: "))
#     wine = {'red wine': 42, 'white wine': 37}
#     try:
#         print(kate_wine * wine[kate_sortwine] + ann_wine * wine['white wine'])
#         break
#     except KeyError:
#         print("Есть только ['red wine', 'white wine'], выберите из них")


# Самостоятельно придуманные задачи:

# 7.2 Анна регистрируется на сайте. Ей надо ввести имя,  фамилию, возраст и почту. Создать кортеж из этих данных.
# Она ввела только «Anna» и  почту.
# Необходимо запросить недостающие данные.
# - не смогла решить через исключения)))
# while True:
#     name = input("Имя: ")
#     lastname = input("Фамилия: ")
#     adress = input("Эл. почта: ")
#     age = input("Возраст: ")
#     if name == '' or lastname == '' or adress == '' or age == '':
#         print("Repeat")
#     else:
#         tpl = (name, lastname, adress, age)
#         print(tpl)
#         break

# В задаче 5/15 вызвать ошибку TypeError
# Вход: число N и кол-во строк,равное N. Программа делает список из полученных строк.
# try:
#     print(lst  = [input("Введите строку: ") for i in range(int(input("Укажите число строк: ")))])
# except TypeError:
#     print("Это нельзя распечатать(")

# 5.4 Вход: 2 числа a и b Программа выводит все числа от a до b
# включительно. Числа могут быть любыми и подаваться в любом порядке.
# В задаче 5.4 вызвать ошибку NameError.
# a = int(input())
# b = int(input())
# try:
#     if a < b:
#         s = set([i for i in range(i, b+1)])
#     elif a == b:
#         s = set([a])
#     else:
#         s = set([i for i in range(b, a + 1)])
#     print(s)
# except NameError:
#     print("Название переменной не существует")