"""3)	Um número é dito perfeito quando a soma dos seus divisores é igual
a ele próprio. Ex. 6 é um número perfeito pois 1 + 2 + 3 = 6.
Faça um programa em python que tenha uma função que recebe
um número e retorna se ele é ou não perfeito."""


def perfeito(n):
    soma = 0
    for j in range(1,n):
        if n % j == 0:
            soma += j
    if soma == n:
        return True
    else:
        return False
while True:
    try:
        numero = int(input("\nDigite um número: "))
        if perfeito(numero):
            print("O número %i é perfeito." % numero)
        else:
            print("O número %i não é perfeito." % numero)
        break
    except:
        print("\nNúmero inválido. Digite novamente!")