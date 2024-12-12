#Первое задание
# def add_bascekt():
#     bascekt_name = input("Введите имя игрока")
#     if bascekt_name in bascekt_base:
#         print("Этот игрок уже в базе")
#         return
#     heith = int(input("Рост"))
#     bascekt_base[bascekt_name] = heith
#     print("Игрок добавлена\n\n")
# def change_bascekt():
#     bascekt_name = input("Введите имя игрока")
#     if bascekt_name not in bascekt_base:
#         print("Такого игрока нет в базе")
#         return
#     qua = int(input("Введите рост игрока"))
#     bascekt_base[bascekt_name] = qua
#     print("Рост игрока изменен\n\n")
#
# def delete_bascekt():
#     bascekt_name = input("Введите имя игрока")
#     if bascekt_name not in bascekt_base:
#         print("Такого игрока нет")
#         return
#     bascekt_base.pop(bascekt_name)
#     print(f"Игрок {bascekt_name} удален \n\n")
#
# def show_bascekt():
#     for name,qua in bascekt_base.items():
#         print(f"Имя: {name} Рост: {qua}\n")
#
#
# if __name__ == "__main__":
#     bascekt_base = {}
#     while True:
#         print("1. Добавить игрока")
#         print("2. Изменить игрока")
#         print("3. Удалить игрокаа")
#         print("4. Показать игроков")
#         print("0. Выход")
#         user_choice = input("Ваш выбор: ")
#         match user_choice:
#             case "1": add_bascekt()
#             case "2": change_bascekt()
#             case "3": delete_bascekt()
#             case "4": show_bascekt()
#             case "0": quit()
#             case _: print("Неизвестная команда")
#Второе задание
# def add_word():
#     word = input("Введите слово на англ")
#     if word in slovar:
#         print("Это слово есть в словаре")
#         return
#     france = input("Введите перевод на французком")
#     slovar[word] = france
#     print("Слово добавлено\n\n")
# def change_word():
#     word = input("Введите слово для измениния")
#     if word not in slovar:
#         print("Такого слова нет в базе")
#         return
#     qua = input("Введите перевод")
#     slovar[word] = qua
#     print("Слово изменино\n\n")
#
# def delete_word():
#     word = input("Введите слово")
#     if word not in slovar:
#         print("Такого слова нет")
#         return
#     slovar.pop(word)
#     print(f"Слово {word} удалено \n\n")
#
# def show_word():
#     for name,qua in slovar.items():
#         print(f"Слово на англ: {name} Слово на французком: {qua}\n")
#
#
# if __name__ == "__main__":
#     slovar = {}
#     while True:
#         print("1. Добавить слово")
#         print("2. Изменить слово")
#         print("3. Удалить слово")
#         print("4. Показать словарь")
#         print("0. Выход")
#         user_choice = input("Ваш выбор: ")
#         match user_choice:
#             case "1": add_word()
#             case "2": change_word()
#             case "3": delete_word()
#             case "4": show_word()
#             case "0": quit()
#             case _: print("Неизвестная команда")
#Третье задание
def add_name():
    name = input("Имя сотрудника")
    if name in slovar:
        print("Это имя уже есть")
        return

    info = {"number": None,
            "email": None,
            "Должность": None,
            "Номер кабинет":None,
            "Skype": None
            }
    number = input("Введите номер")
    user_email = input("Введите email")
    doljnost = input("Введите олжность")
    cab_num = input("Введите номер кабинета")
    skype = input("Введите скайп")
    info["number"] = number
    info["email"] = user_email
    info["Должность"] = doljnost
    info["Номер кабинет"] = cab_num
    info["Skype"] = skype
    slovar[name] = info
    print("Информация добавлена\n\n")


def delete_word():
    name = input("Введите имя")
    if name not in slovar:
        print("Такого слова нет")
        return
    slovar.pop(name)
    print(f"Сотрудник {name} удалено \n\n")

def change_word():

    name = input("Введите имя для измениния")
    if name not in slovar:
        print("Такого слова нет в базе")
        return
    info = {"number": None,
            "email": None,
            "Должность": None,
            "Номер кабинет": None,
            "Skype": None
            }
    name = input("Введите имя")
    while True:
        print("1. Изменить номер")
        print("2. Изменить маил")
        print("3. Изменить должность")
        print("4. Изменить номер кабинета")
        print("5. Изменить скайп")
        print("0. Выход из меню")
        change_info = input("Выберите действие")
        match change_info:
            case "1":
                number = input("Введите номер")
                info["number"] = number
            case "2":
                    user_email = input("Введите email")
                    info["email"] = user_email
            case "3":
                    doljnost = input("Введите должность")
                    info["Должность"] = doljnost
            case "4":
                    skype = input("Введите скайп")

            case "5":
                    cab_num = input("Введите номер кабинета")

            case "0": break
            case _: print("Неверны")




        info["Номер кабинет"] = cab_num
        info["Skype"] = skype
        slovar[name] = info
    print("Информация добавлена\n\n")
    slovar[name] = info
    print("Слово изменино\n\n")
def show_word():
    for name,qua in slovar.items():
        print(f"Имя: {name} Информация: {qua}\n")


if __name__ == "__main__":
    slovar = {}
    while True:
        print("1. Добавить сотрудника")
        print("2. Изменить сотрудника")
        print("3. Удалить сотрудника")
        print("4. Показать базу")
        print("0. Выход")
        user_choice = input("Ваш выбор: ")
        match user_choice:
            case "1": add_name()
            case "2": change_word()
            case "3": delete_word()
            case "4": show_word()
            case "0": quit()
            case _: print("Неизвестная команда")