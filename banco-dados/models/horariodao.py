from models.horario import Horario
from models.conexao import conectar


def get_connection():
    return conectar()


class HorarioDAO:
    def __init__(self):
        self.__conn = get_connection()

    def inserir(self, obj):
        cursor = self.__conn.cursor()
        cursor.execute(
            "INSERT INTO horarios (data, confirmado, id_cliente, id_servico) VALUES (?, ?, ?, ?)",
            (
                obj.get_data(),
                int(obj.get_confirmado()),
                obj.get_id_cliente(),
                obj.get_id_servico()
            )
        )
        self.__conn.commit()
        id_gerado = cursor.execute("SELECT SCOPE_IDENTITY()").fetchone()
        obj.set_id(id_gerado[0] if id_gerado and id_gerado[0] is not None else 0)

    def listar(self):
        cursor = self.__conn.cursor()
        cursor.execute("SELECT id, data, confirmado, id_cliente, id_servico FROM Horarios")
        registros = cursor.fetchall()
        horarios = []
        for r in registros:
            h = Horario(r[0], r[1])
            h.set_confirmado(bool(r[2]))
            h.set_id_cliente(r[3])
            h.set_id_servico(r[4])
            horarios.append(h)
        return horarios

    def listar_id(self, id):
        cursor = self.__conn.cursor()
        cursor.execute("SELECT id, data, confirmado, id_cliente, id_servico FROM Horarios WHERE id = ?", (id,))
        r = cursor.fetchone()
        if r is None:
            return None
        h = Horario(r[0], r[1])
        h.set_confirmado(bool(r[2]))
        h.set_id_cliente(r[3])
        h.set_id_servico(r[4])
        return h

    def atualizar(self, obj):
        cursor = self.__conn.cursor()
        cursor.execute(
            "UPDATE Horarios SET data = ?, confirmado = ?, id_cliente = ?, id_servico = ? WHERE id = ?",
            (
                obj.get_data(),
                int(obj.get_confirmado()),
                obj.get_id_cliente(),
                obj.get_id_servico(),
                obj.get_id()
            )
        )
        self.__conn.commit()

    def excluir(self, id):
        cursor = self.__conn.cursor()
        cursor.execute("DELETE FROM Horarios WHERE id = ?", (id,))
        self.__conn.commit()
