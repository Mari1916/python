
class Carro:

    # Configuração inicial do objeto
    def __init__(self, nome, cor, modelo, ano, marca):
        self.nome = nome
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.marca = marca

    def correr(self):
        print("Correndo dms!!!!")
    
    def frear(self):
        print("Freiando nas últimas!!")

    def ligar(self):
        print("ligando o carro", self.nome)

passatiCarro = Carro("Passati", "Verde", "V1", "2025", "BMW")
passatiCarro.ligar()
passatiCarro.correr()
passatiCarro.frear()