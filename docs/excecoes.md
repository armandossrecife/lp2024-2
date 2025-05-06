## Tratamento de Exceções em Python

O tratamento de exceções em Python é uma técnica fundamental para garantir a robustez e a segurança de seus programas. Ele permite que você antecipe e lide com erros que podem ocorrer durante a execução do código, evitando que seu programa pare abruptamente.

[https://docs.python.org/pt-br/3/tutorial/errors.html](https://docs.python.org/pt-br/3/tutorial/errors.html)

## **1. Introdução**  

O tratamento de exceções é essencial para garantir que um programa continue executando mesmo quando ocorrem erros inesperados. Ele permite:  
- **Evitar interrupções abruptas** do programa.  
- **Fornecer feedback claro** ao usuário sobre erros.  
- **Melhorar a manutenção e depuração** do código.  

---

## **2. O que são Exceções?**  
Exceções são eventos que interrompem o fluxo normal de um programa quando ocorre um erro.  

### **Tipos de Exceções**  
- **Erros de Sintaxe (`SyntaxError`)** → Código mal escrito (detectado antes da execução).  
- **Erros em Tempo de Execução (`RuntimeError`)** → Ocorrem durante a execução (ex: divisão por zero).  
- **Erros Lógicos** → Problemas na lógica do programa (não são detectados pelo Python).  

### **Exemplos de Exceções Comuns**  
| Exceção | Causa |  
|---------|-------|  
| `ValueError` | Valor inválido (ex: `int("abc")`). |  
| `TypeError` | Operação com tipos incompatíveis (ex: `"10" + 5`). |  
| `IndexError` | Índice fora do intervalo (ex: `lista[10]` em uma lista de 5 elementos). |  
| `KeyError` | Chave inexistente em um dicionário. |  
| `ZeroDivisionError` | Divisão por zero. |  
| `FileNotFoundError` | Tentativa de abrir um arquivo que não existe. |  

---

## **3. Tratamento de Exceções com `try-except`**  
### **Sintaxe Básica**  
```python
try:
    # Código que pode gerar uma exceção
except TipoDaExcecao:
    # Código executado se a exceção ocorrer
```  

### **Exemplo Prático**  
```python
try:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    resultado = num1 / num2
    print("Resultado:", resultado)
except ValueError:
    print("Erro: Valor inválido! Digite um número.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não permitida!")
```  

### **Tratamento Genérico (não recomendado para produção)**  
```python
try:
    # Código perigoso
except Exception as e:  # Captura qualquer exceção
    print(f"Ocorreu um erro: {e}")
```  

---

## **4. Blocos `else` e `finally`**  
### **`else`** → Executado **apenas se nenhuma exceção ocorrer**.  
```python
try:
    arquivo = open("dados.txt", "r")
except FileNotFoundError:
    print("Arquivo não encontrado!")
else:
    print("Arquivo lido com sucesso!")
    arquivo.close()
```  

### **`finally`** → **Sempre executado**, independentemente de erros.  
```python
try:
    arquivo = open("dados.txt", "r")
    print(arquivo.read())
except FileNotFoundError:
    print("Arquivo não encontrado!")
finally:
    arquivo.close()  # Garante que o arquivo será fechado
```  

---

## **5. Lançamento de Exceções (`raise`)**  
### **Quando Usar?**  
- Para **forçar um erro** quando uma condição indesejada ocorre.  
- Para **criar exceções personalizadas**.  

### **Sintaxe**  
```python
raise TipoDaExcecao("Mensagem de erro")
```  

### **Exemplo**  
```python
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não permitida!")
    return a / b

try:
    dividir(10, 0)
except ZeroDivisionError as e:
    print(e)  # Saída: "Divisão por zero não permitida!"
```  

### **Criando Exceções Personalizadas**  
```python
class SaldoInsuficienteError(Exception):
    pass

def sacar(valor, saldo):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente!")
    return saldo - valor

try:
    sacar(1000, 500)
except SaldoInsuficienteError as e:
    print(e)  # Saída: "Saldo insuficiente!"
```  

---

## **6. Boas Práticas no Tratamento de Exceções**  
**Seja específico** → Capture exceções específicas, evite `except Exception`.  
**Mantenha blocos `try` pequenos** → Facilita a leitura e manutenção.  
**Use `finally` para liberar recursos** → Fechar arquivos, conexões, etc.  
**Documente exceções** → Use docstrings para explicar possíveis erros.  
**Não silencie exceções sem motivo** → Pode mascarar bugs.  

---

## **7. Conclusão**  
- **Tratamento de exceções** torna o código mais **robusto e confiável**.  
- **`try-except-else-finally`** permite um controle preciso sobre erros.  
- **`raise`** é útil para forçar ou criar exceções personalizadas.  
- **Siga boas práticas** para evitar problemas de manutenção.  
