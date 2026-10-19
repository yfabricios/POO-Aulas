import pyodbc

try:

    # conecta o banco de dados
    string_conexao = 'Driver={ODBC Driver 17 for SQL Server};Server=.;Database=LOL;UID=sa;PWD=senha@12345'

    conexao = pyodbc.connect(string_conexao)
    print("Conexão bem-sucedida!")

    # select na tabela contato
    cursor = conexao.cursor()
    cursor.execute('select id, nome, telefones, email, datanascimento from contato')

    registros = cursor.fetchall()

    for reg in registros:
        print(f'ID: {reg[0]}; Nome: {reg[1]}; telefones: {reg[2]}; email: {reg[3]}; datanascimento: {reg[4]}')
        print()

    lista_paises = [
        ('Brasil', 'América do Sul', 'Brasília', 214000000),
        ('Japão', 'Ásia', 'Tóquio', 125000000),
        ('França', 'Europa', 'Paris', 67000000),
        ('Canadá', 'América do Norte', 'Ottawa', 38000000),
        ('Egito', 'África', 'Cairo', 109000000)
    ]


except Exception as err:
    print(f"Erro BD: {err}")