distancia = float(input('qual a distância da sua viagem? '))
print('você esta prestes a fazer uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('e o preço de sua passagem, vai ser {:.2f}' .format(preco))