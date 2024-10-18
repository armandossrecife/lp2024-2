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

## Entrada e Saída de Dados Simples em Python

**Entrada de dados** em Python se refere ao processo de obter informações do usuário ou de um arquivo externo para serem utilizadas em um programa. A função principal para isso é a `input()`.

**Saída de dados** é a forma de exibir o resultado de um cálculo ou qualquer outra informação para o usuário. A função mais comum para isso é a `print()`.

### Função `input()`
* **Sintaxe:** `variavel = input("mensagem para o usuário")`
* **Funcionamento:**
  1. A mensagem entre aspas é exibida na tela.
  2. O programa pausa, esperando que o usuário digite algo e pressione Enter.
  3. O valor digitado pelo usuário é armazenado na variável especificada.

**Exemplo:**
```python
nome = input("Digite seu nome: ")
print("Olá,", nome + "!")
```

### Função `print()`
* **Sintaxe:** `print("mensagem a ser exibida")`
* **Funcionamento:**
  1. Exibe a mensagem entre aspas na tela.
  2. Você pode concatenar strings usando o operador `+` para combinar texto com variáveis.

**Exemplo:**
```python
idade = 25
print("Eu tenho", idade, "anos.")
```

### Conversão de tipos
É importante lembrar que a função `input()` retorna sempre uma string. Se você precisar de um número (inteiro ou float), é necessário converter o valor usando as funções `int()` ou `float()`:

```python
numero = int(input("Digite um número: "))
print("O dobro do número é:", numero * 2)
```

### Em resumo
* **`input()`:** Captura dados do usuário.
* **`print()`:** Exibe dados na tela.
* **Conversão de tipos:** Use `int()` e `float()` para converter strings em números.
