""" Faça uma função que recebe, por parâmetro, a hora de inicio e a hora de
término de um jogo, ambas subdivididas em 2 valores distintos: horas e minutos.
O procedimento deve retornar, também por parâmetro, a duração do jogo em
horas e minutos, considerando que o tempo máximo de duração de um jogo é
de 24 horas e que o jogo pode começar em um dia e terminar no outro."""

def duracao(hi, mi, hf, mf):
     if hi <= hf:
          minutos_totais = ()
    
assert duracao(17, 30, 20, 40) == (3, 10)
assert duracao(23, 30, 1,40) == (2, 10)
assert duracao(23, 59, 2,59) == (2, 0)
print ("Todos os testes ok!!")