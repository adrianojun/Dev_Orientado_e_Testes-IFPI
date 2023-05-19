# 14) Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.

# S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!

def soma(n):
    s = 0
    f = 1
    for t in range(1, n + 1):
        f *=  t
        s += 1 / f 
    return s 

while True:
    try:
        n = int (input("\nDigite a quantidade de termos: "))
        if n < 0: 
            print("Valor negativo. Digite novamente.")
        else:
            print("O valor é %2.2f" % soma(n))
            break
    except:
        print("Valor inválido. Digite novamente!")
