print("Mega Car")
login = input("Digite seu usuário \n")
senha = input("Digite sua senha: \n")
user_db = "Jeferson"
senha_db = "85475244"
if login == user_db and senha == senha_db:
    print("Usuário autenticado")
    print("Sistema de Locação de Veículos")
    print("Selecione uma opção:")
    print("1 - Cadastrar")
    print("2 - Aluguel")
    opcao = input("Digite opção desejada! ")
    if opcao == "1":
        print("Sistema de Cadastro!")
        print("Selecione um opcão:")
        print("1-Usuário")
        print("2-Cliente")
        print("3-Veículos")
        opc = input("Digite a opção desejada:")
        if opc == "1":
            print("Bem Vindo(a) ao seu perfil de usuário!")
            print("Selecione uma opção:")
            print("1-Configurações de conta")
            print("2-Carros já alugados")
            print("3-Lista de desejos")
            opc = input("Digite a opção desejada:")
            if opc == "1":
                print("1-Atualizar perfil")
                print("2-Cadastrar perfil")
                opc = input("Digite a opção desejada:")
                if opc == "1":
                    nome = input("Digite o seu nome")
                    sobrenome = input("Digite o seu sobrenome")
                    data = input("Preencha com sua data de nascimento")
                    cpf = input("Preencha com seu CPF")
                    cart = input("Preencha com CNH")
                    ender = input("Preencha com endereço")
                    email = input("Preencha com seu e-mail")
                    print("Perfil cadastrado com sucesso!")
                if opc == "2":
                    nome = input("Digite o seu nome")
                    sobrenome = input("Digite o seu sobrenome")
                    data = input("Preencha com sua data de nascimento")
                    cpf = input("Preencha com seu CPF")
                    cart = input("Preencha com CNH")
                    ender = input("Preencha com endereço")
                    email = input("Preencha com seu e-mail")
                    print("Perfil atualizado com sucesso!")

            if opc == "2":
                print("Carros alugados")
                print("Esses são os carros já alugados:")
                print("Carro 1")
                print("Carro 2")
                print("Carro 3")
                print("Fim")
            if opc == "3":
                print("Lista de desejos")
                print("Esses são seus carros da lista de desejos:")
                print("Carro 1")
                print("Carro 2")
        if opc == "2":
            print("Cliente")
            print("Opcao finalizada!")
        if opc == "3":
            print("Veículos")
            print("1-Veículos disponíveis")
            print("2-Cadastrar Veículo")
            opc = input("Digite a opção desejada:")
            if opc == "1":
                print("Veiculo 1")
                print("Veículo 2")
                opc = input("Selecione o carro desejado:")
                if opc == "1":
                    print("Veículo selecionado-1")
                if opc == "2":
                    print("Veículo selecionado-2")
            if opc == "2":
                print("Ficha de Cadastro de Veículo")
                marca = input('Informe a marca do veículo:\n')
                modelo = input("Informe o modelo do veículo:\n")
                categoria = input("Informe a categoria do veículo (Grande - Médio - Pequeno:\n")
                placa = input("Informe a placa do veículo: \n")
                cor = input("Informe a cor do veículo \n")
                print("Veíclo cadastrado com sucesso!")
                print(marca)
                print(modelo)
                print(categoria)
                print(placa)
                print(cor)
                print("Fim")
    if opcao == "2":
        print("Bem vindo aos alugueis de carros")
        print("Por favor, selecione o período que deseja alugar")
        print("A - Período Curto de 7 a 10 dias")
        print("B - Período Médio de 12 a 18 dias")
        print("C - Período Longo de 23 a 30 dias")
        selecao = input("Escolha uma opção:")
        if selecao == "A" or selecao == "a":
            print("Período Curto selecionado, escolha qual carro deseja alugar")
            print(" 1. Carros grandes")
            print(" 2. Carros médios")
            print(" 3. Carros pequenos")
        if selecao == "B" or selecao == "b":
            print("Período Médio selecionado, escolha qual carro deseja alugar")
            print(" 1. Carros grandes")
            print(" 2. Carros médios")
            print(" 3. Carros pequenos")
        if selecao == "C" or selecao == "c":
            print("Período Longo selecionado, escolha qual carro deseja alugar")
            print(" 1. Carros grandes")
            print(" 2. Carros médios")
            print(" 3. Carros pequenos")

else:
    print("Usuário ou senha inválida")
