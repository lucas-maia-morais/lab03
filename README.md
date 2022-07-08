# lab03

## Abstract Factory Padaria

### Identificação das Classes
Vamos implementar a abstract Factory da padaria, inicialmente identifica-se a matriz de tipos de produtos versus variantes do produto. Neste caso assumisse que os produtos sãos os tipos de bolo, e a variante são os sabores, como resultado temos o nome do bolo que representa o bolo gerado:

<center>

| Sabores   |     Anivesário    |       Casamento      |         Informal       |
| :-------: | :---------------: | :------------------: | :--------------------: |
| Chocolate | Choco de Niver    | Gateau au chocolat   | bento cake de choco    |
| Mandioca  | Mandioca de Niver | Gateau au Manioc     | bento cake de mandioca |
| Cenoura   | Cenoura de Niver  | Gateau aux Carrottes | bento cake de cenoura  |

</center>

### Diagrama de classes
O diagrama de classes para o sistema da padaria está descrito abaixo
![Alt text](./padaria-factory.svg)
<!-- <img src="./padaria-factory.drawio.svg"> -->

### Exemplo de caso
Para uma main descrita abaixo:

```
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
```

Temos o output esperado a seguir:

``` 
Bolos de Aniversário
---------------------------------------
o Bolo Cholate
Parabéns por mais um ano de vida com seu Choco de Niver
Niver de Choco, que Delicia!

o Bolo de Mandioca
Parabéns por mais um ano de vida com seu Cenoura de Niver
Cenoura de Niver, para quem gosta de clássicos!

o Bolo de Cenoura
Parabéns por mais um ano de vida com seu Cenoura de Niver
Cenoura de Niver, para quem gosta de clássicos!


Bolos de Casamento
---------------------------------------
o Bolo Cholate
Felicitações pelo casamento, que seja tão bom quanto um Gateau au Chocolat!
Refinado e elegante, Gateau au Chocolat!

o Bolo de Mandioca
Felicitações pelo casamento, que seja tão bom quanto um Gateau aux Carrottes!
Tradicional e Inesperado, Gateau aux Carrottes!

o Bolo de Cenoura
Felicitações pelo casamento, que seja tão bom quanto um Gateau aux Carrottes!
Tradicional e Inesperado, Gateau aux Carrottes!


Bolos Informais
---------------------------------------
o Bolo Cholate
Refinado e elegante, Gateau au Chocolat!

o Bolo de Mandioca
Tradicional e Inesperado, Gateau aux Carrottes!

o Bolo de Cenoura
Tradicional e Inesperado, Gateau aux Carrottes!
```

## Builder Padaria

### Identificação das classes

No caso da implementação utilizando builder seria trivial construir um único builder e salvar o tipo de bolo e o recheio utilizando o diretor, porém para fazer mais sentido o uso de classes vamos supor que criar diferentes tipos bolo tenha procedimentos muito diferentes e faremos um procedimento no diretor para cada tipo, e a os recheios do bolo ficaram sendo feito pelo builder:

Procedimentos:
 - bakeAniversario
 - bakeCasamento
 - bakeInformal

Builder:
 - bakeChocolate
 - bakeMandioca
 - bakeCenoura

### Diagrama de classes
O diagrama de classes para o sistema da padaria usando o builde imaginado está descrito abaixo
![Alt text](./padaria-builder.svg)
<!-- <img src="./padaria-builder.drawio.svg">
 -->

### Exemplo de caso
Para uma main descrita abaixo que funciona como cliente:

```
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
```

Temos o output esperado a seguir:

```
Bolos de Chocolate
=============================
Bolo de chocolate do tipo Aniversário com Vela
Bolo de chocolate do tipo Casamento com Boneco
Bolo de chocolate do tipo Informal com 


Bolos de Mandioca
=============================
Bolo de Mandioca do tipo Aniversário com Vela
Bolo de Mandioca do tipo Casamento com Boneco
<property object at 0x7f4d8b244cc0>


Bolos de Cenoura
=============================
Bolo de Cenoura do tipo Aniversário com Vela
Bolo de Cenoura do tipo Casamento com Boneco
Bolo de Cenoura do tipo Informal com 

```