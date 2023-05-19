""" Faça uma função que recebe a idade de um nadador por parâmetro e retorna
a categoria desse nadador de acordo com a tabela abaixo:
  Idade            Categoria
5 a 7 anos        Infantil A
8 a 10 anos       Infantil B
11-13 anos        Juvenil A
14-17 anos        Juvenil B
Maiores de 18 anos
(inclusive)

Adulto """

def idade(i):
    if (type(i)) != int: 
        return Exception
    
    if i < 5 or i > 120:
        return Exception
    
    if i >= 5 and i <= 7:
        return "Infantil A"
    
    elif i >= 8 and i <= 10:
        return "Infantil B"
    
    elif i >= 11 and i <= 13:
        return "Juvenil A"
    
    elif i >= 14 and i <= 17:
        return "Juvenil B"
    
    elif i >= 18:
        return "Adulto"
    
assert idade(5) ==  "Infantil A"
assert idade(7) ==  "Infantil A"
assert idade(8) ==  "Infantil B"
assert idade(10) == "Infantil B"
assert idade(11) == "Juvenil A"
assert idade(13) == "Juvenil A"
assert idade(14) == "Juvenil B"
assert idade(17) == "Juvenil B"
assert idade(18)== "Adulto"
assert idade(-1) == Exception
assert idade(150) == Exception
assert idade(3.25) == Exception
assert idade("") == Exception
print("Testes Ok!")
