# # import time
# count = int(input("Введите длину"))
# # for i in range(count):
# #     for j in range(count):
# #         if i > j-1:
# #             print("*",end="")
# #         else: print("=",end="")
# #     print()
#
# for i in range(1,count):
#     for j in range(1,count):
#         if (j > j +i or j > j -(j*i) ):
#             print("*",end="")
#         else: print(" ",end="")
#     print()

# myStr = "Hello"
# print(f"Длинна стироки {len(myStr)}")
# print("-".join(myStr))
# print(myStr+myStr)
# print(myStr.upper())
# print(myStr.lower())
# print(myStr[-1::-1])
# print(myStr[0:5])
# print(myStr[0:4])
# polindrom = input("Введите полиндром")
# lowerpoli = polindrom.lower()
# print(lowerpoli)
#
# if lowerpoli == lowerpoli[::-1]:
#     print(True)
# else:
#     print(False)
# newStr = input("Введите строку")
# listStr = []
# listStr += newStr
# print(listStr)
# countDigit = 0
# countAlpha = 0
# for i in listStr:
#     i = str(i)
#     if i.isdigit() == True:
#         countDigit +=1
#     if i.isalpha() == True:
#         countAlpha +=1
# print(countAlpha)
# print(countDigit)
#
# usersStr = input("Введите строку")
# searchSymp = input("Введите искомый символ ")
# symCount = usersStr.count(searchSymp)
# print(symCount)
#
# usersStr = input("Введите строку")
# searchAlpha = input("Введите искомое слово")
# symSearch = usersStr.count(searchAlpha)
# print(symSearch)
#
# usersStr = input("Введите строку")
# searchAlpha = input("Введите искомое слово")
# userChange = input("Введите солово на которое будем менять")
# symSearch = usersStr.count(searchAlpha)
# print(usersStr.replace(searchAlpha,userChange))

# someTxt= "lorem ipsum dolor sit amet,1 2 3 !consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. facilisis mauris sit amet massa vitae tortor condimentum lacinia. Et malesuada fames ac turpis egestas maecenas. Nulla aliquet porttitor lacus luctus accumsan tortor posuere ac. Consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus."
# someTxt.title()
# countPrepin = 0
# countDigits = 0
# countVoskl = 0
# for i in someTxt:
#     if i.isdigit() == True:
#         countDigits += 1
#     countPrepin += i.count(",")
#     countPrepin += i.count(".")
#     countVoskl += i.count("!")
# print(countPrepin)
# print(countVoskl)
# print(countDigits)
# print(someTxt)
search = int(input("Введите искомую цифру"))
newList = list(map(int,input("Введите числа через пробел").split(" ")))
print(newList)
res = newList.count(search)
print(res)
# userInput = list(map(int,input("Введите число")))
# print(userInput)
# userLen = len(userInput)
# print(f"Сумма равна {sum(userInput)}")
# print(f"Среднее равно {sum(userInput)/userLen}")
# print(f"Нулей в числе {userInput.count(0)}")