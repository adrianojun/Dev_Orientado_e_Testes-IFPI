# 10) Escreva um programa composto de uma função Max e o programa principal como segue:
# a) A função Max recebe como parâmetros de entrada dois números inteiros e retorna o maior. Se forem iguais retorna qualquer um
# deles;
# b) O programa principal lê 4 séries de 4 números a, b. Para cada série lida imprime o maior dos quatro números usando a função
# Max.

def max(a, b):
    if a > b:
        return a
    elif a == b:
        return a   
    else:
        return b
    
while True:
    try:
        for i in range (a1, a2):
            