""" 10. Faça uma função que recebe a média final de um aluno por parâmetro e
retorna o seu conceito, conforme a tabela abaixo:
   Nota       Conceito
de 0,0 a 4,9     D
de 5,0 a 6,9     C
de 7,0 a 8,9     B
de 9,0 a 10,0    A """ 

def nota(n):
    if type(n) != int or type(n) != float:
        return Exception
    if n < 0 or n > 10:
        return Exception
    if n >= 0 or n <= 4.9:
        return "D"
    if n >= 5 or n <= 6.9:
        return "C"
    if n >= 7 or n <= 8.9:
        return "B"
    if n >= 9 or n <= 10:
        return "A"
    


assert nota(-1) == Exception
#assert nota(0) == "D"
assert nota(5) == "C"
assert nota(7) == "B"
assert nota(9) == "A"
assert nota("*") == Exception
assert nota(11) == Exception
assert nota(10.1) == Exception
assert nota(-0.1) == Exception

