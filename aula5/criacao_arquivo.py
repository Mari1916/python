import csv

dados = [
    ["Nome", "Preco", "Quantidade"],
    ["Camiseta", "10.00", "8"],
    ["Tenis", "20.00", "5"],
    ["Chinelo", "60.00", "1"], 
    ["Moleotm", "170.00", "9"],
    ["Jaqueta", "20.00", "2"]
]

# Criar Arquivo
with open("dados_pandas.csv", "w", newline="", encoding="utf-8") as csvarquivo:
    escritor = csv.writer(csvarquivo)
    escritor.writerows(dados)