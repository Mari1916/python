from controller.cliente_controller import cliente_controller

def exibir_menu():
    print("=== MENU ===")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Cliente")
    print("0 - Sair do Sistema")

def main():
    clienteController = cliente_controller()

    while True:
        exibir_menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            idade = int(input("Digite a idade do cliente: "))
            clienteController.criar_cliente(nome, email, idade)

        elif opc == "2":
            clientes = clienteController.listar_cliente()
            for index, cliente in enumerate(clientes, 1):
                print(f'{index} - {cliente}')

        elif opc == "0":
            print("Saindo do sistema!")
            break

        else:
            print("Opção Inválida")

if __name__ == "__main__":
    main()
