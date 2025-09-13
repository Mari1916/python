
class Pessoa:

    # difinição
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def cadastrar(self):
        print("Cadastrando Pessoa")

    def sair(self):
        print("Saindo do Sistema")
