velocidade = float(input('qual a velocidade atual do carro?'))
if velocidade > 80:
    print('multado!, você excedeu o limite permitido que é 80km/h')
    multa = (velocidade-80) * 7
    print('você deve pagar uma multa de R${:.2f}'.format(multa))
print('tenha um bom dia! dirija com cuidado!')



