salario = float(input('qual o salário do funcionário? R$'))
if salario <= 1200:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('quem ganhava R${:.2f}, passa a ganhar R${:.2f}'.format(salario,novo))
