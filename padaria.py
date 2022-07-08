from __future__ import annotations
from abc import ABC, abstractmethod

# Classe Padaria
class Padaria:

    def __init__(self, sabor):
        if   (sabor=='chocolate'):
            self.recheioFactory = ChocolateFactory()
        elif (sabor == 'mandioca'):
            self.recheioFactory = MandiocaFactory()
        else:
            self.recheioFactory = CenouraFactory()
    
    def getFactory(self):
        return self.recheioFactory

# ------------------------------------------------------------------------------------------
# Abstract Factory
class CakeFactory(ABC):
    
    @abstractmethod
    def bakeAniversario(self) -> Aniversario:
        pass

    @abstractmethod
    def bakeCasamento(self) -> Casamento:
        pass

    @abstractmethod
    def bakeInformal(self) -> Informal:
        pass

# ------------------------------------------------------------------------------------------
# Concrete Factories
class ChocolateFactory(CakeFactory):

    def bakeAniversario(self) -> Aniversario:
        return ChocoAniversario()

    def bakeCasamento(self) -> Casamento:
        return ChocoCasamento()

    def bakeInformal(self) -> Informal:
        return ChocoInformal()

class MandiocaFactory(CakeFactory):

    def bakeAniversario(self) -> Aniversario:
        return MandiocaAniversario()

    def bakeCasamento(self) -> Casamento:
        return MandiocaCasamento()

    def bakeInformal(self) -> Informal:
        return MandiocaInformal()

class CenouraFactory(CakeFactory):

    def bakeAniversario(self) -> Aniversario:
        return CenouraAniversario()

    def bakeCasamento(self) -> Casamento:
        return CenouraCasamento()

    def bakeInformal(self) -> Informal:
        return CenouraInformal()

# ------------------------------------------------------------------------------------------
# Abstract Products
class Aniversario(ABC):
    @abstractmethod
    def soprarVelas(self) -> None:
        pass

    @abstractmethod
    def comer(self) -> None:
        pass

class Casamento(ABC):
    @abstractmethod
    def cortarBolo(self) -> None:
        pass

    @abstractmethod
    def comer(self) -> None:
        pass

class Informal(ABC):
    @abstractmethod
    def comer(self) -> None:
        pass

# ------------------------------------------------------------------------------------------
# Concrete Products
class ChocoAniversario(Aniversario):

    def soprarVelas(self) -> None:
        print('Parabéns por mais um ano de vida com seu Choco de Niver')

    def comer(self) -> None:
        print('Niver de Choco, que Delicia!')

class MandiocaAniversario(Aniversario):

    def soprarVelas(self) -> None:
        print('Parabéns por mais um ano de vida com seu Mandioca de Niver')

    def comer(self) -> None:
        print('Mandioca de Niver, muito Bom!')

class CenouraAniversario(Aniversario):

    def soprarVelas(self) -> None:
        print('Parabéns por mais um ano de vida com seu Cenoura de Niver')

    def comer(self) -> None:
        print('Cenoura de Niver, para quem gosta de clássicos!')

class ChocoCasamento(Casamento):

    def cortarBolo(self) -> None:
        print('Felicitações pelo casamento, que seja tão bom quanto um Gateau au Chocolat!')

    def comer(self) -> None:
        print('Refinado e elegante, Gateau au Chocolat!')

class MandiocaCasamento(Casamento):

    def cortarBolo(self) -> None:
        print('Felicitações pelo casamento, que seja tão bom quanto um Gateau au Manioc!')

    def comer(self) -> None:
        print('Rústico e revolucionário, Gateau au Manioc!')

class CenouraCasamento(Casamento):

    def cortarBolo(self) -> None:
        print('Felicitações pelo casamento, que seja tão bom quanto um Gateau aux Carrottes!')

    def comer(self) -> None:
        print('Tradicional e Inesperado, Gateau aux Carrottes!')

class ChocoInformal(Informal):

    def comer(self) -> None:
        print('Bento cake de choco, o melhor dos melhores.')

class MandiocaInformal(Informal):

    def comer(self) -> None:
        print('Bento cake de mandioca, o melhor dos regionais.')

class CenouraInformal(Informal):

    def comer(self) -> None:
        print('Bento cake de mandioca, o melhor do café da tarde.')

if __name__ == '__main__':
    
    padariaChoco = Padaria('chocolate')
    padariaMadioca = Padaria('Mandioca')
    padariaCenoura = Padaria('Cenoura')

    ## Região dos bolos de aniversário
    print('Bolos de Aniversário')
    print('---------------------------------------')
    b1 = padariaChoco.getFactory().bakeAniversario()
    print('o Bolo Cholate')
    b1.soprarVelas()
    b1.comer()
    
    print('')
    b2 = padariaMadioca.getFactory().bakeAniversario()
    print('o Bolo de Mandioca')
    b2.soprarVelas()
    b2.comer()

    print('')
    b3 = padariaCenoura.getFactory().bakeAniversario()
    print('o Bolo de Cenoura')
    b3.soprarVelas()
    b3.comer()

    print('\n')
    ## Região dos bolos de aniversário
    print('Bolos de Casamento')
    print('---------------------------------------')
    b1 = padariaChoco.getFactory().bakeCasamento()
    print('o Bolo Cholate')
    b1.cortarBolo()
    b1.comer()
    
    print('')
    b2 = padariaMadioca.getFactory().bakeCasamento()
    print('o Bolo de Mandioca')
    b2.cortarBolo()
    b2.comer()

    print('')
    b3 = padariaCenoura.getFactory().bakeCasamento()
    print('o Bolo de Cenoura')
    b3.cortarBolo()
    b3.comer()

    print('\n')
    ## Região dos bolos de aniversário
    print('Bolos Informais')
    print('---------------------------------------')
    b1 = padariaChoco.getFactory().bakeCasamento()
    print('o Bolo Cholate')
    b1.comer()
    
    print('')
    b2 = padariaMadioca.getFactory().bakeCasamento()
    print('o Bolo de Mandioca')
    b2.comer()

    print('')
    b3 = padariaCenoura.getFactory().bakeCasamento()
    print('o Bolo de Cenoura')
    b3.comer()