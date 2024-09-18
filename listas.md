## Listas em Python

**O que são Listas em Python?**

Listas são estruturas de dados extremamente versáteis em Python, utilizadas para armazenar coleções de itens. Esses itens podem ser de qualquer tipo de dado, como números, strings, booleanos e até mesmo outras listas, criando estruturas complexas.

**Criando Listas:**

Para criar uma lista, basta usar colchetes `[]` e separar os elementos por vírgulas:

```python
minha_lista = [1, 2, 3, "Olá", True]
```

**Acessando Elementos:**

Cada elemento em uma lista tem um índice, começando em 0. Para acessar um elemento específico, usamos o índice entre colchetes:

```python
primeiro_elemento = minha_lista[0]  # 1
ultimo_elemento = minha_lista[-1]  # True
```

**Modificando Listas:**

Listas são **mutáveis**, ou seja, você pode alterar seus elementos após a criação:

```python
minha_lista[1] = "Mundo"  # Substitui o segundo elemento
```

**Adicionando Elementos:**

* **append():** Adiciona um elemento ao final da lista.
* **insert():** Insere um elemento em uma posição específica.

```python
minha_lista.append(4)  # Adiciona 4 ao final
minha_lista.insert(2, "novo")  # Insere "novo" na posição 2
```

**Removendo Elementos:**

* **remove():** Remove o primeiro elemento com o valor especificado.
* **pop():** Remove e retorna o elemento em um índice específico.
* **del:** Remove um elemento por índice.

```python
minha_lista.remove("Olá")  # Remove a primeira ocorrência de "Olá"
ultimo_elemento = minha_lista.pop()  # Remove e retorna o último elemento
del minha_lista[0]  # Remove o primeiro elemento
```

**Slicing:**

Assim como em strings, você pode extrair partes de uma lista usando slicing:

```python
sublista = minha_lista[1:3]  # Cria uma nova lista com os elementos 1 e 2
```

**Iterando sobre Listas:**

Para percorrer cada elemento de uma lista, use um loop `for`:

```python
for item in minha_lista:
    print(item)
```

**Operações com Listas:**

* **Concatenação:** Junta duas listas usando o operador `+`.
* **Repetição:** Repete os elementos de uma lista um número especificado de vezes usando o operador `*`.
* **Verificação de Membro:** Use o operador `in` para verificar se um elemento está na lista.

**Métodos Úteis:**

* **len():** Retorna o número de elementos na lista.
* **count():** Conta o número de ocorrências de um elemento.
* **sort():** Ordena os elementos da lista.
* **reverse():** Inverte a ordem dos elementos.

**Exemplo Completo:**

```python
numeros = [3, 1, 4, 1, 5, 9]
numeros.sort()  # Ordena a lista
print(numeros.count(1))  # Conta quantos 1s existem
```

**Em resumo:**

Listas são estruturas de dados extremamente versáteis em Python, permitindo você armazenar e manipular coleções de dados de forma eficiente. Com o conhecimento das operações básicas e dos métodos disponíveis, você poderá explorar todo o potencial das listas em seus projetos.
