from service import Service

class UI:

    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()

        @staticmethod
        def menu():
            print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 9-Fim")
            return int(input('Informe uma opção:'))
        
        @staticmethod
        def cliente_inserir():
            id = int(input("id: "))
            nome = int(input("nome: "))
            email = int(input("email: "))
            fone = int(input("telefone: "))
            Service.cliente_inserir(id, nome, email, fone)

        @staticmethod
        def cliente_listar():
            for obj in Service.cliente_listar(): print(obj)

        @staticmethod
        def cliente_atualizar():
            for obj in Service.cliente_listar(): print(obj)
            id = int(input("id: "))
            nome = int(input("nome: "))
            email = int(input("email: "))
            fone = int(input("telefone: "))
            Service.cliente_inserir(id, nome, email, fone)

        @staticmethod
        def cliente_excluir():
            for obj in Service.cliente_listar(): print(obj)
            id = int(input("id para excluir: "))
            Service.cliente_excluir(id)

UI.main()