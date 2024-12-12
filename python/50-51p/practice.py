"""
Статический метод @staticmethod дает возможность вызывать
методы класса без объекта
@ - это декоратор
"""
# Класс число
# class Num:
#     def __init__(self, chisl:int):
#         self.chisl = chisl
#     def display(self):
#         print(f"{self.chisl}")
#
#     def summa(self,objNum2):
#         print(f"{self.chisl + objNum2.chisl}")
#
#     def substraction (self,obj):
#         print(f"{self.chisl - obj.chisl}")
#
#     def division (self, pObjNum):
#         if pObjNum == 0:
#             print("Нельзя делить на 0")
#             return
#         print(f"{self.chisl / pObjNum.chisl}")
#
#     @staticmethod
#     def multi(obj1,obj2):
#         return print(obj1.chisl*obj2.chisl)
# num = Num(3)
# num2 = Num(2)
#
#
# num.summa(num2)
# num.substraction(num2)
# num.division(num2)
# Num.multi(num,num2)

class human:

    count = 0

    def __init__(self,name:str, hight:int, gender:str,age:int):
        self.name = name
        self.hight = hight
        self.gender = gender
        self.age = age
        human.count += 1

    @staticmethod
    def show_humans():
        return human.count


hunam1 = human("Вася", 180, "м", 18)
hunam2 = human("Саня", 190, "ж", 22)
hunam3 = human("Несаня", 170, "м", 18)
hunam4 = human("НеВася", 100, "ж", 12)
print(human.show_humans())

# def add():
#     add_new = input("Введите книгк")
#     add_qua = int(input("Введите кол-во"))
#     books[add_new] = add_qua
#
#
# def delete():
#     del_new = input("Введите книгк")
#     books.pop(del_new)
#
#
# def show():
#     print(books)
#
#
# if __name__ == "__main__":
#     books = {"Book": 12, "Book2": 11}
#     while True:
#         user_input = int(input("Выберите действие"))
#         match user_input:
#             case 1: add()
#             case 2: delete()
#             case 3: show()
#             case 0: quit()
#             case _: print("Нет такого")
# tupl1 = ("apple", "banana", "kiwi", "pineapple", "apelsin")
# fruit = input("Введите фрукт")
# fruit_set = set()
# count = 0
# for i in tupl1:
#     if fruit[0] in i[0]:
#         count += 1
#         fruit_set.add(i)
# print(f"Слов на туже букву {count}")
# print(fruit_set)
# class Student:
#     count = 0
#
#     def __init__(self, name:str, group:str, university:str):
#         self.name = name
#         self.group = group
#         self.university = university
#         Student.count += 1 #создание статической переменной
#
#     def set_gruop(self)-> None:
#         self.group = input("Введите группу")
#
#     def get_group(self)-> str:
#         return self.group
#     @staticmethod
#     def counter_stud():
#         print(f"Кол-во студентов {Student.count}")
#
# objStudent = Student("Vasya", "python41", "TOP Academy")
# objStudent2 = Student("Petya", "python41", "TOP Academy")
#
# print(objStudent.get_group())
# Student.counter_stud() #ызов статисеского метода