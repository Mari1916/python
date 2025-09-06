from models.Pessoa import Pessoa

def menu():
    print("=== MENU ===")
    print("1 - Criar Pessoa")
    print("2 - Listar Pessoas")
    print("3 - Limpar Lista")
    print("9 - Sair do Sistema")

def iniciarSistema():
    print("Sistema iniciado!")
    pessoas = [] # Criara Lista de Pessoas

    while(True):
        menu()
        opcao = input("Digite sua opção:")
        if opcao == "1":
            nome = input("Digite o nome do usuário..")
            email = input("Digite o email do usuário..")
            pessoa = Pessoa(nome, email) # Manifestando a entidade
            pessoas.append(pessoa) # Adicionando a pessoa cadastrada a lista de pessoas
        elif opcao == "2":
            for pessoa in pessoas:
                print(pessoa)
                print(f'Nome: {pessoa.get_nome()}, Email: {pessoa.get_email()}')

# Lógica para iniciar automáticamente
if __name__ == "__main__":
    iniciarSistema()