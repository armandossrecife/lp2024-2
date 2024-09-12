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

## Listas em Python

**O que são listas em Python?**

Listas são estruturas de dados extremamente versáteis em Python, utilizadas para armazenar coleções de itens. Elas são **mutáveis**, ou seja, você pode adicionar, remover ou modificar elementos após a criação da lista. Os elementos de uma lista podem ser de qualquer tipo de dado, inclusive outras listas, criando estruturas de dados complexas.

**Como criar uma lista:**

```python
minha_lista = [1, 2, 3, "maçã", "banana", True]
```

* **Colchetes `[]`:** Delimitam os elementos da lista.
* **Elementos separados por vírgula:** Cada elemento ocupa uma posição na lista, começando do índice 0.

**Acessando elementos:**

```python
primeiro_elemento = minha_lista[0]  # Acessa o primeiro elemento (1)
ultimo_elemento = minha_lista[-1]  # Acessa o último elemento (True)
```

* **Índices:** Utilizados para acessar elementos específicos. Índices negativos contam a partir do final da lista.

**Modificando elementos:**

```python
minha_lista[2] = "laranja"  # Substitui o terceiro elemento
```

**Adicionando elementos:**

```python
minha_lista.append("uva")  # Adiciona ao final da lista
minha_lista.insert(1, "pera")  # Insere na posição 1
```

**Removendo elementos:**

```python
minha_lista.remove("maçã")  # Remove o primeiro elemento com o valor "maçã"
del minha_lista[0]  # Remove o elemento na posição 0
```

**Operações com listas:**

* **Concatenando listas:** `lista1 + lista2`
* **Repetindo listas:** `lista * 3`
* **Verificando a existência de um elemento:** `if "maçã" in minha_lista:`
* **Obtendo o tamanho da lista:** `len(minha_lista)`
* **Ordenando a lista:** `minha_lista.sort()` (modifica a lista original)
* **Invertendo a lista:** `minha_lista.reverse()` (modifica a lista original)

**Métodos úteis:**

* `count(x)`: Conta quantas vezes `x` aparece na lista.
* `index(x)`: Retorna o índice da primeira ocorrência de `x`.
* `pop(i)`: Remove e retorna o elemento na posição `i`.
* `clear()`: Remove todos os elementos da lista.

**Exemplo completo:**

```python
numeros = [1, 3, 5, 7]
frutas = ["maçã", "banana", "laranja"]

# Concatenando listas
lista_completa = numeros + frutas

# Adicionando um elemento
lista_completa.append("uva")

# Removendo um elemento
lista_completa.remove("maçã")

print(lista_completa)
```

**Listas aninhadas:**

Listas podem conter outras listas, criando estruturas de dados multidimensionais.

```python
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
```

**Por que usar listas?**

* **Flexibilidade:** Podem armazenar qualquer tipo de dado.
* **Facilidade de uso:** Sintaxe intuitiva e diversos métodos.
* **Versatilidade:** Utilizadas em diversas aplicações, como manipulação de dados, criação de jogos, etc.

## Tuplas em Python

**O que são tuplas?**

Tuplas são estruturas de dados em Python, muito semelhantes às listas, mas com uma diferença crucial: **são imutáveis**. Isso significa que, uma vez criada, uma tupla não pode ser modificada. Seus elementos não podem ser adicionados, removidos ou alterados.

**Por que usar tuplas?**

* **Proteção de dados:** Ao serem imutáveis, as tuplas garantem que os dados não serão alterados acidentalmente, o que pode ser útil em diversas situações, como para armazenar constantes ou como chaves em dicionários.
* **Eficiência:** As tuplas são geralmente mais eficientes em termos de memória do que as listas, especialmente quando se trata de dados que não precisam ser alterados.
* **Retornando múltiplos valores de funções:** Funções podem retornar tuplas para retornar múltiplos valores de uma só vez.

**Como criar uma tupla:**

```python
minha_tupla = (1, 2, 3, "maçã", "banana")
```

* **Parênteses:** Delimitam os elementos da tupla.
* **Elementos separados por vírgula:** Cada elemento ocupa uma posição na tupla.

