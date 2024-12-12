import random
# def my_sort():
#     unsort = []
#     for i in range(10):
#         unsort.append(random.randint(0,99))
#     print(unsort)
#     for i in range(len(unsort)):
#         lowest_value_index = i
#         for j in range(i+1,len(unsort)):
#             if unsort[j] < unsort[lowest_value_index]:
#                 lowest_value_index = j
#         unsort[i],unsort[lowest_value_index] = unsort[lowest_value_index],unsort[i]
#     print(unsort)
# my_sort()
"""Задание 1 Написать программу, выполняющую сортировку списка целых чисел методом слияния."""
# def msort4(x):
#     if len(x) < 20:
#         return sorted(x)
#     result = []
#     mid = int(len(x) / 2)
#     y = msort4(x[:mid])
#     z = msort4(x[mid:])
#     i = 0
#     j = 0
#     while i < len(y) and j < len(z):
#         if y[i] > z[j]:
#             result.append(z[j])
#             j += 1
#         else:
#             result.append(y[i])
#             i += 1
#     result += y[i:]
#     result += z[j:]
#     return result
# x = [1,3,5,1,2,0,1,10,21,11,12,31,12,55,123,323,12,31,0,10,12,3,0,1,456,43,7,5,3]
# print(msort4(x))
def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Т. к. длина списков применяется часто, создадим для удобства переменные
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если 1-й элемент левого подсписка меньше, добавляем его
            # в сортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если 1-й элемент правого подсписка меньше, добавляем его
            # в сортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Когда достигнут конец левого списка, добавляем элементы правого списка
        # в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Когда достигнут конец правого списка, добавляем элементы левого списка
        # в сортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):
    # Возвращаем список, когда он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    # Чтобы найти середину списка, применяем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем сортированные списки в результирующий
    return merge(left_list, right_list)

# Проверяем, что всё работает
random_list_of_nums = [120, 45, 68, 250, 176]
random_list_of_nums = merge_sort(random_list_of_nums)
print(random_list_of_nums)