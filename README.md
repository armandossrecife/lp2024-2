# lp2024-2

Turma de Laboratório de Programação UFPI 2024.2 (Departamento de Computação)

## Variáveis, Tipos e Operações

[Exemplos](https://github.com/armandossrecife/lp2024-2/blob/main/introducao_ao_python1.ipynb)

### Variáveis em Python

* **Conceito:** Uma variável em Python é como um rótulo que você atribui a um valor. É uma forma de armazenar dados na memória do computador para que você possa usá-los mais tarde em seu programa.
* **Declaração:** Em Python, você não precisa declarar explicitamente o tipo de uma variável. O tipo é inferido automaticamente pelo interpretador no momento da atribuição.
* **Atribuição:** Utiliza-se o sinal de igual (=) para atribuir um valor a uma variável. 
    * Exemplo: `idade = 30`

**Atribuindo valores a variáveis**
```python
nome = "João"
idade = 30
altura = 1.75
```

### Tipos de Dados em Python
Python possui diversos tipos de dados built-in, os mais comuns são:

* **Números:**
    * **int:** Números inteiros (ex: 42, -10)
    * **float:** Números de ponto flutuante (ex: 3.14, -2.5)
    * **complex:** Números complexos (ex: 2+3j)
* **Strings:** Sequências de caracteres (ex: "Olá, mundo!", 'Python')
* **Booleanos:** Valores lógicos (True ou False)
* **Listas:** Coleções ordenadas e mutáveis de itens (ex: [1, 2, 3], ["apple", "banana"])
* **Tuplas:** Coleções ordenadas e imutáveis de itens (ex: (1, 2, 3), ("apple", "banana"))
* **Dicionários:** Coleções de pares chave-valor (ex: {"nome": "Alice", "idade": 30})
* **Conjuntos:** Coleções não ordenadas e sem elementos duplicados (ex: {1, 2, 3})

### Operações em Python
* **Operadores Aritméticos:**
    * `+`: Adição
    * `-`: Subtração
    * `*`: Multiplicação
    * `/`: Divisão
    * `//`: Divisão inteira
    * `%`: Resto da divisão
    * `**`: Potência
* **Operadores de Comparação:**
    * `==`: Igual a
    * `!=`: Diferente de
    * `<`: Menor que
    * `>`: Maior que
    * `<=`: Menor ou igual a
    * `>=`: Maior ou igual a
* **Operadores Lógicos:**
    * `and`: E lógico
    * `or`: Ou lógico
    * `not`: Negação
* **Operadores de Atribuição:**
    * `=`: Atribuição simples
    * `+=`: Acrescenta e atribui
    * `-=`: Subtrai e atribui
    * `*=`: Multiplica e atribui
    * `/=`: Divide e atribui
    * `//=`: Divisão inteira e atribui
    * `%=`: Resto da divisão e atribui
    * `**=`: Potência e atribui

**Exemplos**
```python
soma = 10 + 5
subtracao = 20 - 3
multiplicacao = 4 * 2
divisao = 10 / 2
```

```python
print("Olá,", nome)
print("Você tem", idade, "anos e", altura, "m de altura.")
print("Resultados das operações:")
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
```

**Observações:**
* O tipo de uma variável pode ser verificado usando a função `type()`.
* Python é uma linguagem tipada dinamicamente, o que significa que você não precisa declarar o tipo de uma variável antes de usá-la.
* As operações entre diferentes tipos de dados podem resultar em conversões implícitas.

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
