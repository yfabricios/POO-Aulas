import json
from models.dao import DAO
from models.pagamento import Pagamento


class PagamentoDAO(DAO):
    def __init__(self):
        super().__init__("pagamentos.json")

    def _abrir(self):  
        try:  
            arquivo = open(self._arquivo, mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            self._objetos = []
            for dic in list_dic:
                obj = Pagamento.from_json(dic)
                self._objetos.append(obj)
        except FileNotFoundError:
            pass

    def _salvar(self):    
        arquivo = open(self._arquivo, mode = "w")
        json.dump(self._objetos, arquivo, default = Pagamento.to_json, indent = 2)
        arquivo.close()

    def listar_id_atendimento(self, id_atendimento):
        self.abrir()
        for obj in self.objetos:
            if obj.get_id_atendimento() == id_atendimento:
                return obj
        return None
