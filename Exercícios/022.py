nome = str(input('digite seu nome completo:')).strip()
print('analisando seu nome...')
print('seu nome em maiusculo é {}'.format(nome.upper()))
print('seu nome em minusculo é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('seu primeiro nome é {} e tem {} letras'.format(separa[0],len(separa[0])))


