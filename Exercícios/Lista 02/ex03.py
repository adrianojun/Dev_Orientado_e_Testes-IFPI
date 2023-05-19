"""3) Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da
leitura."""

l = list(range(5))

from random import randint

for i in range (5):
    l[i] = randint(0,100)
#a)
"""print("Lista original.............: ", l)
for i in range(4,-1,-1): # imprimir na ordem inversa
     print(l[i])"""

print("Lista original.............: ", l)
print("Impressão na ordem inversa.: ", l[::-1])
print("Imprimir uma parte da lista: ", l[2:4])


l2 = list(range(5))

print("Lista original.............: ", l)
j = 0
for i in range(4,-1,-1):
     l2[j] = l[i]
     j += 1
print("\nLista l   : ", l)
print("\nLista l2 (inversa de l) : ", l2)