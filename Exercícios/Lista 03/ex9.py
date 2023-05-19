"""Faça uma função que recebe um valor inteiro e verifica se o valor é par ou
ímpar. A função deve retornar um valor booleano."""


def par_impar(n):
    if type(n) != int or n <= 0:
        return Exception
    if n % 2 == 0:
        return True
    elif n % 2 != 0:
        return False
    
assert par_impar(2) == True    
assert par_impar(1) == False    
assert par_impar(0) == Exception
assert par_impar(-10) == Exception
assert par_impar("*") == Exception
assert par_impar(5.4) == Exception

print("Testes Ok!")