# Biblioteca Requisição
import requests
# Responsavel por tratar o retorno
from bs4 import BeautifulSoup

# pip install requests
# pip install bs4

headers = {
    "User-Agent": "Mozilla/5.0 (Windowns NT 10.0; Win64; x64) AppleWebKit/537.36"
}

url = "https://www.inter.it/en/"

# Fazendo requisição http
resposta = requests.get(url, headers=headers)

# Verificar se deu certo :)
if resposta.status_code == 200:
    print("requisição feita com sucesso!")
    # 200 -> OK

    # Traduzir a resposta do site
    soup = BeautifulSoup(resposta.text, "html.parser")
    #Recortar informação
    noticias = soup.find_all("a", class_="css-0")

    print("Últimas noticias:")
    for noticia in noticias:
        print(f"{noticia.text} - {noticia['href']}")
else:
    print("Deu errado!!")