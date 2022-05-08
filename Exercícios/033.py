n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
n3 = int(input('terceiro valor: '))
# verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n1
# verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('o menor valor digitado foi {}'.format(menor))
print('o maior valor digitado foi {}'.format(maior))
