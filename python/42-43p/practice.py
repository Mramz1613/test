# # my_list = ["Банан",1]
# # my_tuple = ("Банан", 1)
# # print(f"list {my_list}, size: {my_list.__sizeof__()}")
# # print(f"tuple {my_tuple}, size: {my_tuple.__sizeof__()}")
# #
# # my_list = ["Банан",1,12]
# # my_tuple = ("Банан", 1,12)
# # print(f"list {my_list}, size: {my_list.__sizeof__()}")
# # print(f"tuple {my_tuple}, size: {my_tuple.__sizeof__()}")
# #
# # my_list = ["Банан",1,12]
# # my_tuple = ("Банан", 1,12)
# # print(f"list {my_list}, size: {my_list.__sizeof__()}")
# # print(f"tuple {my_tuple}, size: {my_tuple.__sizeof__()}")
# #
# # my_list = ["Банан",1,12,12]
# # my_tuple = ("Банан", 1,12,12)
# # print(f"list {my_list}, size: {my_list.__sizeof__()}")
# # print(f"tuple {my_tuple}, size: {my_tuple.__sizeof__()}")
#
# # my_tuple = (1,2,2,2,3,4,5)
# # print(my_tuple.index(3)) #индекс певого совпадения
# # print(my_tuple.count(2)) #посчитать колво
# # if 2 in my_tuple:
# #     print(my_tuple.index(2))
#
# my_dict = {}
#
#
#
# human = {"name": "Vasya","age": 25, "gender": "AH-64"}
# print(human)
# print(human["gender"]) # вернуть значение по ключу
# if "name" in human:
#     print("name есть")
# print(human.get("age")) #вернуть по ключу(None если ключа нет)
# print(human.get("a", "Ключа нет")) #если ключ отсутствует  вернет "Ключа нет"
#
# print(human.pop("age")) #удалить пару по ключу, возвращает значение данного ключа
# print(human)
# print(human.popitem())
# print(human)
# human["heith"]= 150 #создание ключа значение
# print(human)
#
# human["heith"]= 160 #создание ключа значение
# print(human)
# print(human.keys()) # вернуть список ключей
#
# print(human)
# print(human.values()) # вернуть список значений
#
# print(human)
# print((human.items())) # вернет список кортежей ключ значение


# human = {"name": "Vasya",
#          "age": 25,
#          "gender": "AH-64",
#          "adress": {"city":"Kaliningrad","country": "Russia", "street": "Puskina"}}
#
#
# # print(human["adress"]["country"])
#
# for key in human: #перебор всех ключей
#     print(key)
#
# for key in human.values(): #перебор всех значений
#     print(key)
#
# for key in human.items(): #перебор всех пар
#     print(key)
#
# for key, value in human.items(): #перебор всех пар
#     print(f"key: {key}, value: {value}")
# #создать словарь из ключей, присвоить значение "student"
# test_dict = dict.fromkeys(["Vasya","Petya","Vanya"],"student")
# print(test_dict)
#
# print(test_dict.setdefault("Vasya")) #получить значение по ключу
# print(test_dict)
# print(test_dict.setdefault("Anna", "student")) #если ключа нет,создаст ключ
# print(test_dict)

# fruits = ("Apple","Banana-kiwi","kiwi","Pineapple-kiwi","kiwi","kiwi","Banana")
# print(fruits.count(input("Введите название фрукта которое хотите посчитать ").lower()))
# search = input("введите фрукт для поиска").lower()
# count = 0
#
# for i in fruits:
#     if search in i:
#         count += 1
# print(count)
# cars = ("bmw","opel","toyta","audi","audi","audi","audi","zaz")
# old_name = input("Ведиите страторе название ")
# new_name = input("Введите новое название ")
# cars = list(cars)
# for i in range(len(cars)):
#     if cars[i] == old_name:
#         cars[i] = new_name
# cars = tuple(cars)
# print(cars)

# my_nums = (1,22,333,1,123123)
# dict_nums = {}
# for i in my_nums:
#     dict_nums.setdefault(i,len(str(i)))
# print(dict_nums)

"""Надо написать программу для хранения инфы о футбалите
фамилия и голы
надо реализовать создание,хранение, добавления
"""
my_footballers = {}
def add_player():
    player_last = input("Фамилия игрока: ")
    if player_last in my_footballers:
        print("Такой игрок уже есть")
    goals = int(input("Количество голов"))
    my_footballers[player_last] = goals
def delete_player():
    print("Кого удалить")
def change_player():
    pass
def show_info():
    for player_last,goals in my_footballers.items():
        print(f"Имя игрока: {player_last}, значение голов: {goals}")

if __name__ == "__main__":
    my_footballers = {}
    while True:
        print("1. Добавить игрока")
        print("2. Удалить игрока")
        print("3. Изменить данные игрока игрока")
        print("4. Показать всех игроков")
        print("0. Выход")
        user_choice = input("Ваш выбор ")
        match user_choice:
            case "1": add_player()
            case "2": delete_player()
            case "3": change_player()
            case "4": show_info()
            case "0": quit()
            case _: print("Неизвестная команда")