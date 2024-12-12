"""
методы класса которые возвращают новый объект
"""
# class Number:
#     def __init__(self,number:int):
#         self.number = number
#         print("Создано число")
#
#     def display(self)->None:
#         print(self.number)
#
#     def summ(self,numObj)->"Number":
#         num = self.number + numObj.number
#         #возвращаем новый объект число
#         return Number(num)
#
#     def sub(self,numObj)->"Number":
#         num = self.number - numObj.number
#         objresSub = Number(num)
#         return objresSub
#
#
#
# numObj = Number(5)
# numObj2 = Number(7)
# numObj3 = numObj.sub(numObj2)
# numObj3.display()
#
# class Human:
#     def __init__(self,name:str,age:int,hight:int,gender:str):
#         self.name = name
#         self.age = age
#         self.__hight = hight
#         self.gender = gender
#
#     def display(self):
#         print(f"{self.name=},{self.age=},{self.__hight=},{self.gender=},", end=" ")
#
# class Student(Human):
#     def __init__(self, name: str, age: int, gender: str,course:int):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.course = course
#
#     def BD(self):
#         self.age += 1
#
#     def display(self):
#         print(f"{self.name=},{self.age=},{self.gender=},{self.course=},", end=" ")
#
#
# objHuman1 = Human("Вася",18,180,"мужской")
# objStudent1 = Student(objHuman1.name,objHuman1.age,objHuman1.gender,4)
# objStudent1.BD()
# objStudent1.display()
class Human:
    def __init__(self,name:str,age:int,experience:int,money:int):
        self.name = name
        self.age = age
        self.experience = experience
        self.money = money

    def display(self):
        print(f"{self.name=},{self.age=},{self.experience=},{self.money=}",end=" ")

class Sailor(Human):
    def __init__(self, name: str, age: int, experience: int, voyages: int, role: str, ship: str, money: int):
        super().__init__(name, age, experience, money)
        self.voyages = voyages
        self.role = role
        self.ship = ship


    def voyadge(self)->None:
        print("Моряк ушел в рейс")
        self.age += 1
        self.experience += 1
        self.money += 10000

    def change_ship(self)->None:
        self.ship = input("Введите название судна")
        print(f"Моряк поменял судно на{self.ship} ")

    def display(self):
        super().display()
        print(f"{self.ship=},{self.role=},")

class Builder(Human):
    def __init__(self, name: str, age: int, experience: int,razrad:int,object:str,money:int):
        super().__init__(name, age, experience,money)
        self.razrad = razrad
        self.object = object

    def build(self):
        self.age += 1
        self.experience += 1
        self.money += 1000
        print("/\\\n__\n|  | Строитель построил дом")

    def change_object(self):
        self.object = input("Введите новый объект")
        print(f"Строитель работает на {self.object}")

    def display(self):
        super().display()
        print(f"{self.razrad=},{self.object=},")

class Pilot(Human):
    def __init__(self, name: str, age: int, experience: int,clas:int,air_plane:str,money:int):
        super().__init__(name, age, experience,money)
        self.clas = clas
        self.air_plane = air_plane

    def fly(self):
        self.age += 1
        self.experience += 1
        self.money += 1500
        print("Пилот улетел")

    def change_plane(self):
        self.air_plane = input("Введите название самолета")
        print(f"Пилот поменял самолет на{self.air_plane}")

    def povichenie(self):
        if self.clas == 2 and self.experience >= 3:
            self.clas = int(input("Введите новый класс"))
        else: print("Мало опыта")

    def display(self):
        super().display()
        print(f"{self.clas=},{self.air_plane=},")

hum1 = Human("Антое",22,3,1000)
hum2 = Human("Вася",26,4,1000)
hum3 = Human("Катя",30,6,1000)
sailor = Sailor(hum1.name,hum1.age,hum1.experience,2,"Матрос","Аничкин",hum1.money)
builder = Builder(hum2.name,hum1.age,hum1.experience,3,"Стадион Калиниград",hum2.money)
pilot = Pilot(hum3.name,hum3.age,hum3.experience,1,"Победа",hum3.money)

sailor.voyadge()
sailor.change_ship()

builder.build()
builder.change_object()

pilot.fly()
pilot.povichenie()