"""
Цикл - это повторяющиесе последовательность действий
с условием выхода из цикла или цикл бесконечный
Виды циклов:
while условие:
    действие_1

Расшифровка: Пока условие верно, выполняется действие_1

for i in range(0,10,1)
    действие_1
Расшифровка: Пока переменная i находится в диапозоне от 0 до 10(не включительно)
c шагом 1
"""
def speed_of_donw(arg):
    size = float(input("Введите вес файла в гб: "))
    speed = float(input("Введите скорость скачивания в битах в сек: "))
    speed_in_bite = speed/8
    size_in_bite = size*1000*1000*1000
    res = size_in_bite / speed_in_bite
    if arg == "c":
        return print(f'Вам понадобится {res} секунд')
    elif arg == "м":
        return print(f'Вам понадобится {res / 60} минут')
    elif arg == "ч":
        return print(f'Вам понадобится {res / 60 / 60} часов')
    else:
        None







print(speed_of_donw(input("Введите 'c' или 'м' или 'ч'")))
# def diam_action(arg, pi = 3.14):
#     if arg == "пл":
#         diam = int(input("Введите диаметр: "))
#         rad = diam / 2
#         res = pi *rad**2
#         return res
#     elif arg == "пр":
#         diam = int(input("Введите диаметр: "))
#         rad = diam / 2
#         res = 2 * pi*rad
#         return res
#     else:
#         return None
#
# print(diam_action(input("Ввведите \"пл\" или \"пр\"")))
# num4 = 11
# while num4 <= 25:
#     num4 = num4 + 1
#     if num4 % 2 == 0:
#         print(f"Число {num4} четное")
#     else:
#         print(f"Число {num4} не четное")
#Цикл с условием
# num = 0
# while num != 5:
#     print(f"num= {num}")
#     num = num + 1
#
# #Бесконечный цикл 1
# # while True:
# #     print(f"Бесконечный цикл")
# #Бесконечный цикл 2
# num1 = 0
# while num1 == 0:
#     print(f"Бесконечный цикл 2")
#     break #команда прерывания цикла
# print(f"Строка после цикла")
#
# #Разница break и continue
#
# num2 = 12
# while num2 > 10:
#     if num2 == 11:
#         print("Проверка условия цикла")
#         continue #прерывание цикла, все что после контин не выполнится
#         print(f"строка после контин не выполнится")
#     if num2 == 12:
#         print(f"Строка перед break")
#         break #Прерывание цикла
#         print(f"строка после контин не выполнится")
# #Цикл со счетчиком
# num3 = 5
# count = 0#счетчик, считает сколько раз выполнился цикл
# while num3 <10:
#     print(f"Цикл выполнился: {count} раз")
#     print(f"Переменная num3 = {num3}")
#     num3 += 1
#     count += 1