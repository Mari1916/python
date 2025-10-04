import sqlite3

conn = sqlite3.connect('alunos.db')
cursor = conn.cursor()

# Cira uma tabela se nn existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TXT,
    nota REAL
)
''')

# Inserir dados
cursor.execute('INSERT INTO alunos (nome, nota) VALUES (?, ?)', ('Mariana', 10.0))
conn.commit() # Executar

# Consultar dados
for row in cursor.execute("SELECT * FROM alunos"):
    print(row)

conn.close()