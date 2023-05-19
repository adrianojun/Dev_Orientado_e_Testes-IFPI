"""5) Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os
elementos deste em uma outra lista de 20 elementos."""

max_lista = 3
l1 = []
l2 = list(range(max_lista))

from random import randint
def gravar_listas():
     for i in range (max_lista):
          l1.append(randint(0,100))
          l2[i] = randint(0,100)


def intercalar():
     l3 = []
     for i in range(max_lista):
         l3.append(l1[i])
         l3.append(l2[i])
     return l3


def intercalar2():
     l3 = [0]*(2*max_lista)
     j = 0
     for i in range(max_lista):
         l3[j] = l1[i]
         j += 1
         l3[j] = l2[i]
         j += 1
     return l3

gravar_listas()
print("\nLista 1: ", l1)
print("\nLista 2: ", l2)
print("\nLista intercalada  : ", intercalar())
print("\nLista intercalada 2: ", intercalar2())