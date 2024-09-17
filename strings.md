## Strings em Python

**O que são Strings?**

Em Python, strings são sequências de caracteres, ou seja, são usadas para representar texto. Elas podem conter letras, números, símbolos e espaços. As strings são delimitadas por aspas simples (') ou duplas ("). 

**Criando Strings:**

```python
# Usando aspas simples
nome = 'João da Silva'

# Usando aspas duplas (útil para strings com apóstrofes)
frase = "Ele disse: 'Olá, mundo!'"
```

**Acessando Caracteres:**

As strings são indexadas, ou seja, cada caractere tem uma posição específica, começando em 0. Você pode acessar um caractere específico usando colchetes:

```python
nome = "Python"
primeiro_caractere = nome[0]  # 'P'
ultimo_caractere = nome[-1]  # 'n'
```

**Slicing:**

Para extrair uma parte de uma string, usamos o slicing:

```python
frase = "Linguagem de programação"
palavra = frase[9:18]  # 'programação'
```

**Imutabilidade:**

As strings em Python são imutáveis. Isso significa que você não pode modificar um caractere individual de uma string. Se precisar alterar uma string, você precisa criar uma nova string.

**Operações com Strings:**

* **Concatenção:** Junta duas ou mais strings usando o operador `+`.
* **Repetição:** Repete uma string um número específico de vezes usando o operador `*`.
* **Métodos:** As strings possuem diversos métodos para manipulação de texto, como `upper()`, `lower()`, `find()`, `replace()`, `split()`, entre outros.

**Exemplo:**

```python
frase = "Olá, mundo!"
print(frase.upper())  # OLÁ, MUNDO!
print(frase.find("mundo"))  # 7
nova_frase = frase.replace("mundo", "Python")  # Olá, Python!
```

**Formatação de Strings:**

* **f-strings:** Uma forma concisa e poderosa de formatar strings, inserindo valores de variáveis diretamente no texto.

```python
nome = "Alice"
idade = 30
mensagem = f"Meu nome é {nome} e tenho {idade} anos."
```

**Iterando sobre Strings:**

Você pode percorrer cada caractere de uma string usando um loop `for`:

```python
for letra in "Python":
    print(letra)
```

**Convertendo para String:**

Para converter outros tipos de dados em strings, use a função `str()`.

### Principais métodos prontos

## Exemplos dos Métodos de String em Python

Com certeza! Vamos explorar cada um desses métodos com exemplos práticos:

### upper()
Converte todos os caracteres da string para maiúsculas.

```python
texto = "Olá, mundo!"
texto_maiúsculo = texto.upper()
print(texto_maiúsculo)  # Saída: OLÁ, MUNDO!
```

### lower()
Converte todos os caracteres da string para minúsculas.

```python
texto = "PYTHON É LEGAL!"
texto_minúsculo = texto.lower()
print(texto_minúsculo)  # Saída: python é legal!
```

### find()
Retorna o índice da primeira ocorrência de uma substring dentro da string. Se a substring não for encontrada, retorna -1.

```python
frase = "A linguagem Python é muito poderosa."
indice_python = frase.find("Python")
print(indice_python)  # Saída: 10 (pois "Python" começa na posição 10)
```

### replace()
Substitui todas as ocorrências de uma substring por outra.

```python
texto = "Eu gosto de maçã."
novo_texto = texto.replace("maçã", "banana")
print(novo_texto)  # Saída: Eu gosto de banana.
```

### split()
Divide a string em uma lista de substrings, utilizando um delimitador especificado. Se nenhum delimitador for especificado, divide a string por espaços em branco.

```python
frase = "Olá, mundo! Como vai?"
palavras = frase.split()
print(palavras)  # Saída: ['Olá,', 'mundo!', 'Como', 'vai?']

# Com delimitador personalizado
email = "usuario@example.com"
usuario, dominio = email.split('@')
print(usuario)  # Saída: usuario
print(dominio)  # Saída: example.com
```

### Outros métodos úteis:

* **strip():** Remove caracteres em branco do início e do final da string.
* **startswith() e endswith():** Verificam se a string começa ou termina com uma determinada substring.
* **count():** Conta o número de ocorrências de uma substring dentro da string.
* **join():** Junta os elementos de uma lista em uma única string, utilizando um delimitador especificado.

```python
texto = "  Olá, mundo!  "
texto_sem_espacos = texto.strip()  # Remove espaços em branco
print(texto_sem_espacos)  # Saída: Olá, mundo!

palavras = ["Python", "é", "legal"]
frase = " ".join(palavras)  # Junta as palavras com espaços
print(frase)  # Saída: Python é legal
```

**Observação:** Os métodos de string não modificam a string original. Eles retornam uma nova string com as alterações.

**Exemplo completo:**

```python
texto = "  Olá, mundo! Python é divertido.   "

# Limpa os espaços em branco
texto_limpo = texto.strip()

# Converte para maiúsculas
texto_maiúsculo = texto_limpo.upper()

# Divide em palavras
palavras = texto_maiúsculo.split()

# Conta quantas vezes a palavra "PYTHON" aparece
num_python = palavras.count("PYTHON")

print(num_python)  # Saída: 2
```

**Resumo:**

As strings são um tipo de dado fundamental em Python, utilizado para representar texto. Elas oferecem diversas funcionalidades para manipulação e formatação de texto, tornando-as uma ferramenta essencial para a programação.
