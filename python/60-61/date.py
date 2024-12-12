# from datetime import *
#
# class Date:
#     def __init__(self,data:datetime):
#         self.date = data
#     def display(self):
#         print(f"Дата {self.date}")
#
#     def gettype(self):
#         print(type(self.date))
#
#     def sub(self,sec_ob):
#         return self.date - sec_ob.date
#
#     def plus(self,sec_ob):
#         return self.date + sec_ob
#
#
#
# if __name__ == '__main__':
#     while True:
#         first = Date(datetime(int(input("Введите год")),int(input("Введите месяц")),int(input("Введите день"))))
#         second = Date(datetime(int(input("Введите год")), int(input("Введите месяц")), int(input("Введите день"))))
#         user_choice = int(input("Выберите действие\n"
#                                 "1. Разница дат\n"
#                                 "2. Прибавить к дате\n"))
#         while user_choice != 0:
#             match user_choice:
#                 case 1: print(first.sub(second))
#                 case 2: print(first.plus(timedelta(float(input("Введите дни")))))
#                 case 0: quit()
#                 case _: print("Нет такого")
#             user_choice = int(input("Выберите действие\n"
#                                     "1. Разница введеных дат\n"
#                                     "2. Прибавить к дате дни\n"))