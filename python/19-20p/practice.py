# count = 0
# for i in range(100,1000):
#     n1 = i//100
#     n2 = i//10%10
#     n3 = i%10
#     if n1==n2 or n2==n3 or n3==n1:
#         count+=1
# print(count)
"""
Список - это набор разных типов данных, объедененных одним именем
"""
# list1= [1,2,3,4] #создали список
# list2 = ['a','b','c','d']
# list3 = [1,'a',"asd", 0.5, True, None,[12,42,True]]
# list4 = [10, 1, 4,5,123,45,15]
# #Методы списков - это готовые функции для работы со списком
# list1.append(100)
# print(list1)
# list2.insert(2,'y')
# print(list2)
# list2.sort()
# print(list2)
# list2.reverse()
# print(list2)
# list4.sort()
# print(list4)
# print(list4[-1::-1])
# list5=[]
# list5 = list2
# list5.clear()
# print(list2)
# print(list5)
# list6 = list3.copy()
# list3.clear()
# print(f"После Clear{list3}")
# print(f"После Clear{list6}")
# list6.pop()
# print(list6)
#заполение списка через цикл
# list1 = []
# for i in range(1,7):
#     list1.append(i)
# print(list1)
# for i in range(3):
#     list1.append(int(input()))
# print(list1)
# size = int(input("Размер клетки "))
# for j in range (size):
#     for i in range(size):
#         print("*"*size,"+"*size,end="")
#     print()
# for j in range (size):
#     for i in range(size):
#         print("+"*size,"*"*size,end="")
#     print()

userInput = list(map(int,input("Введите число")))
print(userInput)
userLen = len(userInput)
print(f"Сумма равна {sum(userInput)}")
print(f"Среднее равно {sum(userInput)/userLen}")
print(f"Нулей в числе {userInput.count(0)}")