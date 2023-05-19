"""6) Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um
programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba
também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos
e quantos faturamentos estão abaixo da média."""

def gerar_listas():
    for i in range(1,max_lista+1):
        quantidade = int(input("Digite a quantidade do produto %d: " % i)) 
        q.append(quantidade)
        preco = float(input("Digite o preço do produto %d: " % i)) 
        p.append(preco)
        f.append(quantidade * preco)
        print("O faturamento do produto %d foi R$ %2.2f" % (i,quantidade * preco))

def calcular_faturamento():
    fat_total = 0
    for i in range(max_lista):
        fat_total = fat_total + f[i]
    print("O faturamento total foi R$ %2.2f" % (fat_total))
    media = fat_total / len(f)
    print("A média de faturamentos foi de %2.2f" % (media))
    quant_menor = 0
    for i in range(max_lista):
        if f[i] < media:
            quant_menor += 1
    print("Quantidade de faturamentos menores que a média: %d" % (quant_menor))
    
max_lista = 3
p = []
q = []
f = []
gerar_listas()
calcular_faturamento()