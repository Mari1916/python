import pandas as pd 
import matplotlib.pyplot as plt

# pip install pandas
# pip install matplotlib

ARQUIVO = "produtos.csv"
CAMPOS = ["Nome", "Quantidade", "Preco"]

df = pd.read_csv(ARQUIVO, encoding="utf-8")

df["Faturamento"] = df["Quantidade"] * df["Preco"]
print(df)

df.boxplot(column="Preco", by="Nome", grid=True)
plt.title("Distribuição de Preco por Produto")
plt.xlabel("Preço")
plt.ylabel("Produto")

plt.show()



df.plot(kind="bar", x="Nome", y="Preco", grid=True)
plt.title("Preco dos Produtos")
plt.xlabel("Nome")
plt.ylabel("Preco")

plt.show()

df.plot(kind="pie", x="Nome", y="Quantidade", grid=True)
plt.title("Preco dos Produtos")
plt.xlabel("Nome")
plt.ylabel("Quantidade")

plt.show()