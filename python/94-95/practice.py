from abc import ABC,abstractmethod
class Divice(ABC):
    @abstractmethod
    def isEnable(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def getVolume(self):
        pass

    @abstractmethod
    def setVolume(self,volume):
        pass

    @abstractmethod
    def getChannel(self):
        pass

    @abstractmethod
    def setChannel(self,channel):
        pass

class Remote:
    def __init__(self,divice: Divice):
        self.divice = divice

class TV(Divice):
    def __init__(self,volume:int,channel:int,isEnable:bool):
