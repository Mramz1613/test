# """
# Функции с параметрами:
#  def name_fun(parametr):
#     действие_1 'Тело функции'
#
# Обязательные и необязательные параментры
#
#
# Рекурсия это функция которая вызывает сама себя
# Анонимная функция - функция без имени
# """
# def function1(number):
#     print(number)
#
# number = 5
# function1(number) # Вызовет ошибку елси не передать обязательного параметра
#
# def function2(number=0):
#     print(number)
#
# number = 17 ZXCard@12
# function2()

# def factarial(user_num):
#     res = 1
#     for i in range(user_num):
#         res *= user_num
#         user_num -= 1
#     return res
#
# print(factarial(3))
#
# user_num = int(input("Введите число: "))
# #Найти факториал числа с помощью рекурсии
# def factarial2(user_num):
#     if user_num == 1:
#         return 1
#     return factarial2(user_num-1)*user_num
#
# print(factarial2(user_num))
#
#
# def f1(num):
#     print(num)
#     if num == 0:
#         return num
#     f1(num-1)
#
# f1(5)
# lst = [3,7,6,5,1]
# lst2 = list(map(lambda num:num * 2,lst))
# print(lst2)
# lst.sort()
# print(lst)
# def maksimum(user_enter):
#     return print(f"Максимальное число это: {max(user_enter)}")
#
# user_list = list(map(int,input("Введите числа через пробел").split(" ")))
# maksimum(user_list)
#
# def prime_nums(list_of_nums):
#     list_of_prime = []
#     count = 0
#     x = 2
#     for i in list_of_nums:
#         if i == 1 or i ==2:
#             list_of_nums.remove(i)
#     for i in list_of_nums:
#         while i % x != 0:
#             x += 1
#         if x == i:
#             list_of_prime.append(i)
#             count += 1
#         x = 2
#     return print(f"Количесво простых чисел в списке равно: {count}")
# user_list = list(map(int,input("Введите числа через пробел").split(" ")))
# prime_nums(user_list)
# """3.Напишите функцию, которая отображает на экран
# форматированный текст, указанный ниже:
# “Don't let the noise of others' opinions
# drown out your own inner voice.”
# Steve Jobs
#
# 4.Напишите функцию, которая принимает два числа в качестве параметра
# и отображает все нечетные числа между ними."""
#
# def Jobs():
#     print('"Don\'t let the noise of others\' opinions\n'
#           '"drown out your own inner voice."\n'
#           " Steve Jobs")
# Jobs()
# def odd(start,end):
#     lst = []
#     for i in range(start,end+1):
#         if i % 2 != 0:
#             lst.append(i)
#     return print(lst)
#
# start = int(input())
# end = int(input())
# odd(start,end)
import random

def generate_secret_number():
    """Генерация случайного четырёхзначного числа без повторяющихся цифр."""
    digits = list(range(10))
    random.shuffle(digits)
    secret_number = ''.join(map(str, digits[:4]))
    return secret_number


def count_bulls_and_cows(secret_number, guess):
    """Подсчет количества быков и коров."""
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1
    return bulls, cows


def play():
    """Основная функция игры."""
    secret_number = generate_secret_number()
    pop = 0
    print("Добро пожаловать в игру 'Быки и коровы'!")
    print("Попробуйте угадать загаданное четырёхзначное число.")

    while True:
        guess = input("Введите вашу догадку: ")
        if len(guess) != 4 or not guess.isdigit():
            print("Пожалуйста, введите четырёхзначное число.")
            continue

        bulls, cows = count_bulls_and_cows(secret_number, guess)
        pop += 1

        print(f"Быки: {bulls}, Коровы: {cows}")
        print(secret_number)

        if bulls == 4:
            print(f"Поздравляем! Вы угадали число {secret_number} за {pop} попыток!")
            break

play()