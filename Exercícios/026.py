frase = str(input('digite uma frase: ')).upper().strip()
print('a letra a, aparece na posição {} na frase .'.format(frase.count('A')))
print('a primeira letra A, apareceu na posiçâo {} .'.format(frase.find('A')+1))
print('a ultima letra A, apareceu na posiçâo {} .'.format(frase.rfind('A')+1))

