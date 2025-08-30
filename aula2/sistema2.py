
# Sistema de gerenciador de nomes
nomes = []

def menu():
    print("==== MENU ====")
    print("1 - Cadastrar Nome")
    print("2 - Listar Nomes")
    print("3 - Excluir Nomes")
    print("9 - Sair do Sistema")
    return input("Escolha uma opção: ")

def cadastro():
    nome = input("Digite o seu nome: ")
    nomes.append(nome)
    print("Nome adicionado com sucesso!")

def listar():
    if len(nomes) == 0:
        print("Não existem nomes cadastrados!")
    else:
        print("=== NOMES CADASTRADOS ===")
        for i, nome in enumerate(nomes, start=1):
            print(f"{i}. {nome}")

def deletar():
    if len(nomes) == 0:
        print("Não existem nomes cadastrados!")
    else:
        for posicao, nome in enumerate(nomes, start=1):
            print(f"{posicao}. {nome}")
        
        pos = int(input("Escolha o nome para deletar:"))
        nomes.remove(nomes[pos-1])
        print("Nome deletado")

def sair():
    print("Saindo do sistema!")

while True:
    opcao = menu()
    if opcao == "1": 
        cadastro()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        deletar()
    elif opcao == "9":
        sair()
        break
    else:
        print("Opção inválida, tente novamente!")
