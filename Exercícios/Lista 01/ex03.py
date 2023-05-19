# 3) Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar
# o valor correspondente em graus Celsius.
# Fórmula: C = ((F-32)/9)*5

#PESQUISAR COMO FORMATAR UMA FUNÇÃO

def celsius(f):
    return ((f - 32) / 9) * 5

h = float(input("Digite a temperatura em graus fahrenheit: "))
print("A temperatura em graus celsius é: %.2f" % celsius(h))