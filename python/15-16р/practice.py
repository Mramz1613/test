"""
while условие:
    действие_1
else:
    действие после завершение цикла

break - полностью прирывает цикл и выходит из него
"""
# num = 1
# while num<=5:#пока условие истино заходим внутрь цикла
#     print(f"Цикл выполнился {num} раз")
#     num += 1
#     if num == 4:
#         break
# else: #else не сработал так как цикл прервался досрочно, из-за того что сработал break
#     print(f"Цикл отработал {num-1} раз")
#     print(f"строка вывелась если цикл отработал до конца")
# start = int(input("введите начало диапазона"))
# end = int(input("введите конец диапазона"))
# if start > end:
#     start, end = end, start
# summ_even = 0
# summ_odd = 0
# summ_nine = 0
# count_even = 0
# count_odd = 0
# count_nine = 0
# for i in range(start, end+1):
#     if i % 2 == 0:
#         summ_even += i
#         count_even += 1
# for j in range(start, end+1):
#     if j % 2 > 0:
#         summ_odd += j
#         count_odd += 1
# for k in range(start, end+1):
#     if k % 9 == 0:
#         summ_nine += k
#         count_nine += 1
# print(f"Сумма четных чисел равна {summ_even}", f"Средние равно {summ_even/count_even}")
# print(f"Сумма четных чисел равна {summ_odd}" , f"Средние равно {summ_odd/count_odd}")
# print(f"Сумма четных чисел равна {summ_nine}" , f"Средние равно {summ_nine/count_nine}")
#
# symb = input("Введите символ")
# symb_len = int(input("Введите длину"))
# for i in range(symb_len):
#     print(symb)
# user_num = int(input("Введите число "))
# if user_num == 7:
#     print("Good bye!")
# elif user_num < 0:
#     print("Number is negative")
# elif user_num > 0:
#     print("Number is positive")
# elif user_num == 0:
#     print("Number is equal to zero")
user_enter = list(map(int,input("Введите числа ").split(" ")))
user_min = 0
user_max = 0
user_summ = 0
if 7 in user_enter:
    print("Good bye")
else:
    user_min = min(user_enter)
    user_max = max(user_enter)
    user_summ = sum(user_enter)
print(f"Минимум равен {user_min}, Максимум равен {user_max}, Сумма равна {user_summ}")
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums)
nums = list((map(lambda x:(x**2), nums)))
print(nums)
nums = list(filter(lambda x: x % 5 == 0, nums))
print(nums)
nums = list(map(lambda x: x/5,nums))
print(nums)
nums = list(map(int,nums))
print(nums)