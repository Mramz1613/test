'''
Паттерн фабричный метод - позволяет создавать объект через общий интерфейс в родительском классе, позволяя дочерним
классам изменять тип создаваемых объектов
'''

# для создания абстрактного класса
from abc import ABC, abstractmethod


class Creator(ABC):  # В классе создатель реализован фабричный метод, который возвращает
    # объект класса продукт
    @abstractmethod
    def createProduct(self):
        pass

    # Основная обязанность Создателя(Creator) не заключается в создании продуктов, он обычно
    # содержит некоторую бизнес-логику которая основана на обьектах продуктов возвращаемых
    # фабричным методом. Дочерние классы могут менять бизнес-логику, переопределяя фабричный
    # метод и возвращать из него другой тип продукта
    # @abstractmethod
    def someOperation(self):
        product = self.createProduct()
        result = f"Создатель: Код того же создателя только что отработал с {product.operation()} "
        return result


class Product(ABC):
    '''
    Интрефейс продукта объявляет операции, которые должны выполнить конкретные продукты
    '''

    @abstractmethod
    def operation(self):
        pass


class ConcreateCreator1(Creator):
    '''
    Создатель может оставаться независимым от конкретных
    классов продуктов
    '''

    def createProduct(self) -> Product:
        return ConcreateProduct1()


class ConcreateProduct1(Product):
    # переопределяем ф-ию родительского класса
    def operation(self):
        return "Результат класса ConcreateProduct1"


# клиенткский код работает с экземпляром конкретного создателя, через его базовый интерфейс.
# пока клиент продолжает работать с создателем через базовый интерфейс, вы можете передать ему
# любой дочерний класс создателя
def client_code(creator : Creator):
    print(f"Клиент: Я не знаю о классе создателя, но он будет работать {creator.someOperation()}")


print("Работает ConcreateCreator1")
# в функцию клиентский код передаем объект ConcreateCreator1()
client_code(ConcreateCreator1())