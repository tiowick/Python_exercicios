from random import randint
from time import sleep
computador = randint(0,100) #faz o computador pensar
print('-=-' * 20)
print('vou pensar em um número entre 0 e 10, tente advinhar! ')
print('-=-' * 20)
print('PROCESSANDO...')
sleep(4)
jogador = int(input('em que número eu pensei? ')) #jogador tenta advinhar
if jogador == computador:
    print('PARABÉNS!, você conseguiu me vencer!')
else:
    print('GANHEI!, eu pensei no {}, e não no {} !'.format(computador,jogador))


