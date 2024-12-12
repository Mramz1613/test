from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self,position:tuple,color:str):
        self.position = position
        self.color = color

    @abstractmethod
    def clone(self):
        pass

class Rectangle(Shape):
    def __init__(self, position: tuple, color: str,width:int,height:int):
        super().__init__(position, color)
        self.wigth = width
        self.height = height

    def clone(self):
        return Rectangle(self.position,self.color,self.wigth,self.height)

    def display(self):
        print(f"{self.position},{self.color},{self.wigth},{self.height}")

class Circle(Shape):
    def __init__(self, position: tuple, color: str,radius:float):
        super().__init__(position, color)
        self.radius = radius

    def clone(self):
        return Circle(self.position,self.color,self.radius)

    def display(self):
        print(f"Круг с параметрами: {self.position=},{self.color=},{self.radius=}")

shar = Circle((0,0),"Blue",3.4)
shar2 = shar.clone()
shar2.display()
shar.display()
