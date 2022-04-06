 # Hometask_13_1 Из полученного списка чисел создайте список с суммами
# этих чисел, отсортированными по возрастанию
# In: 965 582 023 8 695210
# Out: [5, 8, 15, 20, 23]
#
def count_num(number):
    """
    Подсчёт суммы цифр натурального числа математическим методом.
    : param number: натуральное число | int
    : return: натуральное число сумма цифр числа number | int
    """

    b = number % 10
    c = 0
    while b > 0:
        c += b
        number = number // 10
        b = number % 10
    return c

numbers_lst = [int(i) for i in input("Input numbers: ").split()]
sum_number_lst = []
for i in numbers_lst:
     sum_number_lst.append(count_num(i))
sum_number_lst.sort()
print(sum_number_lst)

# Hometask_13_2
# Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:
# f(x) = 1 - (x+2)**2, при x<= -2
# f(x) = - x/2 , при 2 <x< 2
# f(x) = (x+2)**2 + 1 , при x> 2

def func_val_1(x):
    """
    Подсчёт значения функции f(x) = 1 - (x+2)**2
    : param number:  число | float
    : return:  result = f(x) | float
    """
    result = 1 - (x+2)**2
    return result

def func_val_2(x):
    """
    Подсчёт значения функции f(x) = - x/2
    : param number:  число | float
    : return:  result = f(x) | float
    """
    result = - x/2
    return result


def func_val_3(x):
    """
    Подсчёт значения функции f(x) = (x+2)**2 + 1
    : param number:  число | float
    : return:  result = f(x) | float
    """
    result = (x+2)**2 + 1
    return result


x = float(input("Input X: "))
if x <= - 2:
    print(func_val_1(x))
elif x > - 2 and x < 2:
    print(func_val_2(x))
else:
    print(func_val_3(x))

# Hometask_13_3  Напишите функцию которая принимает на вход список целых чисел, удаляет из него
# все нечётные значения, а чётные нацело делит на два.
# In: 852 85 784 58
# Out: [852, 784, 58

def dev_even(lst_numbers):
    """

    удаляет из списка все нечётные значения, а чётные нацело делит на два
    : param lst_input список целых чисел | list
    : return:  result = список делённых на 2 чётных чисел | list
    """

    i = 0
    while i < len(lst_numbers):
        if int(lst_numbers[i]) % 2 > 0:
            del lst_numbers[i]
            i = i
        else:
            lst_numbers[i] = int(lst_numbers[i]) / 2
            i += 1
    return lst_numbers
a = input("Input numbers: ").split()
print(dev_even(a))