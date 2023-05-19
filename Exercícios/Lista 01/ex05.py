# 5) Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
# 1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e
# que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
# - para homens : (72.7 * h) – 58
# - para mulheres : (62.1 * h) – 44.7
# Observação: Altura = h (na fórmula acima).

def peso_ideal(s):
    if s == 1:
        return (62.1 * h) - 44.7
    else:
        return (72.7 * h) - 58

while True:
    try:
        h = float(input("Digite sua altura em metros: "))
        sexo = int(input("Digite 1 para sexo feminino ou 2 para sexo masculino: "))
        if (sexo == 1 or sexo == 2):
            print("Seu peso ideal é ", peso_ideal(sexo))
            break
        else:
            print('Sexo inválido, digite novamente!')
    except:
        print('Erro, digite novamente: ')