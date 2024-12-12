class Book:
    def __init__(self,name:str, year_of_write:int, izdatel:str, genra:str, author:str,price:int):
        self.name = name
        self.year = year_of_write
        self.izdatel = izdatel
        self.genra = genra
        self.author = author
        self.price = price

    def setName(self)-> None:
        self.name = input("Введите название книги")

    def setYear(self)-> None:
        self.year = int(input("Введите год выпуска"))

    def setIzdatel(self)-> None:
        self.izdatel = input("Введите издателя")

    def setGenra(self)-> None:
        self.genra = input("Введите жанр")

    def setAuthor(self)-> None:
        self.author = input("Введите автора")

    def setPrice(self)-> None:
        self.price = int(input("Введите цену"))


    def getName(self)-> str:
        return self.name

    def getYear(self)-> int:
        return self.year

    def getIzdatel(self)-> str:
        return self.izdatel

    def getGenra(self)-> str:
        return self.genra

    def getAuthor(self)-> str:
        return self.author

    def getPrice(self)-> int:
        return self.price
    def display(self):
        print(self.name, self.year, self.izdatel, self.genra, self.author, self.price)

objBook = Book("Зов Клулху", 1980, "ООО мимо кассы", "Хоррор", "Лавкравт", 800)
objBook.display()
objBook.setName()
objBook.setYear()
objBook.setPrice()
objBook.setGenra()
objBook.setAuthor()
objBook.setIzdatel()
objBook.display()