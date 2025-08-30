print("SISTEMA ADMINISTRATIVO")

usuario = input("Digite o usuário: ")
senha = input("Digite a seNha: ")

if usuario == "admin":
    if senha == "123456":
        print("Login bem sucedido!")
    else:
        print("Senha incorreta")
else:
    print("Usuário inválido")