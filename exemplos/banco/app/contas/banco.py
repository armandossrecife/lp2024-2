# contas/banco.py
from app.contas.contas import Conta

class Banco:
    def __init__(self):
        self.contas = []

    def criar_conta(self, numero, cpf_cliente, saldo=0):
        nova_conta = Conta(numero, cpf_cliente, saldo)
        self.contas.append(nova_conta)
        print("Conta criada com sucesso!")

    def buscar_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero == numero_conta:
                return conta
        print("Conta não encontrada.")
        return None

    def realizar_operacao(self, numero_conta, operacao, valor):
        conta = self.buscar_conta(numero_conta)
        if conta:
            if operacao == "depositar":
                conta.depositar(valor)
            elif operacao == "sacar":
                conta.sacar(valor)
            else:
                print("Operação inválida.")
        else:
            print("Conta não encontrada.")