## Tuplas em Python

**O que são Tuplas?**

Tuplas são estruturas de dados em Python, muito semelhantes às listas, mas com uma característica fundamental: **são imutáveis**. Isso significa que, uma vez criada, uma tupla não pode ter seus elementos alterados, adicionados ou removidos.

**Criando Tuplas:**

Para criar uma tupla, basta colocar os elementos entre parênteses, separados por vírgulas:

```python
minha_tupla = (1, 2, 3, "Olá", True)
```

**Acessando Elementos:**

Assim como em listas, você acessa os elementos de uma tupla pelo índice:

```python
primeiro_elemento = minha_tupla[0]  # 1
```

**Imutabilidade:**

A principal diferença entre tuplas e listas é a imutabilidade. Tentar modificar um elemento de uma tupla resultará em um erro:

```python
minha_tupla[1] = "Mundo"  # Isso gerará um erro
```

**Por que usar Tuplas?**

* **Proteção de dados:** Ao serem imutáveis, tuplas ajudam a prevenir alterações acidentais em dados importantes.
* **Chaves de dicionários:** As chaves em dicionários devem ser imutáveis, e tuplas são uma ótima opção para isso.
* **Retorno de múltiplos valores:** Funções podem retornar múltiplos valores em uma tupla.
* **Eficiência:** Tuplas são geralmente mais eficientes em termos de memória do que listas, especialmente para dados que não precisam ser modificados.

**Operações com Tuplas:**

* **Concatenar:** Você pode concatenar duas tuplas para criar uma nova tupla.
* **Repetir:** Pode-se repetir uma tupla um número específico de vezes.
* **Slicing:** Assim como em listas, você pode extrair partes de uma tupla usando slicing.

**Métodos Úteis:**

* **count():** Conta o número de ocorrências de um elemento.
* **index():** Retorna o índice da primeira ocorrência de um elemento.

**Exemplo:**

```python
coordenadas = (10, 20)
nome, idade = ("Alice", 30)  # Desempacotamento de tupla
```

**Resumo:**

Tuplas são estruturas de dados imutáveis em Python, ideais para armazenar dados que não precisam ser modificados. Elas oferecem vantagens em termos de segurança e eficiência. A escolha entre listas e tuplas depende da necessidade de modificar os dados. Se os dados forem constantes, as tuplas são a melhor opção.

**Quando usar Tuplas e Listas?**

* **Tuplas:**
    * Dados que não precisam ser alterados.
    * Chaves de dicionários.
    * Retornar múltiplos valores de uma função.
* **Listas:**
    * Coleções de dados que precisam ser modificadas frequentemente.
    * Pilhas e filas.
