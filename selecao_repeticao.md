## Estruturas de Seleção e Repetição em Python

### Estruturas de Seleção (if)

As estruturas de seleção em Python, principalmente o comando `if`, permitem que seu programa tome decisões com base em condições. Elas avaliam uma expressão booleana e executam um bloco de código se a condição for verdadeira.

**Sintaxe básica:**
```python
if condição:
    # Código a ser executado se a condição for verdadeira
else:
    # Código a ser executado se a condição for falsa
```

**Exemplo:**
```python
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

**Características:**
* **Condição:** Deve ser uma expressão que resulte em um valor booleano (True ou False).
* **Blocos de código:** Indentados para indicar qual código pertence a cada condição.
* **`elif`:** Pode ser usado para adicionar mais condições.
* **`else`:** Executado se nenhuma das condições anteriores for verdadeira.

### Estruturas de Repetição (Loops)

As estruturas de repetição permitem que um bloco de código seja executado repetidamente enquanto uma determinada condição for verdadeira.

**1. `for`:**
   * Utilizado para iterar sobre sequências (listas, tuplas, strings, etc.).
   * **Sintaxe:**
     ```python
     for elemento in sequência:
         # Código a ser executado para cada elemento
     ```
   * **Exemplo:**
     ```python
     frutas = ["maçã", "banana", "laranja"]
     for fruta in frutas:
         print(fruta)
     ```

**2. `while`:**
   * Continua a executar um bloco de código enquanto uma condição for verdadeira.
   * **Sintaxe:**
     ```python
     while condição:
         # Código a ser executado enquanto a condição for verdadeira
     ```
   * **Exemplo:**
     ```python
     contador = 0
     while contador < 5:
         print(contador)
         contador += 1
     ```

**Características:**
* **Condição:** Deve ser uma expressão que resulte em um valor booleano.
* **Iteração:** O loop continua até que a condição se torne falsa.
* **`break`:** Interrompe o loop imediatamente.
* **`continue`:** Pula para a próxima iteração do loop.

**Exemplo completo:**
```python
numeros = [1, 2, 3, 4, 5]
soma = 0

for numero in numeros:
    if numero % 2 == 0:
        soma += numero

print("A soma dos números pares é:", soma)
```
