# 13) Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.
def soma(s):
    s = 0
    for t in range(1, n + 1):
        numerador = 1
        denominador =  t
        s += numerador / denominador 
    return s 

while True:
    try:
        n = int (input("\nDigite a quantidade de termos: "))
        if n < 0: 
            print("Valor negativo. Digite novamente.")
        else:
            print("A soma é %2.2f" % soma(n))
            break
    except:
        print("Valor inválido. Digite novamente!")


