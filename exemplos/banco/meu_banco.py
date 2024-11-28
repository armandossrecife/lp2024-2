from app.contas.banco import Banco
from app.contas.contas import Investimentos
from app.relatorios.despesas import Despesas

# Criando um banco
banco = Banco()
# Exemplo de uso:
investimento = Investimentos()
despesa = Despesas()

numero_conta1 = 123
numero_conta2 = 456

# Criando algumas contas
print(f"Conta: {numero_conta1}")
banco.criar_conta(numero_conta1, "12345678910", 1000)
print(f"Conta: {numero_conta2}")
banco.criar_conta(numero_conta2, "98765432109", 500)

# Realizando operações
print(f"Conta: {numero_conta1}")
banco.realizar_operacao(123, "depositar", 500)
print(f"Conta: {numero_conta2}")
banco.realizar_operacao(456, "sacar", 200)

# Consultando saldo

conta = banco.buscar_conta(numero_conta1)
print(f"Conta: {numero_conta1}")
conta.consultar_saldo()