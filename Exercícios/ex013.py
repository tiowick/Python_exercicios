salário = float(input('Qual é o salário do funcionário?'))
novo = salário + (salário * 15 / 100)
print('o salário do funcionário é R${:.2f}, com 15% de aumento fica R${:.2f}.'.format(salário,novo))


