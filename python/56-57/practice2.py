"""Задание 1
Создать базовый класс «Животное» и производные
классы «Тигр», «Крокодил», «Кенгуру». С помощью
конструктора установить имя каждого животного и его характеристики.
Создайте для каждого класса необходимые
методы и поля


Задание 2
Создайте класс для конвертирования температуры из
Цельсия в Фаренгейт и наоборот. У класса должно быть
два статических метода: для перевода из Цельсия в Фаренгейт и
для перевода из Фаренгейта в Цельсий. Также
класс должен считать количество подсчетов температуры и
возвращать это значение с помощью статического метода

"""
import random as r

class Animal:
    def __init__(self,animal_cell:bool,eats:str, location:str):
        self.animal_cell = animal_cell
        self.eats = eats
        self.location = location

    def display(self):
        print(f"{self.animal_cell=}, {self.eats=}, {self.location}")


class Tiger(Animal):

    hung = 100
    energy = 100
    days = 200
    childs = 0

    def __init__(self, animal_cell: bool, eats: str, location: str, subspecies:str,mammal:bool):
        super().__init__(animal_cell, eats, location)
        self.subspecies = subspecies
        self.mammal = mammal

    def display_tiger(self):
        print(f"{self.animal_cell=},{self.eats=},{self.location=},{self.subspecies=},{self.mammal=}")

    @staticmethod
    def hunt()->None:
        Tiger.energy -= 5
        chance = r.randint(0,1)
        if chance == 1:
            Tiger.hung += 20
            print("Тигр нашел добычу")
            Tiger.days += 1
        else:
            print("Сегодня голодный")
            Tiger.days += 1

    @staticmethod
    def sleep():
        Tiger.energy += 20
        Tiger.days += 1
        print("Тигр поспал")

    @staticmethod
    def spawn():
        if Tiger.energy >= 150 and Tiger.hung >= 150:
            Tiger.childs += 1
            Tiger.days += 3
            print("Тигр дал потомство")
        else:
            print("Не хватает ресурсов")
            Tiger.days += 1

    @staticmethod
    def stats():
        print(f"{Tiger.days= }, {Tiger.hung= },{Tiger.energy= },{Tiger.childs= }")

    def walk(self):
        self.location = input("Куда пошел тигр?")
        print(f"Тигр теперь в {self.location}")


class Crocodile(Animal):
    def __init__(self, animal_cell: bool, eats: str, location: str,reptilia:bool,eggs:int ):
        super().__init__(animal_cell, eats, location)
        self.reptilia = reptilia
        self.eggs = eggs

    def display_croco(self):
        print(f"{self.animal_cell=},{self.eats=},{self.location=},{self.reptilia=},{self.eggs=}")

    @staticmethod
    def swim():
        print("Крокодил ")

class Kangaroo(Animal):
    def __init__(self, animal_cell: bool, eats: str, location: str,mammal:bool,endemic:bool):
        super().__init__(animal_cell, eats, location)
        self.mammal = mammal
        self.emdemic = endemic

    def display_tiger(self):
        print(f"{self.animal_cell=},{self.eats=},{self.location=},{self.mammal=},{self.emdemic=}")




tigr = Tiger(True,"Хищник","Россия","Амурский",True)
tigr.stats()
tigr.spawn()
for i in range(5):
    tigr.hunt()

for i in range(5):
    tigr.sleep()

tigr.spawn()
tigr.stats()
tigr.walk()
tigr.display_tiger()












# #static method
#
# class Human:
#     def __init__(self,name):
#         self.name = name
#
# class Student(Human):
#     def __init__(self, humanObj, course):
#         super().__init__(humanObj.name)
#         self.couse = course
#
#     def disp(self):
#         print(f"{self.name},{self.couse}")
#
# humanobj = Human("Vasya")
# studobj = Student(humanobj,4)
# studobj.disp()
# print(issubclass(Student,Human))
#
#
#
#
#
#
# class StudentPython41:
#     name_of_group = "Python41"
#     def __init__(self,name:str,age:int,class_room:str):
#         self.name = name
#         self.age = age
#         self.class_room = class_room
#
#     def display(self):
#         print(f"Студент: {self.name} , Возраст: {self.age} , Аудитория: {self.class_room}")
#
#     @staticmethod
#     def dispGR():
#         print(f"Название группы {StudentPython41.name_of_group}")
#
#     @staticmethod
#     def changeGR():
#         StudentPython41.name_of_group = input("Введите новое название группы")
# StudentPython41.dispGR()
# StudentPython41.changeGR()
# StudentPython41.dispGR()
#
# obj1 = StudentPython41("Вася",19,"411")
# obj1.display()