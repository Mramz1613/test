"""
Фабричный метод  - позволяет создавать объект
через общий интерфейс а родительском классе,
позволяя дочерним классом изменять тип создаваемых обЪектов
"""
#для создания абстрактного класса

from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self)-> str:
        product = self.factory_method()
        result = f"Создатель: Код этого создателя работает с {product.operation()}"
        return result

class Product(ABC):
    @abstractmethod
    def operation(self)-> str:
        pass

class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()



class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Результат конкретного создателя1"

class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Результат конкретного создателя2"


def client_code(creator: Creator) -> None:

    print(f"Клиент: Я не знаю класс создателя,но он работает.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("Приложение: Запуск с ConcreteCreatorA")
    client_code(ConcreteCreatorA())
    print("\n")

    print("Приложение: Запуск с ConcreteCreatorB")
    client_code(ConcreteCreatorB())