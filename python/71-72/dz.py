# with open("first.txt","r",encoding="utf-8") as first:
#     with open("second.txt", "r", encoding="utf-8") as second:
#         with open("res.txt", "w", encoding="utf-8") as res:
#             f_list = first.readlines()
#             s_list = second.readlines()
#             for i in f_list:
#                 if i not in s_list:
#                     res.write(i)
#             for i in s_list:
#                 if i not in f_list:
#                     res.write(i+"\n")

# with open("stat.txt","r",encoding="utf-8") as stat:
#     with open("res2.txt", "w", encoding="utf-8") as res:
#         out_put = stat.read()
#         stat.seek(0)
#         out_put_lines = stat.readlines()
#         print(out_put)
#         print(len(out_put_lines))
#         sogl = {"б","в","г","д","ж","з","к","л","м","н","п","р","с","т","ф","х","ц","ч","ш","щ","ъ","ь"}
#         glasn = {"a","е","ё","и","й","о","у","ы","э","ю","я"}
#         char_count = 0
#         sogl_count = 0
#         glasn_count = 0
#         num_count = 0
#         for i in out_put.lower():
#             if isinstance(i,str):
#                 char_count +=1
#
#         for i in out_put.lower():
#             if i in sogl:
#                 sogl_count += 1
#
#         for i in out_put.lower():
#             if i in glasn:
#                 glasn_count += 1
#
#         for i in out_put:
#             if i.isdigit():
#                 num_count += 1
#
#         res.write(f"Кол-во символов: {char_count}\n"
#                   f"Кол-во строк: {len(out_put_lines)}\n"
#                   f"Кол-во гласн букв: {glasn_count}\n"
#                   f"Кол-во согласн букв: {sogl_count}\n"
#                   f"Кол-во цифр: {num_count}\n")
#         print(char_count)
#         print(glasn_count)
#         print(sogl_count)
#         print(num_count)

# with open("stat.txt","r",encoding="utf-8") as cur_file:
#     with open("res3.txt","w",encoding="utf-8") as res_file:
#         res_file.write(cur_file.readlines()[-1])
# with open("stat.txt","r",encoding="utf-8") as file:
#     all_lines = file.readlines()
#     print(f"Самая длинная строка:{max(all_lines)}")


# user_input = input("Введите слово")
# with open("stat.txt","r",encoding="utf-8") as file:
#     all_str = file.read()
#     count_sub = 0
#     new = all_str.split(" ")
#
#     for i in new:
#         if i == user_input:
#             count_sub +=1
#     print(f"Слово {user_input} встречается {count_sub} раз")
#
# user_input2 = input("Введите слово котооре заменяем")
# user_input3 = input("Введите слово на которое заменяем")
# with open("stat.txt","r",encoding="utf-8") as file:
#     with open("stat2.txt", "w", encoding="utf-8") as file2:
#         new_file = file.read()
#         new_file = new_file.replace(user_input2,user_input3)
#         print(new_file)
#         file2.write(new_file)

#
# start = int(input("Начало диапозона:"))
# finish = int(input("Конец диапозона:"))
# result = 0
#
# # for i in range(start, finish + 1):
#     result += 1
# print(f"Сумма чисел:{result};Среднее арифметическое:{result / (finish - start)}")
#
# start = int(input("Начало диапозона:"))
# finish = int(input("Конец диапозона:"))
# print(sum(range(start, finish + 1)))
#
# import math
# start = int(input("Число:"))
# result = math.factorial(start)
# print(result)

# start = int(input("длинна:"))
# for i in range(start):
#     print("*", end="")
#

# num = int(input("Число:"))
# num2 = input("Символ:")
#
# print(num * num2)


# number = int(input("Введите число для таблицы умножения: "))
# print(f"Таблица умножения для числа {number}:")
# for i in range(1, 11):
#     result = number * i
#     print(f"{number} x {i} = {result}")

# print("Доступные валюты:")
# print("1. USD (Доллар)")
# print("2. EUR (Евро)")
# print("3. RUB (Рубль)")
#
#
# amount = float(input("Введите сумму: "))
#
#
# from_currency_index = int(input("Выберите валюту из которой конвертируете (1-3): ")) - 1
# to_currency_index = int(input("Выберите валюту в которую конвертируете (1-3): ")) - 1
#
#
# currencies = ['USD', 'EUR', 'RUB']
# from_currency = currencies[from_currency_index]  # Валюта, из которой конвертируем
# to_currency = currencies[to_currency_index]      # Валюта, в которую конвертируем
#
#
# if from_currency == 'USD':
#     if to_currency == 'EUR':
#         converted_amount = amount * 0.85
#     elif to_currency == 'RUB':
#         converted_amount = amount * 75.0
#     else:
#         converted_amount = amount  # USD to USD
#
# elif from_currency == 'EUR':
#     if to_currency == 'USD':
#         converted_amount = amount / 0.85
#     elif to_currency == 'RUB':
#         converted_amount = amount * (75.0 / 0.85)
#     else:
#         converted_amount = amount  # EUR to EUR
#
# elif from_currency == 'RUB':
#     if to_currency == 'USD':
#         converted_amount = amount / 75.0
#     elif to_currency == 'EUR':
#         converted_amount = amount * (0.85 / 75.0)
#     else:
#         converted_amount = amount  # RUB to RUB
#
#
# print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")


start = input("Вы сегодня поели?")

if start := "да":
    print("Отлично")
else:
    input("Тогда приготовим ")

