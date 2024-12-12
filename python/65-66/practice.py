from abc import *
import math
class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Figure):
    def __init__(self,side:int):
        self.side = side

    def area(self)->int:
        return self.side**2

    def perimeter(self)->int:
        return self.side*4

class Circle(Figure):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2*3.14 * self.radius

class Rectangle(Figure):
    def __init__(self,f_side,s_side):
        self.f_side = f_side
        self.s_side = s_side

    def area(self):
        return self.f_side*self.s_side

    def perimeter(self):
        return 2*(self.f_side+self.s_side)


class Triangle(Figure):
    def __init__(self,f_side,s_side,th_side):
        self.f_side = f_side
        self.s_side = s_side
        self.th_side = th_side

    def perimeter(self):
        return self.f_side+self.s_side+self.th_side

    def area(self):
        p = Triangle.perimeter(self)/2
        return math.sqrt(p*(p-self.f_side)*(p-self.s_side)*(p-self.th_side))

tre =Triangle(3,4,5)
print(tre.area())

class Human(ABC):
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def say(self):
        pass

    @abstractmethod
    def info_about_profession(self):
        pass

class President(Human):
    def __init__(self, name, age, gender,education):
        super().__init__(name, age, gender)
        self.education = education

    def say(self):
        print(f"{self.name} сказал 'Ввожу налог на воздух'")

    def info_about_profession(self):
        print(f"Президент занимает руководящую должность в стране, принимает или отвергает законы, имеет {self.education}")

class Driver(Human):
    def __init__(self, name, age, gender,car):
        super().__init__(name, age, gender)
        self.car = car
    def say(self):
        print(f"{self.name} Сказал 'До центра 500 рублей'")

    def info_about_profession(self):
        print(f"Развозит людей на машине {self.car}")

class Cook(Human):
    def __init__(self, name, age, gender,knife):
        super().__init__(name, age, gender)
        self.knife = knife

    def say(self):
        print(f"{self.name} Сказал 'Я не буду это готовить'")

    def info_about_profession(self):
        print(f"Готовит еду используя {self.knife}")


vova = President("Вова",66,"м","Высшее образование")
vova.say()
vova.info_about_profession()
drive = Driver("Вася",30,'м',"Toyota")
drive.say()
drive.info_about_profession()
ya = Cook("Ваня",23,"м","Японский нож")
ya.say()
ya.info_about_profession()

class Fraction:
    def __init__(self,a:int,b:int):
        if isinstance(a,int) is False or isinstance(a,int) is False:
            raise ValueError("Вы ввели не коретный тип данных")
        self.a = a
        self.b = b
        if self.b == 0:
            self.b = int(input("Знаменатель не может быть равен нулю"))

    def mul (self, other):
        return Fraction(self.a*other.a,self.b*other.b)

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def dev (self,other):
        return Fraction(self.a*other.b,self.b*other.a)

    def __truediv__(self, other):
        return Fraction(self.a * other.b, self.b * other.a)

    def display(self):
        print(f"{self.a}/{self.b}")

    def summ(self,other):
        if self.b == other.b:
            return Fraction(self.a+other.a,self.b)
        else:
            return Fraction(self.a*other.b+other.a*self.b)

    def __eq__(self, other):
        return self.a / self.b == other.a / other.b

    def __ne__(self, other):
        return not (self.a / self.b == other.a / other.b)
f = Fraction(1,4)
s = Fraction(1,2)
print(f != s)
"""Работа с файлами"""
my_file = open("text.txt","w",encoding="utf-8")  #если такой файл уже есть будет создан новый
my_file.write("привет🤢🍌")
my_file.close()
with open("text.jpeg","x", encoding="utf-8") as my_file:
    pass