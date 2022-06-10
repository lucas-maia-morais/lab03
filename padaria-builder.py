from abc import ABC, abstractmethod

class Padaria():
    def __init__(self, builder):
        self.builder = builder

    def bake(self):
        return self.builder.bake()

class Bolo():
    def __init__(self, recheio, tipo):
        self.recheio = recheio
        self.tipo = tipo

class builder(ABC):
    @abstractmethod
    def bake(self):
        pass
    
    @abstractmethod
    def setSabor(self):
        pass

    @abstractmethod
    def setTipo(self):
        pass



class BoloBuilder(builder):
    def __init__(self, sabor, tipo):
        self.sabor = sabor
        self.tipo = tipo
    
    def setSabor(self, sabor):
        self.sabor = sabor

    def setTipo(self, tipo):
        self.tipo = tipo
    
    def bake(self):
        return Bolo(self.sabor, self.tipo)
    
