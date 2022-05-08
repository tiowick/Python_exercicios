preço = float(input('qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('o produto que custava {:.2f}R$, na promoção com desconto de 5%, vai custar {:.2f}.'.format(preço,novo))


