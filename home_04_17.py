# Hometask_14_4
# Добавить классу Dog приватный атрибут - master.
# Создать метод get_master() который возвращает значение атрибута master.


# class Dog:
#     def __init__(self, height, weight, name, age, master):
#         self.height = height
#         self.weight = weight
#         self.name = name
#         self.age = age
#         self.__master = master
#
#     def change_name(self, new_name):
#         self.name = new_name
#         return self.name
#
#     def jump(self):
#         if self.height > 100:
#             return f"Dog {self.name} can jump over your fence"
#         else:
#             return f"Dog {self.name} can`t jump over your fence"
#
#
#     def run(self):
#         if self.weight < 5 and self.weight > 2:
#             return f"Dog {self.name} very likes to run"
#         else:
#             return f"Dog {self.name} don`t likes to run"
#
#     def bark(self):
#         if self.age > 10:
#             return f"Dog {self.name} don`t bark, only bite"
#         else:
#             return f"Dog {self.name} barks very loud"
#
#     def get_master(self):
#         return self.__master
#
# sharik = Dog(100, 50, "Sharik", 5, "Vet")
# print(sharik.get_master())
#
# Hometask_14_5
# Создать три класса: Dog, Cat, Parrot.
# Атрибуты каждого класса: name, age, master.
# Каждый класс содержит конструктор и методы: run, jump, birthday(увеличивает age на 1), sleep.
# Класс Parrot имеет дополнительный метод fly, Cat - meow, Dog - bark.

# class Dog:
#
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self):
#         return f"The dog can run"
#
#     def jump(self):
#         return f"The dog can jump"
#
#     def birthday(self):
#         return f"{self.name} is {self.age+1} years."
#
#     def sleep(self, hours):
#         return f"Sleep {hours}!! hours every day."
#
#     def bark(self):
#         return f"Gav-gav!!!"
#
#
# class Cat:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self):
#         return f"The cat can run"
#
#     def jump(self):
#         return f"The catcan jump"
#
#     def birthday(self):
#         return f"{self.name} is {self.age+1} years."
#
#     def sleep(self, hours):
#         return f"Sleep {hours}!! hours every day."
#
#     def meow(self):
#         return f"Meow-meow!!!"
#
# class Parrot:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self):
#         return f"The parrot can run"
#
#     def jump(self):
#         return f"The parrot can jump"
#
#     def birthday(self):
#         return f"{self.name} is {self.age+1} years."
#
#     def sleep(self, hours):
#         return f"Sleep {hours}!! hours every day."
#
#     def fly(self):
#         return f"I can fly"
#

# Hometask_14_6 Создать родительский класс Pet, содержащий все общие методы классов Dog, Cat, Parrot.
# Унаследовать Dog, Cat, Parrot от класса Pet.
# Удалить в дочерних классах те методы, которые имеются у родительского класса.
# Создать объект каждого класса и вызвать все его методы.


# class Pet:
#
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self):
#         return f"The {self.name} can run!"
#
#     def jump(self):
#         return f"The {self.name} can jump"
#
#     def birthday(self):
#         return f"{self.name} is {self.age+1} years."
#
#     def sleep(self, hours):
#         return f"Sleep {hours}!! hours every day."
#
# class Dog(Pet):
#
#     def __init__(self, name, age, master):
#         super().__init__(name, age, master)
#
#     def bark(self):
#         return f"Gav-gav!!!"
#
#
# class Cat(Pet):
#     def __init__(self, name, age, master):
#         super().__init__(name, age, master)
#
#     def meow(self):
#         return f"Meow-meow!!!"
#
#
# class Parrot(Pet):
#     def __init__(self, name, age, master):
#         super().__init__(name, age, master)
#
#     def fly(self):
#         return f"I can fly"
#
# pet = Pet("turtle Gogi", 15, "ok")
# print(pet.run())
# print(pet.jump())
# print(pet.birthday())
# print(pet.sleep(15))
#
# dog = Dog("Sharik", 5,"ok")
# print(dog.run())
# print(dog.jump())
# print(dog.birthday())
# print(dog.sleep(10))
# print(dog.bark())
#
# cat = Cat("Kotya", 2, "ok")
# print(cat.run())
# print(cat.jump())
# print(cat.birthday())
# print(cat.sleep(7))
# print(cat.meow())
#
# parrot = Parrot("Grisha", 3, "ok")
# print(parrot.run())
# print(parrot.jump())
# print(parrot.birthday())
# print(parrot.sleep(5))
# print(parrot.fly())
#
# print(Cat.mro())


