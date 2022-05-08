from math import sin, cos, tan, radians
angulo = float(input('digite o ângulo que você deseja:'))
seno = sin(radians(angulo))
print('o ângulo de {}, tem o seno de {:.2f}'.format(angulo,seno))
cosseno = cos(radians(angulo))
print('o ângulo de {}, tem o cosseno de {:.2f}'.format(angulo,cosseno))
tangente = tan(radians(angulo))
print('o ângulo de {}, tem a tangente de {:.2f}'.format(angulo, tangente))

