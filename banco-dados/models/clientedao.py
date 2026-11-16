from models.cliente import Cliente
from models.conexao import conectar


def get_connection():
    return conectar()


class ClienteDAO:
    def __init__(self):
        self.__conn = get_connection()

    def inserir(self, obj):
        cursor = self.__conn.cursor()
        cursor.execute(
            "INSERT INTO clientes (nome, email, fone) VALUES (?, ?, ?)",
            (obj.get_nome(), obj.get_email(), obj.get_fone())
        )
        self.__conn.commit()
        id_gerado = cursor.execute("SELECT SCOPE_IDENTITY()").fetchone()
        obj.set_id(id_gerado[0] if id_gerado and id_gerado[0] is not None else 0)

    def listar(self):
        cursor = self.__conn.cursor()
        cursor.execute("SELECT id, nome, email, fone FROM Clientes")
        registros = cursor.fetchall()
        return [Cliente(r[0], r[1], r[2], r[3]) for r in registros]

    def listar_id(self, id):
        cursor = self.__conn.cursor()
        cursor.execute("SELECT id, nome, email, fone FROM Clientes WHERE id = ?", (id,))
        r = cursor.fetchone()
        if r is None:
            return None
        return Cliente(r[0], r[1], r[2], r[3])

    def atualizar(self, obj):
        cursor = self.__conn.cursor()
        cursor.execute(
            "UPDATE Clientes SET nome = ?, email = ?, fone = ? WHERE id = ?",
            (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_id())
        )
        self.__conn.commit()

    def excluir(self, id):
        cursor = self.__conn.cursor()
        cursor.execute("DELETE FROM Clientes WHERE id = ?", (id,))
        self.__conn.commit()
