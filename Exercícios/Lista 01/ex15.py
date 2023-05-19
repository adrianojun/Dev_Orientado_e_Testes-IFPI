# 15) Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)

def soma(n):
    s = 0
    for t in range(1, n + 1):
        numerador = t ** 2 + 1
        denominador = t + 3
        s += numerador / denominador 
    return s 
while True:
    try:
        N = int (input("\nDigite a quantidade de termos: "))
        if N < 0: 
            print("Valor negativo. Digite novamente.")
        else:
            print("A soma é %2.2f" % soma(N))
            break
    except:
        print("Valor inválido. Digite novamente!")