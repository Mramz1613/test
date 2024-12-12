# """
# адаптер
# """
# class Target:
#     def request(self):
#         return "Target: поведение класса по умолчанию"
#
# class Adapted:
#     def spec_request(self):
#         return "ассалк огомеуритпада еинедевоп цепс :detpadA"
#
# class Adapter(Target,Adapted):
#     def request(self):
#         return self.spec_request()[::-1]
#
# def client_code(target: Target):
#     print(target.request())
#
# print("Клиент: Я могу работать только с Target")
# target = Target()
# client_code(target)
# adaptee = Adapted()
# print("Клиент: Класс Adaptee непонятный интерфейс я его вижу но не понимаю")
# print(f"Adatee: {adaptee.spec_request()}")
# print(f"Клиент: Я могу работать только через класс адаптер")
# adapter = Adapter()
# client_code(adapter)
import math
class SquarePeg:
    def __init__(self,wight:int):
        self.wight = wight

    def getWight(self):
        return self.wight

class RoundPeg:
    def __init__(self,radius:int):
        self.radius = radius

    def getRad(self) -> int:
        return self.radius

class RoundHole:
    def __init__(self,radius:int):
        self.radius = radius

    def getRad(self)->int:
        return self.radius

    def fits(self,peg:RoundPeg):
        try:
            if self.radius >= peg.getRad():
                return "Лезет"
            else:
                return "Не лезет"
        except AttributeError:
            print("Уданного объект не имеет радиус")


class SquarePegAdapter(SquarePeg):
    def __init__(self,peg:SquarePeg):
        self.peg = peg

    def getRad(self):
        return self.peg.wight * math.sqrt(2)/2


h1= RoundHole(5)
h2=RoundHole(4)
c1= RoundPeg(6)
w1=SquarePeg(4)
ADW1 = SquarePegAdapter(w1)
print(h1.fits(c1))
print(h1.fits(w1))
print(h1.fits(ADW1))
