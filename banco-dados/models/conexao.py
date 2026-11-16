import pyodbc


def conectar():
    try:
        return pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=.;"
            "Database=trabalho;"
            "UID=sa;"
            "PWD=senha@12345;"
            "TrustServerCertificate=yes;"
        )
    except pyodbc.DatabaseError:
        conn_master = pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=.;"
            "Database=master;"
            "UID=sa;"
            "PWD=senha@12345;"
            "TrustServerCertificate=yes;"
        )
        cursor = conn_master.cursor()
        cursor.execute("SELECT 1 FROM sys.databases WHERE name = 'trabalho'")
        if not cursor.fetchone():
            cursor.execute("CREATE DATABASE trabalho")
        conn_master.commit()
        conn_master.close()

        return pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=.;"
            "Database=trabalho;"
            "UID=sa;"
            "PWD=senha@12345;"
            "TrustServerCertificate=yes;"
        )