**Acessando elementos:**

Assim como nas listas, você usa índices para acessar elementos de uma tupla.

```python
primeiro_elemento = minha_tupla[0]  # Acessa o primeiro elemento (1)
```

**Operações com tuplas:**

* **Concatenando tuplas:** `tupla1 + tupla2`
* **Repetindo tuplas:** `tupla * 3`
* **Verificando a existência de um elemento:** `if "maçã" in minha_tupla:`
* **Obtendo o tamanho da tupla:** `len(minha_tupla)`

**Métodos úteis:**

* **`count(x)`:** Conta quantas vezes `x` aparece na tupla.
* **`index(x)`:** Retorna o índice da primeira ocorrência de `x`.

**Diferenças entre listas e tuplas:**

| Característica | Listas | Tuplas |
|---|---|---|
| Mutabilidade | Mutáveis (podem ser modificadas) | Imutáveis (não podem ser modificadas) |
| Uso comum | Armazenar coleções de dados que podem mudar | Armazenar dados que não precisam ser alterados, como constantes ou para retornar múltiplos valores de funções |
| Sintaxe de criação | Colchetes `[]` | Parênteses `()` |

**Exemplo:**

```python
coordenadas = (3, 5)  # Uma tupla representando coordenadas (x, y)
nome, idade = ("Alice", 30)  # Desempacotamento de tupla

print(coordenadas)
print(nome, idade)
```

**Quando usar tuplas:**

* **Para representar dados imutáveis:** Como coordenadas, datas, cores, etc.
* **Como chaves em dicionários:** As chaves de um dicionário devem ser imutáveis, e tuplas são uma boa opção.
* **Para retornar múltiplos valores de funções:** Funções podem retornar tuplas para retornar vários valores de uma só vez.

**Em resumo:**

O uso de Tuplas em Python permite armazenar dados que não precisam ser alterados. Sua imutabilidade as torna seguras e eficientes em muitas situações.

## Conjuntos (Sets) em Python

**O que são conjuntos em Python?**

Conjuntos em Python são estruturas de dados que armazenam coleções de elementos **únicos e não ordenados**. Isso significa que um conjunto não pode conter elementos duplicados e a ordem dos elementos não é garantida. Os conjuntos são muito úteis para realizar operações matemáticas de conjuntos, como união, interseção e diferença.

**Como criar um conjunto:**

```python
meu_conjunto = {1, 2, 3, "maçã", "banana"}
```

* **Chaves `{}`:** Delimitam os elementos do conjunto.
* **Elementos separados por vírgula:** Cada elemento é único.

**Operações com conjuntos:**

* **Adicionar elementos:** `meu_conjunto.add("laranja")`
* **Remover elementos:** `meu_conjunto.remove("maçã")`
* **Verificar se um elemento está no conjunto:** `if "banana" in meu_conjunto:`
* **União de conjuntos:** `conjunto1.union(conjunto2)`
* **Interseção de conjuntos:** `conjunto1.intersection(conjunto2)`
* **Diferença de conjuntos:** `conjunto1.difference(conjunto2)`
* **Diferença simétrica:** `conjunto1.symmetric_difference(conjunto2)`

**Métodos úteis:**

* **`clear()`:** Remove todos os elementos do conjunto.
* **`copy()`:** Cria uma cópia do conjunto.
* **`pop()`:** Remove e retorna um elemento aleatório.

**Exemplo:**

```python
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

# União
uniao = conjunto_a.union(conjunto_b)  # {1, 2, 3, 4, 5, 6}

# Interseção
intersecao = conjunto_a.intersection(conjunto_b)  # {3, 4}

# Diferença
diferenca = conjunto_a.difference(conjunto_b)  # {1, 2}

print(uniao)
print(intersecao)
print(diferenca)
```

**Quando usar conjuntos:**

* **Remover duplicatas:** Conjuntos são perfeitos para eliminar elementos duplicados de uma lista.
* **Verificar se um elemento pertence a um conjunto:** Operações de pertinência são muito eficientes em conjuntos.
* **Realizar operações matemáticas de conjuntos:** União, interseção, diferença são operações comuns em conjuntos.
* **Implementar algoritmos:** Conjuntos são úteis em diversos algoritmos, como algoritmos de grafos e algoritmos de busca.

