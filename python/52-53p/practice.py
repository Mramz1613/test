# class drob:
#     def __init__(self, cisl:int,znam:int):
#         self.cisl = cisl
#         while znam == 0:
#             print("Не может быть равен нулю")
#             znam = int(input("введите знаменатель"))
#         self.znam = znam
#         print("Вызван метод инит")
#
#     def set_chisl(self):
#         self.cisl = int(input("Введите числитель"))
#         return self.cisl
#
#
#     def set_znam(self):
#         self.znam = int(input("Введите знаменатель"))
#         while self.znam == 0:
#             self.znam = int(input("Введите числитель(не ноль)"))
#         return self.znam
#
#
#     def summ(self,pObj):
#       if self.znam == pObj.znam:
#           print(f"{self.cisl + pObj.cisl} \n"
#                 f"--- \n"
#                 f"{self.znam}")
#       else:
#           print(f"{(self.cisl*pObj.znam) + pObj.cisl * self.znam} \n"
#                 f"--- \n"
#                 f"{self.znam*pObj.znam}")
#
#
# objFr1 = drob(3,4)
# objFr2 = drob(int(input("Введите числ")),int(input("Введите знам")))
# print(objFr1.summ(objFr2))

#Инкапсуляция - возможность програииы скрыть атрибуты класса

# class Person:
#     def __init__(self,name:str,age:int,salary:float):
#         self.name = name
#         self.age = age
#         self.__salary = salary
#
#     def display(self) -> None:
#         print(f"Имя: {self.name}, Возраст: {self.age}, ЗП: {self.__salary}")
#
#     def getSalary(self)->float:
#         return self.__salary
#
#     def setSalary(self)->None:
#         self.__salary = float(input("Введите зп"))
# firstPer = Person("Vasya",18,23.56)
# firstPer.display()
# print(firstPer.age)
# print(firstPer.getSalary())
# print(firstPer.name)
# firstPer.name = "Nastya"
# firstPer._Person__salary = 100
# firstPer.display()
'''
Создайте класс «Страна». Необходимо хранить в
полях класса: название страны, название континента,
количество жителей в стране, телефонный код страны,
название столицы, название городов страны. Реализуйте
методы класса для ввода данных, вывода данных,
реализуйте доступ к отдельным полям через методы класса.

'''


class Country:

    def __init__(self,name_of_country:str,name_of_continent:str,population:float,telephone_code:str,name_of_cap:str,name_of_cities:list):
        self.name_of_country = name_of_country
        self.name_of_continent = name_of_continent
        self.population = population
        self.telephone_code = telephone_code
        self.name_of_cities = name_of_cities
        self.name_of_cap = name_of_cap

    def set_name_of_country(self)->None:
        self.name_of_country = input("Введите название страны")

    def get_name_of_country(self)->str:
        return self.name_of_country

    def set_name_of_continent(self)->None:
        self.name_of_continent = input("Введите континент")

    def get_name_of_continent(self)->str:
        return self.name_of_continent

    def set_population(self)->None:
        self.population = float(input("Введите население"))

    def get_population(self)->float:
        return self.population

    def set_telephone_code(self)->None:
        self.telephone_code = input("Введите код страны начиная с +")
        while self.telephone_code[0] != "+":
            self.telephone_code = input("Введите код страны начиная с +")

    def get_telephone_code(self)->str:
        return self.telephone_code

    def set_name_of_cities(self)->None:
        self.name_of_cities = input("Введите города через пробел").split(" ")
        for i in self.name_of_cities:
            for j in i:
                if j == " " or j == "":
                    j.replace(j,",")

    def get_name_of_cities(self)-> list:
        return self.name_of_cities

    def set_name_of_cap(self)->None:
        self.name_of_cap = input("Введите название столицы")

    def get_name_of_cap(self)->str:
        return self.name_of_cap

    def display(self)->None:
        print(f"{self.name_of_country}, {self.name_of_continent}, {self.population}, {self.telephone_code}, {self.name_of_cities}, {self.name_of_cap}")


objCountry = Country("Russia","Euarasia",128.9,"+7","Moscow",["Kld","Msc", "Spb"])
# objCountry.display()
# objCountry.set_name_of_cities()
# objCountry.display()

if __name__ == "__main__":
    while True:
        print("1.Показать все данные по стране \n"
              "2.Поменять название страны")
        choice = int(input("Выберите действие\n"))
        match choice:
            case 1: objCountry.display()
            case 2: objCountry.set_name_of_country()
            case 0: quit()
            case _: "Nакого нет\n"
