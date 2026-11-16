from models.cliente import Cliente
from models.conexao import get_connection, criar_tabelas

class ClienteDAO:
    def __init__(self):
        criar_tabelas()
        self.__conn = get_connection()

    def inserir(self, obj):
        cursor = self.__conn.cursor()
        cursor.execute(
            "INSERT INTO clientes (nome, email, fone) VALUES (?, ?, ?)",
            (obj.get_nome(), obj.get_email(), obj.get_fone())
        )
        self.__conn.commit()
        obj.set_id(cursor.execute("SELECT SCOPE_IDENTITY()").fetchone()[0])

    def listar(self):
        cursor = self.__conn.cursor()
        cursor.execute("SELECT id, nome, email, fone FROM clientes")
        registros = cursor.fetchall()
        return [Cliente(r[0], r[1], r[2], r[3]) for r in registros]

    def listar_id(self, id):
        cursor = self.__conn.cursor()
        cursor.execute("SELECT id, nome, email, fone FROM clientes WHERE id = ?", (id,))
        r = cursor.fetchone()
        if r is None:
            return None
        return Cliente(r[0], r[1], r[2], r[3])

    def atualizar(self, obj):
        cursor = self.__conn.cursor()
        cursor.execute(
            "UPDATE clientes SET nome = ?, email = ?, fone = ? WHERE id = ?",
            (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_id())
        )
        self.__conn.commit()

    def excluir(self, id):
        cursor = self.__conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
        self.__conn.commit()