**Diferenças entre conjuntos e listas:**

| Característica | Conjuntos (sets) | Listas |
|---|---|---|
| Ordem dos elementos | Não ordenados | Ordenados |
| Elementos duplicados | Não permite | Permite |
| Mutabilidade | Mutáveis (podem ser modificados) | Mutáveis |
| Uso comum | Remover duplicatas, operações matemáticas de conjuntos | Armazenar sequências de elementos |

**Em resumo:**

Conjuntos são uma ferramenta poderosa em Python para trabalhar com coleções de elementos únicos. Sua simplicidade e eficiência os tornam ideais para diversas tarefas, desde a remoção de duplicatas até a implementação de algoritmos complexos.

## Dicionários em Python

**O que são dicionários em Python?**

Dicionários são estruturas de dados que armazenam pares chave-valor. Cada chave é única e é usada para acessar o valor correspondente. Dicionários são mutáveis, ou seja, você pode adicionar, remover ou modificar pares chave-valor após a criação do dicionário.

**Como criar um dicionario:**

```python
meu_dicionario = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}
```

* **Chaves `{}`:** Delimitam os pares chave-valor.
* **Chaves e valores separados por dois pontos:** A chave é um objeto imutável (como uma string, um número ou uma tupla) e o valor pode ser de qualquer tipo de dado.

**Acessando valores:**

```python
nome = meu_dicionario["nome"]  # Acessa o valor da chave "nome"
```

**Modificando valores:**

```python
meu_dicionario["idade"] = 31  # Altera o valor da chave "idade"
```

**Adicionando novos pares:**

```python
meu_dicionario["profissao"] = "Engenheira"
```

**Removendo pares:**

```python
del meu_dicionario["cidade"]
```

**Verificando se uma chave existe:**

```python
if "idade" in meu_dicionario:
    print("A chave 'idade' existe")
```

**Métodos úteis:**

* **`keys()`:** Retorna uma lista com todas as chaves.
* **`values()`:** Retorna uma lista com todos os valores.
* **`items()`:** Retorna uma lista de tuplas (chave, valor).
* **`get(chave, valor_padrao)`:** Retorna o valor da chave, ou um valor padrão se a chave não existir.

**Exemplo:**

```python
usuario = {"nome": "Bob", "email": "bob@example.com", "enderecos": ["Rua A", "Rua B"]}

print(usuario["nome"])  # Imprime "Bob"
print(usuario.get("telefone", "Não encontrado"))  # Imprime "Não encontrado"

for chave, valor in usuario.items():
    print(chave, valor)
```

**Quando usar dicionários:**

* **Armazenar dados relacionados:** Dicionários são ideais para armazenar informações relacionadas, como dados de um usuário, configurações de um programa, etc.
* **Implementar estruturas de dados mais complexas:** Dicionários podem ser usados para criar estruturas de dados mais complexas, como grafos e árvores.

**Diferenças entre dicionários e listas:**

| Característica | Dicionários | Listas |
|---|---|---|
| Acesso aos elementos | Através de chaves | Através de índices numéricos |
| Ordem dos elementos | Não ordenados | Ordenados |
| Duplicatas de chaves | Não permite | Permite duplicatas de valores |

**Em resumo:**

Dicionários são uma ferramenta poderosa em Python para armazenar e organizar dados. Sua flexibilidade e facilidade de uso os tornam uma estrutura de dados fundamental em muitas aplicações.

**Gostaria de explorar algum outro aspecto dos dicionários em Python?** Por exemplo, podemos aprofundar em:

* **Compreensão de dicionários:** Uma forma concisa de criar dicionários.
* **Aninhamento de dicionários:** Criando dicionários dentro de dicionários.
* **Métodos avançados:** `popitem`, `update`, etc.
* **Aplicações de dicionários:** Exemplos práticos de uso de dicionários.

**Qual tópico te interessa mais?**

