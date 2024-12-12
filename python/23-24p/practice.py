import random
"""
1.Пользователь с клавиатуры вводит элементы списка
целых и некоторое число. Необходимо посчитать сколько раз
данное число присутствует в списке. Результат
вывести на экран.1.Пользователь с клавиатуры вводит элементы списка
целых и некоторое число. Необходимо посчитать сколько раз
данное число присутствует в списке. Результат
вывести на экран.
"""

# userEnter = list(input("Введите числа(через пробел)").split(" "))
# userSearch = input("Введите искомое число")
# print(userEnter.count(userSearch))

# userEnter_2 = list(map(int,input("Введите числа(через пробел)").split(" ")))
# print(sum(userEnter_2))
# print(sum(userEnter_2)/len(userEnter_2))
"""
3.Есть некоторый текст. Реализуйте следующую функциональность:
■ Изменить текст таким образом, чтобы каждое предложение начиналось
с большой буквы;
■ Посчитайте сколько раз цифры встречаются в тексте;
■ Посчитайте сколько раз знаки препинания встречаются в тексте;
■ Посчитайте количество восклицательных знаков в
тексте
"""
someTxt= "Ехал грека через 2 часа! реку. видит грека в реке рак. сунул в воду грека руку. рак за руку греку цап."
print(someTxt)
someTxtList = someTxt.split(".")
someTxtList.pop(-1)
countPrepin = 0
countDigits = 0
countVoskl = 0
for i in someTxt:
    if i.isdigit() == True:
        countDigits += 1
    countPrepin += i.count(",")
    countPrepin += i.count(".")
    countPrepin += i.count("!")
    countPrepin += i.count("?")
    countVoskl += i.count("!")
someTxt2 = ""

for i in someTxtList:
    i = str(i)
    if i[0] != " ":
        i = i[0:]
        i = i.capitalize()+". "
        someTxt2 += i
    elif i[0] == " ":
        i = i[1:]
        i = i.capitalize()+". "
        someTxt2 += i
print(countPrepin)
print(countVoskl)
print(countDigits)
print(someTxt2)
"""
Задание 1:
В списке целых, заполненном случайными числами,
определить минимальный и максимальный элементы,
посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать
количество нулей. Результаты вывести на экран.
"""
userUpperPredel = int(input("Введите верхний предел случайного числа: "))
userLowerPredel = int(input("Введите нижний предел случайного числа: "))
userRange = int(input("Введите длину диапазона чисел "))
randomList = []
for i in range(userRange):
    randomList.append(random.randint(userLowerPredel,userUpperPredel))
countZero = 0
countNegative = 0
countPosetive = 0
print(randomList)
for i in randomList:
    if i == 0:
        countZero +=1
    elif i < 0:
        countNegative +=1
    elif i > 0:
        countPosetive +=1
print(countZero)
print(countNegative)
print(countPosetive)