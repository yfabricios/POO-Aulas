from dao_sql.dao import DAO
from models.horario import Horario

class AtendimentoDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO horario (id, data, queixa_principal, historico_saude, avaliacao, prescricao)
            VALUES (?, ?, ?, ?)
        """
        cls.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_senha()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM horario"
        cursor = cls.execute(sql)

        rows = cursor.fetchall()
        objs = [Horario(id, data, queixa_principal, historico_saude, avaliacao, prescricao) for (id, data, queixa_principal, historico_saude, avaliacao, prescricao) in rows]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM horario WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Horario(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE horario SET nome=?, email=?, fone=?, senha=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_senha(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM horario WHERE id=?"
        cls.execute(sql, (obj,))
        cls.fechar()