"""4) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra."""


lista = []

for i in range(1, 10 + 1):
    n = int(input('Digite um número: '))
    lista.append(n)

maior_num = max(lista)
posicao = lista.index(maior_num)
print(f'O maior número é {max(lista)} e estar na posição {posicao} da lista')