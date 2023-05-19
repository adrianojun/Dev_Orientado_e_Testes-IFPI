# 4) Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação).

def aprovado_reprovado(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 6.0:
        return True
    else:
        return False
   
n1 = float(input("Digite a nota da primeira avaliação: "))
n2 = float(input("Digite a nota da segunda avaliação: "))
if aprovado_reprovado(n1, n2):
    print('PARABÉNS! Você foi aprovado!')
else:
    print('Reprovado.')
    