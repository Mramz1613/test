import pymysql
import sql_queries

try:
    with pymysql.connect(host="localhost",port=3307,user="root",password="") as connection:
        print("Успешно подключенно")
        with connection.cursor() as cursor:
            sql_queries.connect_to_cars_database(cursor)
            while True:
                print("0. Выход")
                print("1. Подключится к базе 'cars'")
                print("2. Создать базу данных")
                print("3. Добавить производителя машин")
                print("4. Добавить модель машин")
                print("5. Удалить модель машин")
                print("6. Обновить модель машин")
                print("7. Показать полную информацию о машинах")
                print("8. Показать полную информацию о машинах")
                user_input = int(input("Введите номер команды"))
                match user_input:
                    case 0: break
                    case 1: sql_queries.connect_to_cars_database(cursor)
                    case 2: sql_queries.create_database_and_table(cursor)
                    case 3: sql_queries.add_brand(cursor,connection)
                    case 4: sql_queries.add_model(cursor,connection)
                    case 5: sql_queries.delete_model(cursor,connection)
                    case 6: sql_queries.update_model(cursor,connection)
                    case 7: sql_queries.get_full_model_info(cursor)
                    case 8: sql_queries.get_brands_info(cursor)
                    case _: print("Неизвестная команда\n")
except pymysql.Error as e:
    print(e)