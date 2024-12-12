import random
"""Задание 1
Написать игру «Быки и коровы». Программа «загадывает» четырёхзначное число и играющий должен
угадать его. После ввода пользователем числа программа
сообщает, сколько цифр числа угадано (быки) и сколько
цифр угадано и стоит на нужном месте (коровы). После
отгадывания числа на экран необходимо вывести количество сделанных пользователем попыток."""

random_znach = str(random.randint(1000,9999))
user_znach = input("Компьютер загадал случайное четырехзнвчное число: попробуйте угадать его")
while len(user_znach) < len(random_znach):
    user_znach = input("Вы ввели число вне диапазона, введите еще раз")
bulls = 0
cows = 0
attempt = 0
while random_znach != user_znach:
    print(random_znach)
    for i in random_znach:
        if i in user_znach:
            bulls += 1
    for i in range(len(random_znach)):
        if user_znach[i] in random_znach[i]:
            cows +=1
    print(f"Коров равно: {cows} Быков равно: {bulls}")
    user_znach = input("Попробуйте еще раз: ")
    attempt +=1
    cows = 0
    bulls = 0
print(f"Вы угадали вам понадобилось {attempt} попыток")


