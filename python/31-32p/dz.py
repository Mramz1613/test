import math
def proizvedenie(list_of_nums):
    return sum(list_of_nums)

users_list = list(map(int,input("Введите числа через пробел(Узнать их сумму)").split(" ")))

print(proizvedenie(users_list))

def min_of_mins(list_of_nums):
    return min(list_of_nums)

users_list = list(map(int,input("Введите числа через пробел(Узнать их минимум)").split(" ")))

print(min_of_mins(users_list))

def prime_nums(list_of_nums):
    list_of_prime = []
    x = 2
    for i in list_of_nums:
        while i % x != 0:
            x += 1
        if x == i:
            list_of_prime.append(i)
        x = 2
    return list_of_prime

users_list = list(map(int,input("Введите числа через пробел(Узнать простые числа)").split(" ")))

print(prime_nums(users_list))
def del_nums(list_of_nums,user_del):
    count = 0
    for j in range(len(list_of_nums)):
        for i in list_of_nums:
            if i == user_del:
                list_of_nums.remove(user_del)
                count +=1
    return print(f"Количество удаленных элементов равно {count}: {list_of_nums}")

users_list = list(map(int, input("Введите числа через пробел ").split(" ")))
users_del  = int(input("Введите число которое нужно удалить "))
del_nums(users_list,users_del)
def sum_of_lists(list_1,list_2):
    return print(list_1 + list_2)


users_list1 = list(map(str, input("Введите числа через пробел ").split(" ")))
users_list2 = list(map(str, input("Введите числа через пробел ").split(" ")))
sum_of_lists(users_list1,users_list2)
