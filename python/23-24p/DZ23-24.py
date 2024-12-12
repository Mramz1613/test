# import random
# """
# В списке целых, заполненном случайными числами вычислить:
# ■ Сумму отрицательных чисел
# ■ Сумму четных чисел;
# ■ Сумму нечетных чисел;
# ■ Произведение элементов с индексами кратными 3;
# ■ Произведение элементов между минимальным и максимальным элементом;
# ■ Сумму элементов, находящихся между первым и последним положительными элементами
# """
# userUpperPredel = int(input("Введите верхний предел случайного числа: "))
# userLowerPredel = int(input("Введите нижний предел случайного числа: "))
# userRange = int(input("Введите длину диапазона чисел "))
# randomList = []
# for i in range(userRange):
#     randomList.append(random.randint(userLowerPredel,userUpperPredel))
# countZero = 0
# countNegative = 0
# countPosetive = 0
# print(f"Список случайных чисел от {userUpperPredel} до {userLowerPredel}: {randomList}")
# listNeg = []
# listPos = []
# listDevBy3 = []
# listOdd = []
# listEven = []
# for i in randomList:
#     if i == 0:
#         countZero +=1
#     elif i < 0:
#         countNegative +=1
#         listNeg.append(i)
#     elif i > 0:
#         countPosetive +=1
#         listPos.append(i)
#     if i % 2 == 0:
#         listEven.append(i)
#     else: listOdd.append(i)
#     if i % 3 == 0 and i != 0:
#         listDevBy3.append(i)
#
# print(f"Количество нулей {countZero}")
# print(f"Количество негативных {countNegative}")
# print(f"Количество позитивных {countPosetive}")
# print(f"Сумма негативны {sum(listNeg)}")
# print(f"Список позитивных  {listPos}")
# print(f"Сумма четных {sum(listEven)}")
# print(f"Сумма нечетных {sum(listOdd)}")
# print(f"Список кратных трем {listDevBy3}")
# buffer_ListDevBy3 = 1
# for i in listDevBy3:
#     buffer_ListDevBy3 *= i
# print(f"Произведение кратных трем {buffer_ListDevBy3}")
# print(f"Произведение максимума и минимума {max(randomList)*min(randomList)}")
# firstPos = 0
# lastPos = 0
# for i in randomList:
#     if i > 0:
#         firstPos = i
#         break
# for i in reversed(randomList):
#     if i > 0:
#         lastPos = i
#         break
# firstIndex = randomList.index(firstPos)
# revRandomList = list(reversed(randomList))
# lastIndex = (revRandomList.index(lastPos)+1)*-1
# multyFirstLast = 1
# for i in randomList[firstIndex:lastIndex]:
#     multyFirstLast *= i
# if multyFirstLast == 1:
#     multyFirstLast = 0
# print(f"Произведение всех чисел между первым положительным и последним положительным число {multyFirstLast}")
def color_invert(*rgb):
    return tuple(255 - c for c in rgb)

print(color_invert(255,255,255))