print('Bem-vindo ao aluguel de imoveis!')
print('Por favor, selecione o periodo você deseja alugar:')
print('A-curto 7 á 10 dias')
print('B-medio 12 á 18 dias')
print('C-longo 23 á 30 dias')
selecao = input("selecione a opção desejada: ")
a = 1900
b = 2600
c = 3400
if selecao == "A" or selecao == "a":
    print('valor do periodo curto, é de R${},'.format(a))
if selecao == "B" or selecao == "b":
    print('valor do periodo médio é de, R${}'.format(b))
if selecao == "C" or selecao == "c":
    print('valor periodo longo é de, R${}'.format(c))

    print('periodo curto selecionado, escolha a categoria do imovel que deseja alugar: ')
    print('1-imovel grande')
    print('2-imovel médio')
    print('3-imovel pequeno')
if selecao == "B" or selecao == "b":
    print('periodo medio selecionado, escolha a categoria do imovel que deseja alugar: ')
    print('1-imovel grande')
    print('2-imovel médio')
    print('3-imovel pequeno')
if selecao == "c" or selecao == "c":
    print('periodo longo selecionado, escolha a categoria do imovel que deseja alugar: ')
    print('1-imovel grande')
    print('2-imovel médio')
    print('3-imovel pequeno')

