class Conta:
    def __init__(self, numero, cpf_cliente, saldo):
        self.numero = numero
        self.cpf_cliente = cpf_cliente
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

# contas/investimentos.py
class Investimentos:
    def __init__(self):
        self.carteira = {}

    def adicionar_investimento(self, ativo, valor):
        self.carteira[ativo] = valor

    def calcular_rendimento(self):
        # Lógica para calcular o rendimento da carteira
        pass