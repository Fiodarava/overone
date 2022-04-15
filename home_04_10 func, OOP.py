# Hometask_13_4
# Напишите функцию, которая создает список случайных элементов. На фход функция
# принимает кол-во элементов, минимальное и максимальноезначение
# In: rand_nums(7, 2, 12)
# Out: [12, 6, 9, 2, 11, 5, 8]


from random import randint

def rand_nums(num_elems, min_elem, max_elem):
    """

        создаёт список случайных элементов, принимая на вход кол-во элементов, минимальное и максимальноезначение
        : param num_elems, min_elem, max_elem | int
        : return:  список рандомных чисел | list
        """
    return [randint(min_elem, max_elem) for i in range(num_elems)]

print(rand_nums(5, 1, 20))


# Hometask_13_5
# Преобразуйте задачу с покупкой торта из экзамена 2 в функцию.

choice = input("Какой торт Вы хотели бы приобрести: ")
question = input("Что Вы хотели бы уточнить (цена, количество, описание, купить): ")
if question == "купить":
    weight = int(input("Сколько грамм торта Вам положить: "))

def def_confectionery(choice, question):


    confectionery = {"наполеон": ["крем заварной, слоёное тесто - средне-сладкий", 5.0, 800],
                     "медовик": ["крем сметанный, тесто песочное -  очень сладкий", 4.5, 1200],
                     "киевский": ["ореховый слой, тесто песочное -  самый вкусный торт", 15.0, 1500]}


    if question == "описание":
        return print("Торт ", choice, "состоит из ", confectionery[choice][0])
    elif question == "цена":
        return print("Торт", choice, "стоит",  confectionery[choice][1], "рублей")
    elif question == "количество":
        return print("Торт", choice, "осталось ", confectionery[choice][-1], "грамм")
    elif question == "купить":

        return print("К оплате ", (weight * confectionery[choice][1] * 0.01), " рублей")
        return print("Торта ", choice, " осталось ", confectionery[choice][-1], "грамм" )

# def_confectionery("наполеон", "описание")
def_confectionery(choice, question)


# Hometask_13_6
# Напишите функцию, вычисляющую значение факториала числа N. Используйте рекурсию
# In: 5
# Out: 120

def fuct(n):
    """

        вычисляет значение факториала числа N
        : param n | int
        : return:  значение факториала | int
        """
    if n == 1:
        return 1
    return fuct(n-1)*n
print(fuct(5))


# Hometask_14_1
# Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
# Класс имеет три метода: jump, run, bark.
# Каждый метод выводит сообщение на экран.
# Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.

class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        if self.height > 100:
            return f"Dog {self.name} can jump over your fence"
        else:
            return f"Dog {self.name} can`t jump over your fence"


    def run(self):
        if self.weight < 5 and self.weight > 2:
            return f"Dog {self.name} very likes to run"
        else:
            return f"Dog {self.name} don`t likes to run"

    def bark(self):
        if self.age > 10:
            return f"Dog {self.name} don`t bark, only bite"
        else:
            return f"Dog {self.name} barks very loud"

sharik = Dog(115, 54, "Sharik", 5)
print(sharik.__dict__)
print(sharik.jump())
print(sharik.run())
print(sharik.bark())

# Hometask_14_2
# Добавить в класс Dog метод change_name.
# Метод принимает на вход новое имя и меняет атрибут имени у объекта. Создать один объект класса.
# Вывести имя. Вызвать метод change_name. Вывести имя.

class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age


    def change_name(self, new_name):
        self.name = new_name
        return self.name

    def jump(self):
        if self.height > 100:
            return f"Dog {self.name} can jump over your fence"
        else:
            return f"Dog {self.name} can`t jump over your fence"


    def run(self):
        if self.weight < 5 and self.weight > 2:
            return f"Dog {self.name} very likes to run"
        else:
            return f"Dog {self.name} don`t likes to run"

    def bark(self):
        if self.age > 10:
            return f"Dog {self.name} don`t bark, only bite"
        else:
            return f"Dog {self.name} barks very loud"

sharik = Dog(115, 54, "Sharik", 5)
print(sharik.name)
sharik.change_name("Tusik")
print(sharik.name)

