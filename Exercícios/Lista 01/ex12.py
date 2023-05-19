# 12) Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.

def soma(n):
    s = 0
    for t in range(1, n + 1):
        soma = t
        
        s += soma
    return s 

while True:
    try:
        n = int (input("\nDigite a quantidade de termos: "))
        if n < 0: 
            print("Valor negativo. Digite novamente.")
        else:
            print("A soma é" % soma(n))
            break
    except:
        print("Valor inválido. Digite novamente!")