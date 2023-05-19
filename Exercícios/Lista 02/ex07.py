"""7) Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um outro valor dado pertence ou não à lista."""


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
verificar = (int(input('Digite o número a ser verificado: ')))

if verificar not in lista:
    print(f'O número {verificar} não está contido na lista.')

else:
    print(f'O número {verificar} está contido na lista.')