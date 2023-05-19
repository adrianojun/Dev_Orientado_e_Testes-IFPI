# 8) Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o
# caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um
# programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os
# números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.

def caractere():
    x = input("Deseja continuar (S - Sim ou N - Não)?? ").upper()
    while x != "S" and x != "N":
        x = input("\nCaractere inválido. Digite novamente: ").upper()
    return x

while True:
    try: 
        num = int(input("\nDigite um número: "))
        print("O cubo do número %d é %d" % (num, num**3))
        if caractere() == "N":
            break
    except:
        print("Número inválido. Digite novamente:")
    