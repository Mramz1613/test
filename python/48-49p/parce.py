# class Student:
#     def __init__(self,name:str,age:int,course:int,facultet:str,university:str):
#         # self.name - атрибут класса
#         #name - параметр метода __init__
#         self.name = name
#         self.age = age
#         self.course = course
#         self.facultet = facultet
#         self.university = university
#         print("Вызван метод __init__() класса Student")
#
#     #-> None - ничего не возвращает, не содержит return
#     def setName(self)-> None:
#         self.name = input("Введите имя")
#     def setAge(self)-> None:
#         self.age = int(input("Введите возраст"))
#     def setCourse(self)-> None:
#         self.course = int(input("Введите курс"))
#     def setFacultet(self)-> None:
#         self.facultet = input("Введите факультет")
#     def setUniversity(self)-> None:
#         self.university = input("Введите университет")
#
#     def getName(self)-> str:
#         return self.name
#     def getAge(self)-> int:
#         return self.age
#     def getCourse(self)-> int:
#         return self.course
#     def getFacultet(self)-> str:
#         return self.facultet
#     def getUniversity(self)-> str:
#         return self.university
#
#     def display(self):
#         return print(f"Имя: {self.name}, Возраст: {self.age}, Курс: {self.course}, "
#                      f"Факультет: {self.facultet}, Университет: {self.university}")
#
# objStud = Student("Антон",20,3,"Психология", "БФУ")
# objStud.setName()
# objStud.setAge()
# objStud.setCourse()
# objStud.setFacultet()
# objStud.setUniversity()
# print(objStud.getName())
# print(objStud.getAge())
# print(objStud.getCourse())
# print(objStud.getFacultet())
# print(objStud.getUniversity())

class City:
    def __init__(self,city:str, region:str, country:str, population:int, index:int, cod_of_telephone:str):
        self.city = city
        self.region = region
        self.country = country
        self.population = population
        self.index = index
        self.cod_of_telephone = cod_of_telephone

    def setCity(self)-> None:
            self.city = input("Введите имя")
    def setRegion(self)-> None:
            self.region = int(input("Введите возраст"))
    def setCountry(self)-> None:
            self.country = int(input("Введите курс"))
    def setPopulation(self)-> None:
            self.population = input("Введите факультет")
    def setIndex(self)-> None:
            self.index = input("Введите университет")
    def setCod(self)-> None:
        self.cod_of_telephone = input("Введите номер(начиная с '+')")
        while self.cod_of_telephone[0] != "+":
            self.cod_of_telephone = input("Введите номер(начиная с '+')")

    def getCity(self) -> str:
        return self.city
    def getRegion(self) -> str:
        return self.region
    def getCountry(self) -> str:
        return self.country
    def getPopulation(self) -> int:
        return self.population
    def getIndex(self) -> int:
        return self.index
    def getCod(self) -> str:
        return self.cod_of_telephone

    def display(self):
        print(self.city,self.region,self.country,self.population,self.index,self.cod_of_telephone)


objCity = City("Kld", "KldObl", "Russia", 1000000, 236, "+79527962657" )
objCity.setCod()
len()