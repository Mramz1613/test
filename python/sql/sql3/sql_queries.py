import pymysql


def connect_to_DB(cursor):
    cursor.execute("""USE libary""")
    print()
    print("Подключенно к базе данных!")
    print()

def create_db(cursor):
    query = """
    CREATE DATABASE IF NOT EXISTS libary
    """
    cursor.execute(query)
    cursor.execute("""USE libary""")

    query = """
    CREATE TABLE IF NOT EXISTS books(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    publish_year INT NOT NULL CHECK( publish_year > 0 )
    )
    """
    cursor.execute(query)

    query = """
    CREATE TABLE IF NOT EXISTS readers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
    )
    """
    cursor.execute(query)

    query = """
    CREATE TABLE IF NOT EXISTS books_and_readers(
    book_id INT NOT NULL,
    reader_id INT NOT NULL,
    PRIMARY KEY(book_id, reader_id),
    FOREIGN KEY(book_id) REFERENCES books(id) ON DELETE CASCADE,
    FOREIGN KEY(reader_id) REFERENCES readers(id) ON DELETE CASCADE
    )
    """
    cursor.execute(query)
    print("База данных создана")


def add_book(cursor,connection):
    print("Добавление книги")
    user_title = input("Введите название книги")
    user_author = input("Введите автора")
    user_year = int(input("Введите год выпуска"))
    while user_year <= 0:
        user_year = int(input("Год не может быть меньше или равен 0 введите снова"))

    query = """
    INSERT INTO books (title, author, publish_year) VALUES(%s,%s,%s)
    """
    cursor.execute(query,[user_title,user_author,user_year])
    connection.commit()
    print(f"Книга {user_title} добавлена \n\n\n")


def add_reader(cursor,connection):
    print("Добавление читателя")
    user_name = input("Введите имя читателя")
    user_email = input("Введите электронный адрес")

    query = """
        INSERT INTO readers (name, email) VALUES(%s,%s)
        """
    cursor.execute(query, [user_name, user_email])
    connection.commit()
    print(f"Читатель добавлен {user_name} добавлена \n\n\n")


def give_book_to_reader(cursor,connection):
    get_reader_info(cursor)
    reader_id = int(input("Введите id читателя: "))
    get_books_info(cursor)
    book_id = int(input("Введите id книги: "))
    query = """
    INSERT INTO books_and_readers (book_id,reader_id) VALUES(%s,%s)
    """
    cursor.execute(query,(book_id,reader_id))
    connection.commit()


def get_books_info(cursor):
    cursor.execute("""SELECT * FROM books""")
    for row in cursor:
        print(f"id: {row[0]}\ntitle: {row[1]}\nauthor: {row[2]}\nyear of publish: {row[3]}\n ")

def get_reader_info(cursor):
    cursor.execute("""SELECT * FROM readers""")
    for row in cursor:
        print(f"id: {row[0]}\nName: {row[1]}\nemail: {row[2]}\n ")


def get_all_info(cursor):
    query = """
    SELECT r.name, r.email, b.title,b.author,b.publish_year FROM books_and_readers br
    JOIN readers r ON br.reader_id = r.id
    JOIN books b ON br.book_id = b.id
    """
    cursor.execute(query)

    for row in cursor:
        print(f"Имя читателя:{row[0]}\nНазвание книги:{row[1]}\nАвтор книги:{row[2]}\nГод выпуска:{row[3]}\n")


def get_books_of_user(cursor):
    print("Показать список всех книг у определенного читателя")
    get_reader_info(cursor)
    reader_id = int(input("Выберите id читателя"))
    query = """
    SELECT r.name, b.title,b.author,b.publish_year FROM books_and_readers br
    JOIN readers r ON br.reader_id = r.id
    JOIN books b ON br.book_id = b.id
    WHERE r.id = %s
    """
    cursor.execute(query,reader_id)
    for row in cursor:
        print(*row)


def get_readers_of_book(cursor):
    get_books_info(cursor)
    book_id = int(input("Введите id книги"))
    query = """
    SELECT r.name FROM books_and_readers br
    JOIN readers r ON br.reader_id = r.id
    JOIN books b ON br.book_id = b.id
    WHERE b.id = %s
    """

    cursor.execute(query, book_id)
    for row in cursor:
        print(*row)
