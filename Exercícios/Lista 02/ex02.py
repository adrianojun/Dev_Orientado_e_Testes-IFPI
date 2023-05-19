"""2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
de números negativos e a soma dos números positivos dessa lista."""

from random import *
max_lista = 10
l = list(range(max_lista))
quant_neg = 0; soma_pos = 0.0
for i in range (max_lista):
    l[i] = round(uniform(-100,100),2)
    if l[i] < 0:
        quant_neg += 1
    else:
        soma_pos += l[i]
       
print("\nLista L: ", l)
print("\nQuantidade de números negativos: %d" % quant_neg)
print("\nSoma dos números positivos: %.3f" % soma_pos)