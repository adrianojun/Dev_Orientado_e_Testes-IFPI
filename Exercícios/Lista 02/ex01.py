""" 1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
 a) Mostre a quantidade de números pares;
 b) Grave uma lista somente com os números pares e mostre a lista;
 c) Mostre a quantidade de números ímpares;
 d) Grave uma lista somente com os números ímpares e mostre a lista.
"""
max_lista = 5
l = list(range(max_lista))

l_p = []
l_i = []
from random import *

def gravar_lista():
    for i in range (max_lista):

        l[i] = randint(-100,100)

def quant_p_i():
    cont_par = 0
    cont_impar = 0
    for i in range (max_lista):
        if l[i]% 2 == 0:
           cont_par += 1    
        else:
           cont_impar += 1
    print("\nQuantidade de números pares: %d." % cont_par)
    print("\nQuantidade de números ímpares: %d." % cont_impar)
#c)
def gerar_duas_listas():
    for i in range (max_lista):
        if l[i]% 2 == 0:
           l_p.append(l[i])    
        else:
           l_i.append(l[i])
#d)
def maior():
    maior = l[0]
    for i in range (1,max_lista):
        if l[i] > maior:
           maior = l[i]
    print("\nMaior número da lista l: %d." % maior)
    
gravar_lista()
quant_p_i()
gerar_duas_listas()
maior()
print("Lista L: ", l)
print("Pares (Lista l_p): ",l_p)
print("Impares (Lista l_i): ",l_i)