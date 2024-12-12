from datetime import datetime,date  as d ,time
"""
ООП - объектно ориентированое программироапние
Три принцыпа ООП:
1) Инкансуляция
2) Полиморфизм
3) Наследование
Класс содержит общие черты будущих объектов
Синтаксис: class название_класса:
объект - конкретная реализация класса
Родительский класс (супер класс)
Дочерний класс (подкласс)
def __init__(self) - конструктор для создания объекта
Выделение памяти для объекта

"""
class Human:
    def __init__(self,name:str,date_of_bearth: datetime,number:str,country:str,city:str,adress:str):
        self.name = name
        self.date_of_bf = date_of_bearth
        self.number = number
        self.country = country
        self.city = city
        self.address = adress

    def setName(self):
        self.name = input("Введите имя")

    def setDate(self):
        self.date_of_bf = datetime.strptime(input("Введите дату рождения (формат д:м:г)"),"%d:%m:%Y")

    def setNum(self):
        self.number = input("Введите номер телефона")

    def setCountry(self):
        self.country = input("Введите страну")

    def setCity(self):
        self.city = input("Введите город")

    def setAdress(self):
        self.address = input("Введите адрес")

    def getName(self):
        return print(self.name)

    def getDate(self):
        return print(self.date_of_bf)

    def getNum(self):
        return print(self.number)

    def getCountry(self):
        return print(self.country)

    def getCity(self):
        return print(self.city)

    def getAdress(self):
        return print(self.address)

    def display(self):
        print(f"Имя {self.name}, ДР {self.name}, Номер {self.name}, "
              f"Страна {self.name}, Город {self.name}, Адрес {self.name}, ")

obj= Human("Антон",datetime.strptime("2:10:2000","%d:%m:%Y"),"88005553535","Russia","Kld","9 aprelya")
obj.getName()
obj.setName()
print("1. Хотите добавить данные\n"
      "2. Хотите изменить данные")
user_input = input()
# class Car:
#     def __init__(self,brand:str, price:int, year_ofbuild:int,vol:float):
#         self.brand = brand
#         self.price = price
#         self.year_ofbuild = year_ofbuild
#         self.vol = vol
#
# class Human1:
#     def __init__(self,FIO:str,date:datetime,city:str):
#         self.FIO = FIO
#         self.date = date
#         self.city = city
#         print(f"Метод __init__() был вызван"
#               f"создан объект класса Human1")
#     def setFIO(self):
#         self.FIO = input("Введите новое имя")
#     def setCity(self):
#         self.city = input("Введите новый город")
#     def setDate(self):
#         self.date = datetime.strptime(input("Введите новую дату рождения"),"%Y:%m:%d")
#     def display(self):
#         print(f"Имя {self.FIO}, Дата {self.date}, "
#             f"город {self.city}")
#     def getFIO(self):
#         return self.FIO
# objHuman2 = Human1("Зубенко Михаил Петрович", ("2000-10-2"), "Шумиловка")
# objHuman2.display()
# objHuman2.setFIO()
# objHuman2.setCity()
# objHuman2.setDate()
# objHuman2.display()
# print(objHuman2.getFIO())
#
# class Human: #создали класс, задали ему имя Human
#     #создали метод с параметрами
#     def __init__(self,name,heigth,gender,age):
#         #self обращение именно к объекту, который создал конструктор __init__()
#         self.name = name
#         self.height = heigth
#         self.gender = gender
#         self.age = age
#         print(f"Метод __init__() был вызван"
#               f"создан объект класса Human")
#     #Метод класса вывод данных об объекте
#     def display(self):
#         print(f"Имя {self.name}, рост {self.height}, "
#               f"возраст {self.age} , пол {self.gender}")
#         #Создали объект
# objHuman1 = Human("Антоха",20,"Мужской",180)
# objHuman1.display()