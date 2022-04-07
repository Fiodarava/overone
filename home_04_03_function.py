 # Hometask_13_1 Из полученного списка чисел создайте список с суммами
# этих чисел, отсортированными по возрастанию
# In: 965 582 023 8 695210
# Out: [5, 8, 15, 20, 23]
#
numbers_lst = [int(i) for i in input("Input numbers: ").split()]

def count_num(numbers):
    """
    Из полученного списка чисел создайте список с суммами этих чисел, отсортированными по возрастанию
    : param number: спиcок чисел | list
    : return: отсортированый спиcок сумм цифр каждого числа | list
    """

    sum_number_lst = []
    for i in numbers:
        b = int(i) % 10
        c = 0
        while b > 0:
            c += b
            i = int(i) // 10
            b = int(i) % 10
        sum_number_lst.append(c)
        sum_number_lst.sort()
    return sum_number_lst

print(count_num(numbers_lst))

# Hometask_13_2
# Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:
# f(x) = 1 - (x+2)**2, при x<= -2
# f(x) = - x/2 , при 2 <x< 2
# f(x) = (x+2)**2 + 1 , при x> 2

number = float(input("Input X: "))
def func_val(x):
    """
    функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:
     f(x) = 1 - (x+2)**2, при x<= -2
     f(x) = - x/2 , при 2 <x< 2
     f(x) = (x+2)**2 + 1 , при x> 2
    : param number:  число | float
    : return:  result = f(x) | float
    """
    if x <= - 2:
        result = 1 - (x + 2) ** 2
    elif x > - 2 and x < 2:
        result = - x / 2
    else:
        result = (x + 2) ** 2 + 1
    return result

print(func_val(number))




# Hometask_13_3  Напишите функцию которая принимает на вход список целых чисел, удаляет из него
# все нечётные значения, а чётные нацело делит на два.
# In: 852 85 784 58
# Out: [852, 784, 58
#
# def dev_even(lst_numbers):
#     """
#
#     удаляет из списка все нечётные значения, а чётные нацело делит на два
#     : param lst_input список целых чисел | list
#     : return:  result = список делённых на 2 чётных чисел | list
#     """
#
#     i = 0
#     while i < len(lst_numbers):
#         if int(lst_numbers[i]) % 2 > 0:
#             del lst_numbers[i]
#             i = i
#         else:
#             lst_numbers[i] = int(lst_numbers[i]) / 2
#             i += 1
#     return lst_numbers
# a = input("Input numbers: ").split()
# print(dev_even(a))