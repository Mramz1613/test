"""Список(list) - хранит любые типы данных
list1 = []
Множество(set) - хранит любые типы данных, без повторений
set1 = {}
Кортеж(tuple) - храенит любые типы данных, неизменяетмые
tuple1 = ()
Словарь(dictionary) - хранит любыет типы данных, хранит как пару ключ:значение
Dict1 = {Ключ: значение}"""

myTuple = tuple(["Антоха",2,4,5,61,True])
print(myTuple)
myTuple1 = ()
myTuple2 = (21,12,True,False)
myTuple3 = tuple(i*2 for i in range(10))
print(myTuple3)
myTuple2.index()
























# MySet1 = {"a", 10, True}
# print(f"{MySet1=}")  # set выводится в случайном порядке
#
# MySet2 = {"b",10, False, 10}
# print(f"{MySet2=}")
# # Пересечние множеств общие элементы дял первого и второго множества
# resSet = MySet1.intersection(MySet2)
# print(resSet)
# resSet = MySet1 & (MySet2)
# print(resSet)
# #Разница множеств
# resDiff = MySet1.difference(MySet2)
# print(resDiff)
# #Общая разность множеств
# resSymDiff = MySet1.symmetric_difference(MySet2)
# print(resSymDiff)
# #Метод isdisjoin() если множество не содержат общих элементов, то вернет True
# print(MySet2.isdisjoint(MySet1))
# #Обединение множеств
# unionSet = MySet1.union(MySet2)
# print(unionSet)
# unionSet = MySet1 | (MySet2)
# print(unionSet)
# #Стравнение множеств - возвращает булевое знач
# list1 = [3,2]
# MySet3 = set(list1)
# print(list1,MySet3)
# MySet4 = set([3,1])
# bool_val = MySet3 > MySet4
# print(bool_val)
#
#
#
#
#
#
#
#
# MySet = set()
# MySet.add(1)
# MySet.add(2)
# MySet.add(3)
# MySet.add(4)
# MySet.add(5)
# print(MySet)
# frozenset
# print(MySet)
# print(len(MySet))
# MySet.remove(5)
# print(MySet)
# New_set = MySet.discard()
# print(New_set)
