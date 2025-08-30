print("Bem vindo ao banco RoubaTudo")
saldo = float(input("DIgite seu saldo(R$):"))

transferencia = float(input("Qual o valor da sua transferência?(R$):"))

# valida de ela possui saldo o suficiente para realizar a transferência
if saldo >= transferencia:
    print("Saldo Suficiente!!")
    # Atualizando valor do saldo
    saldo = saldo - transferencia
    print("Seu saldo atual é: ", saldo)
else:
    print("Saldo não é suficiente!!!!")