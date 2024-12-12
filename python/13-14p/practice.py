import random
# """
# Вложенный цикл - один цикл находится внутри другого
# Синтаксис:
# while условние_1:
#     while условние_2:
#         действие_1
#         действие_2
#
#
#
# for i in range(0,10,1):
#     for j in range(0,10,1):
#         действие_1
#         действие_2
# """
#
# for i in range(0,5,1):
#     for j in range(5):
#         print("#",end=" ")
#     print()
# print()
# for i in range(0,5,1):
#     print("*",end=" ")
# print()
# i1 = 0
# j1 = 0
# while i1<5:
#     j1=0
#     while j1<5:
#         print("0", end=" ")
#         j1+=1
#     i1+=1
#     print()
#
# start = int(input("введите начало диапазона: "))
# end = int(input("введите конец диапазона: "))
# count = 0
# summa = 0
# if start>end:
#     start,end = end,start
# for i in range(start,end+1):
#     count +=1
#     summa +=i
# print(summa)
# print(summa/count)
# def sum_and_sr (num1, num2):
#     diap = range(num1,num2+1)
#     diap = list(diap)
#     ARsum = sum(diap)
#     ARlen = len(diap)
#     res = ARsum/ARlen
#     return res, ARsum
# print(sum_and_sr(int(input("Введите первое число: ")),(int(input("Введите первое число: ")))))
#
# len_count = 0
# len_of_symb = int(input("Введите длину линии"))
# while len_count != len_of_symb:
#     print("*", end="")
#     len_count += 1
# print()
#
# def fuctarial (num):
#     diap = range(num,0,-1)
#     diap = list(diap)
#     res = 1
#     for i in range(num):
#         res = res * diap[i]
#
#     return res
# print(fuctarial(int(input("Введите число котооре хотите фактариал: "))))


"""Задание 4
Пользователь вводит с клавиатуры длину линии и
символ для заполнения линии. Нужно отобразить на
экране горизонтальную линию из введенного символа,
указанной длины.
Например, если было введено 5 и &, тогда вывод на
экран будет такой: &&&&&.

Задание 5
Показать таблицу умножения для числа, введенного
пользователем. Например, если пользователь вводит
число 7, нужно показать:
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
…
Задание 6
Пользователь вводит с клавиатуры две границы диапазона и число. Если число не попадает в диапазон,
программа просит пользователя повторно ввести число,
и так до тех пор, пока он не введет число правильно. Программа отображает все числа диапазона, выделяя число
восклицательными знаками. Например:
1 2 3 !4! 5 6 7."""

# symb = input("Введите символ ")
# nums_of_symbs = int(input("Введите количество символов "))
# count = 0
# while count != nums_of_symbs:
#     print(symb, end="")
#     count +=1
# print()
#
# num_multy = int(input("Введите число чтобы увидеть его таблицу умножения"))
#
# for i in range(11):
#     print(f"{num_multy}*{i} = {num_multy*i}")


# start = int(input("введтие старт диапазона "))
# end = int(input("введтие конец диапозона "))
# num_faw = int(input("Введите число из диапазона"))
# if start > end:
#     start,end = end , start
# while num_faw < start or num_faw > end:
#     num_faw = int(input("Введите число из диапазона"))
# for i in range(start,end):
#     if i != num_faw:
#         print(i, end=" ")
#     elif i == num_faw:
#         print(f"!{num_faw}!",end=" ")
#     continue
print("Вам загодали число попробуйте угадать")
set_nums = random.randint(1,501)
print(set_nums)
guess = int(input("Введите вашу догадку"))
count = 0

while guess != set_nums and guess != 0:
    if guess > set_nums:
        print("Вваше число больше загаданого")
        count +=1
        guess = int(input("Введите вашу догадку(для выхода введиите 0)"))
        continue
    elif guess < set_nums:
        print("Ваше число меньше загадонного")
        count += 1
        guess = int(input("Введите вашу догадку(для выхода введиите 0)"))
        continue

else:
    print(f"Вам понадобилось {count} попыток")