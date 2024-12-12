# num = range(1,10)
# new_list = []
# pow_list = (i**2 for i in num)
# for i in pow_list:
#     new_list.insert(0,i)
# print(new_list[::-1])

# for i in range(0, 16):
#     print(i)
# for i in range(100, 89, -1):
#     print(i)
# print()

#цикл со счетчиком
# for i in range(1,6):
#     print(f"Цикл отработал {i} раз")
#
# #цикл выводит тольео четные числа
# for i in range(2,21,2):
#     print(i)
#
# #цикл выводит тольео нечетные числа
# for i in range(1,20,2):
#     print(str(i),sep=" ", end=" ")
# for i in range(0,5,1):
#     for j in range(1,4,1):
#         print(j, end=" ")

# text = "Python 3.12"
# for i in text:
#     print(i)
#Вывод строки по буквенно
# text1 = "World"
# count = 0
# for i in range(len(text1)):
#     print(text1[i])
#     count += 1
# print(f'Цикл сработал {count} раз')

#Срез строки
# text2 = "simple string 12345"
# print(text2)
# newstring = text2[0:6]
# print(newstring)
# print(text2[7:14])
# print(text2[14:19])

#Вывод букв с нулевой позиции с шагом 2
# text3 = "0123456789"
# for i in text3[::2]:
#         print(f"{i}", end=" ")
# for i in "word"[::-1]:
#     print(i, end=" ")
# print()

# for i in iter(int,1):
#     print("Бесконечный цикл")
"""
Задание 1 Пользователь вводит с клавиатуры два числа. Нужно показать все числа в указанном диапазоне.
Задание 2 Пользователь вводит с клавиатуры два числа. Нужно показать все нечетные числа в указанном диапазоне.
Задание 3 Пользователь вводит с клавиатуры два числа. Нужно показать все четные числа в указанном диапазоне.
Задание 4 Пользователь вводит с клавиатуры два числа. Нужно показать все числа в указанном диапазоне в порядке убывания.
Задание 5 Пользователь вводит с клавиатуры два числа. Нужно показать все нечетные числа в указанном диапазоне. Если границы диапазона указаны неправильно требуется произвести нормализацию границ. Например, пользователь ввел 33 и 13, требуется нормализация после которой начало диапазона станет равно 13, а конец 33.
"""
# num1 = int(input("ввдетите первое число: "))
# num2 = int(input("ввдетите второе число: "))
# if num1 < num2:
#     for i in range(num1, num2 + 1):
#         print(i)
# elif num1 > num2:
#     for i in range(num2, num1 + 1):
#         print(i)
# num3 = int(input("ввдетите первое число: "))
# num4 = int(input("ввдетите второе число: "))
# if num3 < num4:
#     for i in range(num3, num4 + 1):
#         if i % 2 > 0:
#             print(i)
# elif num3 > num4:
#     for i in range(num4, num3, 1):
#         if i % 2 > 0:
#             print(i)
# num5 = int(input("ввдетите первое число: "))
# num6 = int(input("ввдетите второе число: "))
# for i in range(num5, num6+1):
#      if i % 2 == 0:
#          print(i)
# num_rew = ""
# num5 = int(input("ввдетите первое число: "))
# num6 = int(input("ввдетите второе число: "))
# for i in range(num3, num4+1):
#      num_rew += str(i)
# num_rew = str(num_rew)
# print(num_rew[::-1])
#
# num7 = int(input("ввдетите первое число: "))
# num8 = int(input("ввдетите второе число: "))
# if num7 < num8:
#     for i in range(num7, num8+1):
#         if i % 2 > 0:
#             print(i)
# elif num7 > num8:
#     for i in range(num8,num7,1):
#         if i % 2 > 0:
#             print(i)
first_num = 0
second_num = 0
recepi = input("Введите номер билета(шесть цифр) ")
recepi = list(recepi)
print(recepi)
for i in recepi[0:3]:
    first_num += int(i)

for j in recepi[3:]:
    second_num += int(j)

if first_num == second_num:
    print("Ваш билет счасливый")
else:
    print("Ваш билет несчастливый")