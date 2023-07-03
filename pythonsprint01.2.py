# Variáveis globais
total_bikes = 0
total_seguro = total_bikes * 0.1
cadastro_realizado = False
registro_bike_realizado = False

#Loop principal do programa
while True:
    # Menu de opções
    print("Selecione uma opção:")
    print("1 - Faça o login caso ja seja cliente!")
    print("2 - Faça seu cadastro na Porto!")
    print("3 - Solicitar seguro de bike")
    print("4 - Valor do seguro")
    print("5 - Encerrar atendimento")

    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        login = int(input("Digite seu CPF ou CNPJ: "))
        senha = input("Digite sua senha: ")
        cadastro_realizado = True

    # Opçao 2: Informações do usuário
    elif opcao == 2:
        nome_usuario = input("Digite seu nome completo: ")
        email = input("Digite seu email principal: ")
        cep = int(input("Digite seu CEP: "))
        while True:
            celular = input("Digite o seu número de celular (apenas números 10 a 11): ")
            if celular.isnumeric() and len(celular) in [10, 11]:
                print(f"O número {celular} foi cadastrado com sucesso!")
                break
            else:
                print("Por favor, digite apenas números.")
         
        while True:  
            cpf = input("Digite seu CPF (apenas 11 números): ")
            if cpf.isnumeric() and len(cpf) == 11:
                print("CPF válido!!", cpf)
                cadastro_realizado = True
                break
            else:
                cpf_inv = ""
                while cpf_inv != "S" and cpf_inv != "N":
                    cpf_inv = input("CPF inválido deseja tentar novamente? (S/N)").upper()
                if cpf_inv == "N":
                    print("Retornando ao menu principal...")
                    break
        

    # Opção 3: Registrar Bike
    elif opcao == 3:
        if not cadastro_realizado:
            print("É necessário realizar o cadastro primeiro.")
        else:
            plano = input("Qual plano deseja? Pedal essencial (1) / Pedal leve (2) / Pedal elite (3): ")
            nm_bike = input("Digite o modelo da bike: ")
            chassi_bike = int(input("Digite o chassi da bike (apenas numeros): "))
            bike = float(input("Digite o valor da bike: "))
            acss_bike = input("Sua bike possui algum acessório? Se sim, quais?: ")
            inf_bike = input("Por favor de uma descrição atual da sua bike, data de compra, algum risco, etc: ")
            nota_fiscal = input("Você possui a nota fiscal da bike? (S/N): ").upper()
            if nota_fiscal == "S":
                nota_fiscal = int(input("Por favor digite a nota fiscal da sua bike: "))
            else:
                print("Não se preocupe caso não tenha. Pediremos informações adicionais no futuro.")
            print("Bike registrada com sucesso. Logo encaminharemos você para nossa vistoria realizada pela nossa Inteligência Artificial.")
            registro_bike_realizado = True


            '''
            # opcao 3 Inteligencia artificial/reconhecimento de imagem
            Aqui sera possivelmente sera implementada a programação da IA no futuro, reconhecimento de imagem etc.

            '''


    # Opção 4: Exibir total de valores da Bike 
    elif opcao == 4:
        if not registro_bike_realizado:
            print("É necessário registrar a bike primeiro.")
        else:
            print(f"Modelo da bike: {nm_bike}")
            print(f"Valor da bike: R$ {bike}")
            print(f"Valor do seguro em cima do valor da bike: R$ {bike * 0.1}")

    # Opção 5: Encerrar atendimento
    elif opcao == 5:
        print("Encerrando atendimento... obrigado por contar com a Porto!")
        break

    # Opção invalida
    else:
        print("Opção inválida. Tente novamente.")

    # Perguntar se o usuário deseja realizar outra operação
    resposta = ""
    while resposta != "S" and resposta != "N":
        resposta = input("Deseja realizar outra operação? (S/N)").upper()
    if resposta == "N":
        print("Encerrando atendimento, obrigado por contar com a Porto!")
        break
