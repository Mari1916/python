
class ContaBancaria:

    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
            return True
        else:
            return False

    def get_saldo(self):
        return self.saldo

contaMari = ContaBancaria(1000)

contaMari.sacar(50)
contaMari.depositar(70)

print(contaMari.get_saldo())