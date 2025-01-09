import pymysql
import sql_queries

try:
    with pymysql.connect(host="localhost", port=3307,user="root",password="") as connection:
        print("Успешно подключенно")
        with connection.cursor() as cursor:
            try:
                cursor.execute("""USE libary""")
            except:
                sql_queries.create_db(cursor)
            while True:
                print("-. Выход")
                print("1. Создать БД")
                print("2. Добавить книгу")
                print("3. Добавить читателя")
                print("4. Дать читателю книгу")
                print("5. Получить информацию по книгам")
                print("6. Получить информацию по читателям")
                print("7. Получить всю информацию")
                print("8. Показать все книги определенного пользователя")
                print("9. Показать всех читателей определенной книги")
                user_input = input("Введите номер команды")
                match user_input:
                    case "1": sql_queries.create_db(cursor)
                    case "2": sql_queries.add_book(cursor,connection)
                    case "3": sql_queries.add_reader(cursor,connection)
                    case "4": sql_queries.give_book_to_reader(cursor,connection)
                    case "5": sql_queries.get_books_info(cursor)
                    case "6": sql_queries.get_reader_info(cursor)
                    case "7": sql_queries.get_all_info(cursor)
                    case "8": sql_queries.get_books_of_user(cursor)
                    case "9": sql_queries.get_readers_of_book(cursor)
                    case "-": quit()
                    case _: print("Неизвестное значение")
except pymysql.Error as e:
    print(e)