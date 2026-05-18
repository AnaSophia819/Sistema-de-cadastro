cadastros = []

while True:
    print("=== Sistema de Cadastro ===")
    print("1 - Novo Cadastro")
    print("2 - Listar")
    print("3 - Sair")

    escolha = input("Digite o número desejado: ")

    if escolha == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        email = input("E-mail: ")

        cadastro = {"Nome": nome, "Idade": idade, "E-mail": email}

        cadastros.append(cadastro)

        print("Cadastro feito com sucesso!")

    elif escolha == "2":
        print("=== USUÁRIOS ===")

        for cadastro in cadastros:
            print(f'Nome: {nome['Nome']}')
            print(f'Idade: {idade['Idade']}')
            print(f'E-mail: {email['E-mail']}')
            print('-' * 20)

    elif escolha == "3":
        print("Encerrando programa...")
        break

    else:
        print("Resposta inválida.")

        