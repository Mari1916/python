# Sistema de tarefas
tarefas = []  # Lista vazia

while True:
    print("=== MENU TAREFAS ===")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefa")
    print("9 - Sair do Sistema")

    opcao = input("Escolha sua opção: ")

    # Adicionar tarefa
    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")

    # Listar tarefas
    elif opcao == "2":
        if len(tarefas) == 0:
            print("Não existem tarefas cadastradas!")
        else:
            print("=== TAREFAS CADASTRADAS ===")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")
    
    # Sair 
    elif opcao == "9":
        print("Saindo do sistema!")
        break

    else:
        print("Opção inexistente, tente novamente...")
