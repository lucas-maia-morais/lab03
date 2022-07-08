from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

# Builder Abstrato
# -------------------------------------------------------

class Builder(ABC):
    
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def putVela(self) -> None:
        pass

    @abstractmethod
    def putBoneco(self) -> None:
        pass

    @abstractmethod
    def setTipo(self, tipo) -> None:
        pass

# Builder Concretos
# -------------------------------------------------------

class ChocolateBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Chocolate()
    
    @property
    def product(self) -> Chocolate:
        product = self._product
        self.reset()
        return product
    
    def putVela(self) -> None:
        self._product.add('Vela')

    def putBoneco(self) -> None:
        self._product.add('Boneco')

    def setTipo(self, tipo) -> None:
        self._product.setType(tipo)

class MandiocaBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Mandioca()
    
    @property
    def product(self) -> Mandioca:
        product = self._product
        self.reset()
        return product
    
    def putVela(self) -> None:
        self._product.add('Vela')

    def putBoneco(self) -> None:
        self._product.add('Boneco')

    def setTipo(self, tipo) -> None:
        self._product.setType(tipo)

class CenouraBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Cenoura()
    
    @property
    def product(self) -> Cenoura:
        product = self._product
        self.reset()
        return product
    
    def putVela(self) -> None:
        self._product.add('Vela')

    def putBoneco(self) -> None:
        self._product.add('Boneco')

    def setTipo(self, tipo) -> None:
        self._product.setType(tipo)

# Classes concretas
# -------------------------------------------------------
class Chocolate():
    def __init__(self) -> None:
        self.parts = []
        self.type = []
    
    def add(self, part: Any) -> None:
        self.parts.append(part)
    
    def setType(self, tipo):
        self.type = tipo
    
    def __str__(self) -> str:
        return f"Bolo de chocolate do tipo {self.type} com {', '.join(self.parts)}"

class Mandioca():
    def __init__(self) -> None:
        self.parts = []
        self.type = []
    
    def add(self, part: Any) -> None:
        self.parts.append(part)
    
    def setType(self, tipo):
        self.type = tipo
    
    def __str__(self) -> str:
        return f"Bolo de Mandioca do tipo {self.type} com {', '.join(self.parts)}"

class Cenoura():
    def __init__(self) -> None:
        self.parts = []
        self.type = []
    
    def add(self, part: Any) -> None:
        self.parts.append(part)
    
    def setType(self, tipo):
        self.type = tipo
    
    def __str__(self) -> str:
        return f"Bolo de Cenoura do tipo {self.type} com {', '.join(self.parts)}"


# Criar diretor
# -------------------------------------------------------
class Director:
    
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder:Builder) -> None:
        self._builder = builder
    
    def bakeAniversario(self) -> None:
        self._builder.setTipo("Aniversário")
        self._builder.putVela()
    
    def bakeCasamento(self) -> None:
        self._builder.setTipo("Casamento")
        self._builder.putBoneco()

    def bakeInformal(self) -> None:
        self._builder.setTipo("Informal")

# A main vai funcionar como Client
# -------------------------------------------------------
if __name__ == "__main__":

    director = Director()

## ========== Chocolate ===================================
    choco = ChocolateBuilder()
    print("Bolos de Chocolate")
    print("=============================")
    director.builder = choco

    director.bakeAniversario()
    print(str(choco.product))

    director.bakeCasamento()
    print(choco.product)

    director.bakeInformal()
    print(choco.product)
    print("\n")

## ========== Mandioca ===================================
    mandioca = MandiocaBuilder()
    print("Bolos de Mandioca")
    print("=============================")
    director.builder = mandioca

    director.bakeAniversario()
    print(mandioca.product)

    director.bakeCasamento()
    print(mandioca.product)

    director.bakeInformal()
    print(Builder.product)
    print("\n")

## ========== Cenoura ===================================
    cenoura = CenouraBuilder()
    print("Bolos de Cenoura")
    print("=============================")
    director.builder = cenoura

    director.bakeAniversario()
    print(cenoura.product)

    director.bakeCasamento()
    print(cenoura.product)

    director.bakeInformal()
    print(cenoura.product)
    print("\n")