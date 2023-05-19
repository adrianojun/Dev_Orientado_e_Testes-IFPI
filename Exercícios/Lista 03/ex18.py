def tabuada(n):
    if type(n) != int or n <= 0:
        return Exception
    lista = []
    for i in range (1, n+1):
        lista.append(i*n)
    return lista

assert tabuada(5) == [5,10,15,20,25]
assert tabuada(1) == [1]
assert tabuada(5.4) == Exception
assert tabuada(0) == Exception
assert tabuada(-1) == Exception
assert tabuada("*") ==  Exception
print("Testes Ok!")
