"""
Вложеные условия
if условие:
    if условие:
        Действие_1
"""
# num3 = 0
# if num3 > 0:
#     if num3 % 2 == 0:
#         print("Это число четное")
#     else:
#         print("Это число нечетное")
# elif num3 == 0:
#     print("Это число равно нулю")
# else:
#     print("Это число отрицательное")
# num4 = int(input("Введите число "))
# if num4 > 0:
#     if num4 % 3 == 0:
#         print("Это число кратно трем")
#     else:
#         print("Это число не кратно трем")
# elif num4 == 0:
#     print("Это число равно нулю")
# else:
#     print("Это число отрицательное")
#

# if num4 % 3 == 0:
#     print("Это число кратно 3")
# if num4 % 7 == 0:
#     print("Это число кратно 7")
# if num4 % 9 == 0:
#     print("Это число кратно 9")
# if num4 % 3 != 0 and num4 % 7 != 0 and num4 % 9 != 0:
#     print("Это число не кратно 3 7 9")
# def is_subset(list1, list2):
#     cop_list1 = list1.copy()
#     cop_list2 = list2.copy()
#     str_list1 = ''
#     str_list2 = ''
#     for i in cop_list1:
#         str_list1 += str(i)
#     for i in cop_list2:
#         str_list2 += str(i)
#     str_list1 = set(str_list1)
#     str_list2 = set(str_list2)
#     is_it_subset = {}
#     is_it_subset = str_list1.issubset(str_list2)
#     if is_it_subset == True:
#         return True
#     else:
#         return False
# print(is_subset([1,2,3],[1,2,4,5]))
# num1 = int(input("Введите число"))
# if num1 % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")
#
# num2 = int(input("Введите число"))
# if num1 % 7 == 0:
#     print("Number is multiple 7")
# else:
#     print("Number is not multiple 7")
hours = int(input("Введите который сейчас час"))
minites = int(input("Введите которая сейчас минута"))
res = 86400
secs = hours*3600 + minites*60
res_in_m = (res - secs)/3600/60
res_in_h = (res - secs)/3600
res_in_s = (res - secs)
act = input("Выберите во что переводить: ч, м, с ")
if act == "ч":
    print(int(res_in_h))
    print("часов осталось до конца дня", end=" ")
elif act == "м":
    print(int(res_in_m), end=" ")
    print("Минут осталось до конца дня")
elif act == "с":
    print(int(res_in_s), end=" ")
    print("Секунд осталось до конца дня")
else:
    print("Гдето ошибка")

45000
# print("print() - ф-ция вызова на экран")
# num = 18
# print(num)
# print(10 == 1)
# print(f"Переменная равно: {num}")
# print("Переменная равна:", num)
# print("end=\"\" команда чтобы убрать перенос строки", end=" ")
# print("end=\"\" команда чтобы убрать перенос строки", end=" ")
# print("end=\"\" команда чтобы убрать перенос строки")
# print("sep=\"\"", "добавляет", "разделитель", sep=")))))")
# #создание и ввод строковой переменной string - str
# name = input("Введите ваше имя ")
# print(f"Вас зовут {name}, так?")
# your_age = int(input("Введите ваш возраст "))
# print(f"Вам {your_age} лет, так?")
# your_num = float(input("Введите ваше число "))
# print(f"Ваше {your_num} число, так?")
