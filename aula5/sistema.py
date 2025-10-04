import csv
import time

ARQUIVO = "produtos.csv"

# Assim que executar ele verifica se o arquivo existe e cria
try:
    # x -> model unico de criaçao 
    with ope(ARQUIVO, "x", newline="") as arquivo:
        escritor = csv.writer(arquivo)
    escritor.writerow(["Nome", "Quantidade", "Preco"])
except:
    pass # Se ja existe o arquivo ele segue em frente

while True:
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))

    #Escrever no arquivo CSV
    with open(ARQUIVO, "a", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, quantidade, preco])

    print(f"Produto {nome} adicionada com sucesso!")

    # Perguntar se deseja continuar no sistema
    continuar = input("Deseja adicionar outro? (s/n): ")
    if continuar == "n":
        print("Encerrando sistema...")
        break
    
    print("-" * 30) #----------
    time.sleep(1) # Ele vai demorar um segundo para rodar dnv