from abc import ABC, abstractmethod

class Padaria():
    def __init__(self, typeFactory):
        self.typeFactory = typeFactory

    def bakeAniversario(self):
        self.typeFactory.bakeAniversario()

    def bakeCasamento(self):
        self.typeFactory.bakeCasamento()
    
    def bakeInformal(self):
        self.typeFactory.bakeInformal() 

class Bolo():
    def __init__(self, recheio, tipo):
        self.recheio = recheio
        self.tipo = tipo
    

class AbstractTypeCakeFactory(ABC):
 
    @abstractmethod
    def bakeAniversario(self):
        pass

    @abstractmethod
    def bakeCasamento(self):
        pass
    
    @abstractmethod
    def bakeInformal(self):
        pass

class CenouraFactory(AbstractTypeCakeFactory):

    @abstractmethod
    def bakeAniversario(self):
        return Bolo("Cenoura", "Aniversario")

    @abstractmethod
    def bakeCasamento(self):
        return Bolo("Cenoura", "Casamento")
    
    @abstractmethod
    def bakeInformal(self):
        return Bolo("Cenoura", "Informal")

class ChocolateFactory(AbstractTypeCakeFactory):

    @abstractmethod
    def bakeAniversario(self):
        return Bolo("Chocolate", "Aniversario")

    @abstractmethod
    def bakeCasamento(self):
        return Bolo("Chocolate", "Casamento")
    
    @abstractmethod
    def bakeInformal(self):
        return Bolo("Chocolate", "Informal")


class MandiocaFactory(AbstractTypeCakeFactory):

    @abstractmethod
    def bakeAniversario(self):
        return Bolo("Mandioca", "Aniversario")

    @abstractmethod
    def bakeCasamento(self):
        return Bolo("Mandioca", "Casamento")
    
    @abstractmethod
    def bakeInformal(self):
        return Bolo("Mandioca", "Informal")