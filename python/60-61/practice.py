# class Passport:
#     def __init__(self,firstName:str, lastName:str, surname:str,
#                  dateOfIssue:int, gender:str,code:int,series:int,
#                  number:int):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.__surname = surname #закрытый атрибут(не наследуется)
#         self.dateOfIssue = dateOfIssue
#         self.gender = gender
#         self.__code = code
#         self.__series = series
#         self.number = number
#
# #класс заграничный паспорт
# class ForeingPassport(Passport): #ForeingPassport - ребенок(дочерний класс)
#                                  #Passport -  родитель(родительский класс)
#     def __init__(self, firstname: str, lastname: str,
#                  dateofissue: int,gender: str, number: int, type:str,
#                  visa:list):
#         super().__init__(firstname,lastname," ",dateofissue,gender,0,0,
#                          number)#вызов __init__() из родительского класса
#         self.type = type
#         self.visa = visa

from abc import *

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius:float):
        self.radius = radius

    def set_radius(self):
        self.radius = float(input("Введите радиус"))

    def area(self,pi=3.14):
        return (self.radius**2)*pi

class Rectangle(Shape):
    def __init__(self,w,h):
        self.w = w
        self.h = h
    def area(self):
        return self.w*self.h

cir = Circle(3.0)
cir.set_radius()
print(cir.area())
rec = Rectangle(2,2)
print(rec.area())
import os
import shutil
from os import path

