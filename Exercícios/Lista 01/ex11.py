# 11) Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.

def divisores(n):
    c = 0
    for i in range(1, n+1):
        if n % i == 0:
            c += 1
    return c

while True:
    try:
        num = int(input('Digite um número qualquer: '))
        if num != 0:
            print(f'O total de divisores de {num} é {divisores(num)}')
        else:
            print('O número não pode ser igual a 0')

    except:
        print('Valor Inválido, digite novamente!')
