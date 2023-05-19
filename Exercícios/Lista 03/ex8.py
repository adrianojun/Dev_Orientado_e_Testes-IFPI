"""8. Faça uma função que recebe um valor inteiro e verifica se o valor é positivo
ou negativo. A função deve retornar um valor booleano."""

def positivo_negativo(n):
    if type(n) != int:
        return Exception
    if n > 0:
        return True
    if n < 0:
        return False
    else:
        return Exception

assert positivo_negativo(-1) == False
assert positivo_negativo(1) == True
assert positivo_negativo(0) == Exception
assert positivo_negativo(0.1) == Exception
assert positivo_negativo("*") == Exception
print("Testes ok")