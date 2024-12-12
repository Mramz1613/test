import random
userUpperPredel = int(input("Введите верхний предел случайного числа: "))
userLowerPredel = int(input("Введите нижний предел случайного числа: "))
userRange = int(input("Введите длину диапазона чисел "))
firstRandomList = []
secondRandomList = []
for i in range(userRange):
    firstRandomList.append(random.randint(userLowerPredel,userUpperPredel))
    secondRandomList.append(random.randint(userLowerPredel, userUpperPredel))
obshiyRandomList = list(firstRandomList+secondRandomList)
print(f"Первый список случайных чисел {firstRandomList}")
print(f"Второй список случайных чисел {secondRandomList}")
print(f"Общий список случайных чисел {obshiyRandomList}")
print(f"Общий список случайных чисел без повторений {list(set(obshiyRandomList))}")
