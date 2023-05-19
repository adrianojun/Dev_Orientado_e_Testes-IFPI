# Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos
# no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma.

def soma(n1, n2):
    s = 0    
    for i in range(n1, n2 + 1):
        s += i
    return s 

while True:
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um número: '))

        if num1 < num2:
            print(f'A soma dos número é {soma(num1, num2)}')
            
        else:
            print('O primeiro número não pode ser maior do que o segundo.')

    except:
        print('Erro! Digite novamente!!')
        
    