# Hometask_14_7
# Сделайте класс Petа абстракным, добавьте метод voice. Подумайте какой метод вам сделать
# абстрактным, т.е. что вам удобно будет переопределять.
# Проверьте, чтобы подклассы Dog, Cat, Parrot работали, т.е. вы могли создавать обеъкты.


# from abc import ABC, abstractmethod
#
# class Pet(ABC):
#
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self):
#         return f"The {self.name} can run!"
#
#     def jump(self):
#         return f"The {self.name} can jump"
#
#     def birthday(self):
#         return f"{self.name} is {self.age+1} years."
#
#     def sleep(self, hours):
#         return f"Sleep {hours}!! hours every day."
#
#     @abstractmethod
#     def voice(self):
#         pass
#
# class Dog(Pet):
#
#     def __init__(self, name, age, master):
#         super().__init__(name, age, master)
#
#     def voice(self):
#         return f"Gav-gav!!!"
#
#
# class Cat(Pet):
#
#
#     def __init__(self, name, age, master):
#         super().__init__(name, age, master)
#
#     def voice(self):
#         return f"Meow-meow!!!"
#
#
# class Parrot(Pet):
#     def __init__(self, name, age, master):
#         super().__init__(name, age, master)
#
#     def voice(self):
#         return f"I can speak like you))"
#
#     def fly(self):
#         return f"I can fly"
#
#
# dog = Dog("Sharik", 5,"ok")
# print(dog.run())
# print(dog.jump())
# print(dog.birthday())
# print(dog.sleep(10))
# print(dog.voice())
#
# cat = Cat("Kotya", 2, "ok")
# print(cat.run())
# print(cat.jump())
# print(cat.birthday())
# print(cat.sleep(7))
# print(cat.voice())
#
# parrot = Parrot("Grisha", 3, "ok")
# print(parrot.run())
# print(parrot.jump())
# print(parrot.birthday())
# print(parrot.sleep(5))
# print(parrot.voice())
# print(parrot.fly())


# Hometask_14_8
# Добавьте в класс Pet дескриптор, чтобы нельзя было задать отрицательный возраст или 0.

class NonNegativeZero:


    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value == 0 or value < 0:
            raise ValueError("Value cannot be negative or zero!!")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


from abc import ABC, abstractmethod

class Pet(ABC):

    age = NonNegativeZero()


    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return f"The {self.name} can run!"

    def jump(self):
        return f"The {self.name} can jump"

    def birthday(self):
        return f"{self.name} is {self.age+1} years."

    def sleep(self, hours):
        return f"Sleep {hours}!! hours every day."

    @abstractmethod
    def voice(self):
        pass

class Dog(Pet):


    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def voice(self):
            return f"Gav-gav!!!"

class Cat(Pet):


    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def voice(self):
        return f"Meow-meow!!!"


class Parrot(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def voice(self):
        return f"I can speak like you))"

    def fly(self):
        return f"I can fly"


dog = Dog("Sharik", 5,"ok")
print(dog.run())
print(dog.jump())
print(dog.birthday())
print(dog.sleep(10))
print(dog.voice())

cat = Cat("Kotya", 2, "ok")
print(cat.run())
print(cat.jump())
print(cat.birthday())
print(cat.sleep(7))
print(cat.voice())

parrot = Parrot("Gosha", -3, "ok")
print(parrot.run())
print(parrot.jump())
print(parrot.birthday())
print(parrot.sleep(5))
print(parrot.voice())
print(parrot.fly())

# Hometask_14_9
# Добавьте в класс Pet валидацию, чтобы у питомца было имя и хозяин.
# Вообще заклинило, не получается. Подскажи что-нибудь, а.
