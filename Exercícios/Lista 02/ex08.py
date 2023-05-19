"""8) Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
ocorreu a letra ‘A’.
OBS: Fazer crítica na entrada do caractere para aceitar somente letras."""

lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J' 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ] 

testar = (str(input('Digite o número a ser verificado: ')))
repetir = lista.count(testar)

print(f' A letra {testar} repete {repetir} vezes na lista')

