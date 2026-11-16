import pyodbc

def conectar():
    return pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=.;"
        "Database=master;"
        "UID=sa;"
        "PWD=senha@12345;"
        "TrustServerCertificate=yes;"
    )