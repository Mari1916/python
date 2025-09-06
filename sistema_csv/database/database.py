import json
from pathlib import Path

class BancoFake:
    def __init__(self, arquivo_db="banco.json"):
        self.arquivo_db = arquivo_db
        self.dados = {"clientes": []}
        self._carregar()

    def _carregar(self):
        """
        Carrega dados do arquivo JSON, se existir.
        Caso não exista, inicia um banco novo
        """
        caminho = Path(self.arquivo_db)
        if caminho.is_file():
            with open(caminho, "r", encoding="utf-8") as arquivo:
                self.dados = json.load(arquivo)
        else:
            self._salvar()

    def _salvar(self):
        """
        Salvar o conteúdo do self.dados no JSON
        """
        with open(self.arquivo_db, 'w', encoding="utf-8") as dados:
            json.dump(self.dados, dados, ensure_ascii=False, indent=4)

    def adicionar_cliente(self, cliente_dict):
        self.dados["clientes"].append(cliente_dict)
        self._salvar()

    def listar_clientes(self):
        return self.dados["clientes"]
