# 6) Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). 

#Faça um procedimento
# que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
# - Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
# - Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
# - Se o número de lados for igual a 5, escrever PENTÁGONO.
# Observação: Considere que o usuário só informará os valores 3, 4 ou 5.

def lados(lado, comprimento):
    if lado == 3:
        perimetro = comprimento * 3
        print('TRIÃNGULO com perímetro igual á ', perimetro)
    if lado == 4:
        area = comprimento * comprimento
        print('QUADRADO, com área igual à ', area)
    else: 
        print('PENTÁGONO')


l = int(input('Digite o número de lados do perímetro: '))
c = float(input('Digite o comprimento do lado do polígono: '))    
print(lados(l,c)) 
while l < 3 or l > 5:
        l = int(input('Digite o número de lados do perímetro: '))
        c = float(input('Digite o comprimento do lado do polígono: '))

        
         