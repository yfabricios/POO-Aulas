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

except Exception as err:
    print(f"Erro BD: {err}")