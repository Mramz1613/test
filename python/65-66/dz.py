from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self,name,max_speed,price):
        self.name = name
        self.max_speed = max_speed
        self.price = price

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def show_info(self):
        pass

    @abstractmethod
    def sound(self):
        pass

class Car(Vehicle):
    def __init__(self, name, max_speed, price,color):
        super().__init__(name, max_speed, price)
        self.color = color
    def move(self,):
        print(f"{self.name} поехала с максимальной скоростью {self.max_speed} км/ч")

    def sound(self):
        print(f"*Звук мотора*")

    def show_info(self):
        print(f"{self.name=},{self.max_speed=},{self.price=},{self.color=}")

class Bus(Vehicle):
    def __init__(self, name, max_speed, price,size):
        super().__init__(name, max_speed, price)
        self.size = size


    def move(self):
        print(f"{self.name} поехала с максимальной скоростью {self.max_speed} км/ч")


    def sound(self):
        print(f"*Звук передачи за проезд*")

    def show_info(self):
        print(f"{self.name=},{self.max_speed=},{self.price=},{self.size=}")


class Bicycle(Vehicle):
    def __init__(self, name, max_speed, price,material):
        super().__init__(name, max_speed, price)
        self.material = material

    def move(self):
        print(f"{self.name} поехала с максимальной скоростью {self.max_speed} км/ч")

    def sound(self):
        print(f"*Звук кручения педалей*")

    def show_info(self):
        print(f"{self.name=},{self.max_speed=},{self.price=},{self.material=}")


BMW = Car("Беха",200,"12000$","Black")
BMW.sound()
BMW.move()
BMW.show_info()

Icarus = Bus("Икарус",100,"15000$","Big")
Icarus.sound()
Icarus.move()
Icarus.show_info()

BMX = Bicycle("Totem",20,"100$","Aluminum")
BMX.sound()
BMX.move()
BMX.show_info()

class Circle:
    def __init__(self,r:float):
        self.r = r

    def __eq__(self, other):
        if self.r == other.r:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.r > other.r:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.r < other.r:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.r >= other.r:
            return True
        else:
            return False

    def __le__(self, other):
        if self.r <= other.r:
            return True
        else:
            return False

    def __add__(self, other):
        return self.r + other.r

    def __sub__(self, other):
        return self.r - other.r

    def __iadd__(self, other):
        self.r = self.r + other.r
        return self.r

    def __isub__(self, other):
        self.r = self.r - other.r
        return self.r

C1 = Circle(10)
C2 = Circle(5)
C3 = Circle(1)
print(C1==C2)
print(C1>C2)
print(C1<C2)
print(C1>=C2)
print(C1<=C2)
print(C1+C2)
print(C1-C2)
C3 += C1
print(C3)
C3 -= C1
print(C3)

