# class Decimal:
#     count_dec = 0
#     def __init__(self,numerator:int,denominator:int,chel:int):
#         self.numerator = numerator
#         self.denominator = denominator
#         self.chel = chel
#         while self.denominator == 0:
#             self.denominator = int(input("Знаменатель не можеть быть равен 0"))
#         print("Создана дробь")
#         Decimal.count_dec +=1
#
#     def nod(self)->int:
#         numer = abs(self.numerator)
#         den = abs(self.denominator)
#         while numer != 0 and den != 0:
#             if numer > den:
#                 numer = numer % den
#             else:
#                 den = den % numer
#         return den + numer
#
#     def display(self)->None:
#         print(f"{self.chel} целых {self.numerator}/{self.denominator}")
#
#     def getNum(self)->int:
#         return self.numerator
#
#     def getDen(self)->int:
#         return self.denominator
#
#     def sum(self,numObj)-> "Decimal":
#         if self.denominator == numObj.denominator:
#             self.numerator += numObj.numerator
#             self.sokrash()
#             self.cel_chast()
#             return Decimal(self.numerator,self.denominator,self.chel)
#         else:
#             self.numerator = self.numerator*numObj.denominator+numObj.numerator*self.denominator
#             self.denominator = self.denominator*numObj.denominator
#             self.sokrash()
#             self.cel_chast()
#             return Decimal(self.numerator,self.denominator,self.chel)
#
#     def sub(self,numObj)->"Decimal":
#         if self.denominator == numObj.denominator:
#             self.numerator -= numObj.numerator
#             return Decimal(self.numerator,self.denominator,self.chel)
#         else:
#             self.numerator = self.numerator*numObj.denominator-numObj.numerator*self.denominator
#             self.denominator = self.denominator*numObj.denominator
#             self.sokrash()
#             self.cel_chast()
#             return Decimal(self.numerator,self.denominator,self.chel)
#
#     def mutlti(self,numObj)->"Decimal":
#         self.numerator *= numObj.numerator
#         self.denominator *= numObj.denominator
#         self.sokrash()
#         self.cel_chast()
#         return Decimal(self.numerator,self.denominator,self.chel)
#     def dev(self,numObj)->"Decimal":
#         self.numerator *= numObj.denominator
#         self.denominator *= numObj.numerator
#         self.sokrash()
#         self.cel_chast()
#         return Decimal(self.numerator,self.denominator,self.chel)
#
#     def sokrash(self):
#         delit = self.nod()
#         self.numerator /= delit
#         self.denominator /= delit
#         self.numerator = int(self.numerator)
#         self.denominator = int(self.denominator)
#         return self.numerator,self.denominator
#
#     def cel_chast(self):
#         if abs(self.numerator) < abs(self.denominator):
#             return self.numerator,self.denominator,self.chel
#         else:
#             self.chel = abs(self.numerator)// abs(self.denominator)
#             self.numerator = abs(self.numerator) % abs(self.denominator)
#             return self.numerator,self.denominator,self.chel
#
#     @staticmethod
#     def get_count():
#         print(f"Количество дробей на данный момент {Decimal.count_dec}")
#         return Decimal.count_dec
#
# dec = Decimal(3,4,0)
# dec2 = Decimal(1,4,0)
# dec3 = dec2.sum(dec)
# dec.display()
# dec3.display()
# Decimal.get_count()
class Money:
    one_dollar = 79
    one_euro = 89

    def __init__(self,chel:int,kopeiki:int):
        self.chel = chel
        self.kopeiki = kopeiki
        if self.kopeiki >= 100:
            self.chel += self.kopeiki // 100
            self.kopeiki = self.kopeiki % 100

    def set_chel(self):
        self.chel = int(input("Введите целое кол-во рублей/долларов/евро"))

    def set_kopeiki(self):
        self.kopeiki = int(input("Введите копейки/центы/евроценты"))

    def display(self):
        print(f"{self.chel} и {self.kopeiki}")

    def convert_dol_to_rub(self):
        rub = (self.chel* Money.one_dollar)
        kop = self.kopeiki * Money.one_dollar
        if kop >= 100:
            rub += kop // 100
            kop = kop % 100
        print(f"Это будет {rub} рублей и {int(kop)} копеек")

    def convert_euro_to_rub(self):
        rub = self.chel* Money.one_euro
        kop = self.kopeiki * Money.one_euro
        if kop >= 100:
            rub += kop // 100
            kop = kop % 100
        print(f"Это будет {rub} рублей и {int(kop)} копеек")

    def convert_rub_to_dollar(self):
        rub = self.chel/ Money.one_dollar
        kop = rub%1*100
        if kop >= 100:
            rub += kop // 100
            kop = kop % 100

        print(f"Это будет {int(rub)} долларов и {int(kop)} центов")

    def convert_rub_to_euro(self):
        rub = self.chel/ Money.one_euro
        kop = rub%1*100
        if kop >= 100:
            rub += kop // 100
            kop = kop % 100

        print(f"Это будет {int(rub)} евро и {int(kop)} евро-центов")

if __name__ == "__main__":
    while True:
        user_in = input("Введите валюту(Р/Д/Е) Для выхода введите 0 ")
        match user_in:
            case "Р": user_val = Money(int(input("Введите рубли")),int(input("Введите копейки")))
            case "Д": user_val = Money(int(input("Введите доллары")),int(input("Введите центы")))
            case "Е": user_val = Money(int(input("Введите евро")),int(input("Введите евро-центы")))
            case "0":quit()
            case _: print("Ошибка")
        while True:
            user_in2 = input("Что во что переводить?(РВД,РВЕ,ЕВР,ДВР)")
            match user_in2:
                case "РВД": user_val.convert_rub_to_dollar()
                case "РВЕ": user_val.convert_rub_to_euro()
                case "ЕВР": user_val.convert_euro_to_rub()
                case "ДВР": user_val.convert_dol_to_rub()
                case "0":quit()
                case _:print("Ошибка")
