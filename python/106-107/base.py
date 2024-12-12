import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Users (
# id INTEGER PRIMARY KEY,
# username TEXT NOT NULL,
# email TEXT NOT NULL,
# age INTEGER
# )
# ''')
# data = [(1,"user1","user1@gmail.com"),
#     (2,"user2","user2@gmail.com")]
# cursor.execute("CREATE TABLE movie(title, year, score)")
# cursor.executemany("INSERT INTO movie VALUES(?,?,?)",data)
# Сохраняем изменения и закрываем соединение
data =[("9 апреля",19,24),
       ("Фрунзе",23,36),
       ("Литовский вал",12,24),
       ("Пионерская",29,36)]
connection.commit()
connection.close()
new_con = sqlite3.connect('my_database.db')
new_cur = new_con.cursor()
new_cur.execute('''
CREATE TABLE IF NOT EXISTS friends 
''')
new_cur.execute("""
INSERT INTO friends VALUES(?,?,?),data
""")
new_con.commit()
new_con.close()