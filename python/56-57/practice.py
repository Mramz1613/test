"""
try
except - исключение
"""

# try:
#     num = int(input("Введите число"))
#     print(f"Введенное число {num}")
# except ValueError:
#     print(f"Ошибка")
# finally:
#     print(f"Блок try завершон")
# print("Завершение программы")

# try:
#     num2 = int(input("Введите делитель"))
#     num = 3 / num2
#     print(num)
# except ZeroDivisionError:
#     print("Делить на ноль нельзя")

# my_list = [1,2,3,4,True,False]
# try:
#     for i in range(len(my_list)+1):
#         print(my_list[i])
# except IndexError:
#     print("Индекс выше возможного")

def fun():
    a,b = map(int,input("Введите числа").split(" "))
    print(f"{a=} {b=}")
    c = a/b
    print(c)
    d = float(a)**b
    print(d)

try:
    fun()
except ZeroDivisionError:
    print("Делить на ноль нельзя")
except OverflowError:
    print("Память переполнена")
except ValueError:
    print("Не правильное значение")