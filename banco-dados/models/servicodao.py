from models.servico import Servico
from models.conexao import get_connection, criar_tabelas

class ServicoDAO:
    def __init__(self):
        criar_tabelas()
        self.__conn = get_connection()

    def inserir(self, obj):
        cursor = self.__conn.cursor()
        cursor.execute(
            "INSERT INTO servicos (descricao, valor) VALUES (?, ?)",
            (obj.get_descricao(), obj.get_valor())
        )
        self.__conn.commit()
        obj.set_id(cursor.execute("SELECT SCOPE_IDENTITY()").fetchone()[0])

    def listar(self):
        cursor = self.__conn.cursor()
        cursor.execute("SELECT id, descricao, valor FROM servicos")
        registros = cursor.fetchall()
        return [Servico(r[0], r[1], float(r[2])) for r in registros]

    def listar_id(self, id):
        cursor = self.__conn.cursor()
        cursor.execute("SELECT id, descricao, valor FROM servicos WHERE id = ?", (id,))
        r = cursor.fetchone()
        if r is None:
            return None
        return Servico(r[0], r[1], float(r[2]))

    def atualizar(self, obj):
        cursor = self.__conn.cursor()
        cursor.execute(
            "UPDATE servicos SET descricao = ?, valor = ? WHERE id = ?",
            (obj.get_descricao(), obj.get_valor(), obj.get_id())
        )
        self.__conn.commit()

    def excluir(self, id):
        cursor = self.__conn.cursor()
        cursor.execute("DELETE FROM servicos WHERE id = ?", (id,))
        self.__conn.commit()