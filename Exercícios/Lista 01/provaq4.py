"""Faça um programa em python que mostre apenas os números pares da sequência de
fibonaci. f = 1,1,2,3,5,8,13,21,34,55, ......."""
def fibonacci(t):
    ant1 = 1
    ant2 = 1
    for i in range (3,t+1):
        valor = ant1 + ant2
        ant2 = ant1
        ant1 = valor
        if valor % 2 == 0:
            print(valor)
while True:
    try:
        # receber o último termo da sequência
        termo = int(input("\nDigite o número do último termo: "))
        if termo > 0:
            fibonacci(termo)
        else:
            print("O número informado deve ser maior que zero")
        break
    except:
        print("\nNúmero inválido. Digite novamente!")
    
