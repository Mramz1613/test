class Num:
    def __init__(self,num:int):
        self.num = num

    def sum(self,secObj):
        return self.num.__add__(secObj.num)

    def sub(self,secObj):
        return self.num.__sub__(secObj.num)

    def mult(self,secObj):
        return self.num.__mul__(secObj.num)

    def dev(self,secObj):
        if secObj == 0:
            return None
        return self.num.__truediv__(secObj.num)



num1 = Num(9)
num2 = Num(10)
print(num1.sum(num2))
print(num1.mult(num2))

class Lib:
    def __init__(self,name,adres,quan:int):
        self.name = name
        self.adres = adres
        self.quan = quan

    def display(self):
        print(f"{self.name=},{self.adres=},{self.adres=}")

    def add(self,obj:int):
        self.quan.__add__(obj)
