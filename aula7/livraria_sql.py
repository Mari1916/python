import sqlite3

conn = sqlite3.connect("livros.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        autor TEXT,
        ano INTEGER
    )
''')

# loop principal
while True:
    print("\n=== CADASTRO DE LIVROS ===")
    print("1 - Cadastrar novo livro")
    print("2 - Listar livros")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título do livro: ")
        autor = input("Autor: ")
        ano = input("Ano de publicação: ")

        cursor.execute("INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)",
                       (titulo, autor, ano))
        conn.commit()
        print(f'Livro "{titulo}" cadastrado com sucesso!')
    
    elif opcao == "2":
        print("\nLivros cadastrados:")
        for linha in cursor.execute("SELECT * FROM livros"):
            print(f'ID: {linha[0]} | Título: {linha[1]} | Autor: {linha[2]} | Ano: {linha[3]}')
    
    elif opcao == "3":
        print("Encerrando sistema...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")

conn.close()
