# import time
# '''
# Абстрактный класс
# '''
# from abc import *
# class Animal(ABC):#класс Animal является дочерним, т.к у него
#                   #указан родитель(класс ABC, который находится в
#                   #в библиотеки abc)
#     name = ""
#     age = 0
#     weight =0
#     isAlive = True #живое ли животное
#     def __init__(self,name:str, age:str, weight:float,
#                  isAlive:bool):
#         #атрибуту класса присвоили значение параметра
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.isAlive = isAlive
#     @abstractmethod
#     def eat(self,food:str):
#         pass
#     @abstractmethod
#     def move(self,speed:float, distance:float):
#         pass
#     @abstractmethod
#     def sound(self):
#         pass
#
# class Mammals(Animal,ABC):#Множественное наследование
#     def __init__(self, isFeedMilk: bool, name: str, age: str, weight: float, isAlive: bool):
#         super().__init__(name, age, weight, isAlive)
#         self.isFeedMilk = True
#     @abstractmethod
#     def procreate(self): #Появление потовство
#         pass
#
# class NotMammals(Animal,ABC):
#     def __init__(self, name: str, age: str, weight: float, isAlive: bool,isFeedMilk:bool):
#         super().__init__(name, age, weight, isAlive)
#         self.isFeedMilk = False
#     @abstractmethod
#     def create_eggs(self):
#         pass
#
# class Tiger(Mammals):
#     def __init__(self, isFeedMilk: bool, name: str, age: str, weight: float, isAlive: bool,isPredator:bool):
#         super().__init__(isFeedMilk, name, age, weight, isAlive)
#         self.isPredator = True
#     def move(self,speed:float, distance:float):
#         print(f"Тигр пошел куда то со скоростью {speed} на расстояние {distance}")
#
#     def eat(self,food:str):
#         print(f"Тигр поел {food}")
#         self.weight +=1
#
#     def sound(self):
#         print("Гррррр")
#
#     def procreate(self)->"Tiger":
#         return Tiger(True,input("введите имя тигра"),input("Введите возраст"),float(input("Введите вес")),True,True)
#
#     def display(self):
#         print(f"{self.name=},{self.isFeedMilk=},{self.age=},{self.weight=},{self.isPredator=}")
#
# class Bird(NotMammals,ABC):
#     def __init__(self, name: str, age: str, weight: float, isAlive: bool, isFeedMilk: bool,feathers:bool,canFly:bool):
#         super().__init__(name, age, weight, isAlive, isFeedMilk)
#         self.feathers = feathers
#         self.canFly = canFly
#
#     @abstractmethod
#     def fly(self,speed:float,distance:float):
#         pass
#
#     @abstractmethod
#     def procreate(self): #Появление потовство
#         pass
#
# class Gull(Bird):
#     def __init__(self, name: str, age: str, weight: float, isAlive: bool, isFeedMilk: bool, feathers: bool,
#                  canFly: bool):
#         super().__init__(name, age, weight, isAlive, isFeedMilk, feathers, canFly)
#
#     def procreate(self):
#         return Gull(input("Введите имя птенца"),input("Введите возраст"),float(input("Введите вес")),bool(input("Он живой?")),False,bool(input("Он в оперении?")),bool(input("Он может летать?")))
#
#     def create_eggs(self):
#         print("Чайка отложила яйцо")
#         time.sleep(5.0)
#         print("Появился птенец")
#         return Gull.procreate(self)
#
#     def fly(self,speed:float,distance:float):
#         if self.feathers == True:
#             print(f"Чайка полетела на скорости {speed} на расстояние {distance}")
#         else:
#             print("Похоже чайка еще не умеет летать")
#
#     def eat(self,food:str):
#         self.weight += 0.1
#         print(f"чайка съела {food} теперь её вес {self.weight}")
#
#     def display(self):
#         print(f"{self.name=},{self.weight=},{self.age=},{self.canFly=},{self.feathers=},{self.isFeedMilk=}")
#
#     def move(self,speed:float, distance:float):
#         pass
#
#     def sound(self):
#         print("ГРГРРГР")
#
#
#
# # Tigr = Tiger(True,"Anton","13",180.5,True,True)
# # Tigr.move(2.5,77.7)
# # NewTirg = Tigr.procreate()
# # NewTirg.display()
# # Tigr.display()
# # Tigr.sound()
# gull = Gull("Петя","11",11.1,False,False,False,False)
# new_gull = gull.create_eggs()
# new_gull.display()
# gull.display()
# new_gull.fly(1,1)
# gull.fly(1,1)