""" 12. Faça uma função que recebe 2 valores inteiros por parâmetro e retorna-os
ordenados em ordem crescente."""

def ordena(x,y):
    if type(x) != int or type(y) != int:
        return Exception
    if x <= y:
        return x, y
    else: 
        return y, x
    
assert ordena('*', 10) == Exception
assert ordena(10, "*") == Exception
assert ordena(2.5, 10) == Exception
assert ordena(1, 1.0) == Exception
assert ordena(-1, 2) == (-1, 2)
assert ordena(20, 10) == (10, 20)

print("Testes OK!")