"""
Dada uma lista de números inteiros, use uma função lambda em conjunto com reduce() para calcular
o produto de todos os números na lista.
Instruções:

    Importe a função reduce do módulo functools.

    Crie uma lista de números inteiros.
    Use a função reduce() em conjunto com uma função lambda para calcular o produto de todos os
    números na lista.

    Imprima o resultado.

numeros = [2, 3, 4, 5]

"""

from functools import reduce

numeros = [2, 3, 4, 5]

calculo_produtos = reduce(lambda soma, numeros: soma * numeros, numeros)

print(calculo_produtos)
