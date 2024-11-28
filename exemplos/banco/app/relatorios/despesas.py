# relatórios/despesas.py
class Despesas:
    def __init__(self):
        self.despesas = []

    def registrar_despesa(self, descricao, valor, data):
        self.despesas.append((descricao, valor, data))

    def gerar_relatorio(self, inicio, fim):
        # Filtra as despesas e gera um relatório
        pass