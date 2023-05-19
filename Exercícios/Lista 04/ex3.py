"""3. Faça uma função que recebe por parâmetro um valor inteiro e positivo e
retorna o valor lógico Verdadeiro caso o valor seja primo e Falso em caso
contrário."""

def num_primo(n):
    if type(n) != int:
        return False
    if n <= 1:
            return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
assert num_primo(0) == False
assert num_primo(-1) == False
assert num_primo(1) == False
assert num_primo(3) == True
assert num_primo(5) == True
assert num_primo(3.4) == False
print("Todos os testes ok!")