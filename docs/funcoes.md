## Funções em Python: Blocos Reutilizáveis de Código

**O que são Funções em Python?**

Em Python, funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas permitem organizar o código, torná-lo mais legível e evitar a repetição de código.

**Por que usar funções?**

* **Reutilização:** Uma vez definida, uma função pode ser chamada várias vezes em diferentes partes do seu programa.
* **Modularidade:** Dividir o código em funções menores torna o programa mais fácil de entender e manter.
* **Abstração:** As funções podem ocultar a complexidade interna, permitindo que você se concentre na lógica geral do programa.

**Como definir uma função:**

Para definir uma função em Python, utilizamos a palavra-chave `def`, seguida do nome da função e dos parâmetros entre parênteses. O corpo da função é indentado:

```python
def saudacao(nome):
  print("Olá,", nome + "!")
```

**Chamando uma função:**

Para executar uma função, basta escrever o nome da função seguido dos argumentos entre parênteses:

```python
saudacao("Maria")  # Saída: Olá, Maria!
```

**Parâmetros e Argumentos:**

* **Parâmetros:** São as variáveis declaradas na definição da função.
* **Argumentos:** São os valores passados para a função quando ela é chamada.

**Retorno de valores:**

Uma função pode retornar um valor usando a palavra-chave `return`:

```python
def soma(a, b):
  return a + b

resultado = soma(3, 5)  # resultado será 8
```

**Tipos de argumentos:**

* **Argumentos posicionais:** A ordem dos argumentos importa.
* **Argumentos nomeados:** Você pode especificar o nome do parâmetro ao passar o argumento.
* **Argumentos com valores padrão:** Você pode definir um valor padrão para um parâmetro.

**Funções anônimas (lambda):**

Funções lambda são funções pequenas e anônimas, definidas em uma única linha. São úteis para operações simples.

```python
dobro = lambda x: x * 2
```

```bash
print(dobro(4))
8
```

**Docstrings:**

Docstrings são strings que descrevem o que uma função faz. Elas são muito importantes para a documentação do código.

```python
def fatorial(n):
  """Calcula o fatorial de um número."""
  if n == 0:
    return 1
  else:
    return n * fatorial(n-1)
```

**Em resumo:**

As funções são um conceito fundamental na programação em Python. Elas permitem organizar o código, torná-lo mais reutilizável e facilitar a manutenção. Ao dominar as funções, você estará dando um grande passo para se tornar um programador Python mais eficiente.

## Funções Recursivas em Python

**O que são Funções Recursivas?**

Uma função recursiva é aquela que, durante sua execução, chama a si mesma. Essa técnica é útil para resolver problemas que podem ser divididos em subproblemas menores e idênticos ao problema original.

**Como funcionam:**

1. **Caso base:** É a condição que interrompe a recursão. Quando essa condição é alcançada, a função não se chama mais a si mesma.
2. **Caso recursivo:** É a parte da função que chama a si mesma, mas com um argumento menor ou mais próximo do caso base.

**Exemplo: Fatorial**

O fatorial de um número natural n é o produto de todos os números naturais de 1 até n. Podemos calcular o fatorial de forma recursiva:

```python
def fatorial(n):
  if n == 0:  # Caso base
    return 1
  else:  # Caso recursivo
    return n * fatorial(n-1)

resultado = fatorial(5)
print(resultado)  # Saída: 120
```

**Explicação:**

* **Caso base:** Se n for 0, o fatorial é 1.
* **Caso recursivo:** Se n for diferente de 0, o fatorial de n é n multiplicado pelo fatorial de n-1.

**Visualizando a recursão:**

Para entender melhor como a recursão funciona, imagine uma árvore:

```
fatorial(5)
  |
  5 * fatorial(4)
    |
    4 * fatorial(3)
      |
      ...
```

A função chama a si mesma várias vezes até chegar ao caso base (fatorial(0)).

**Outro exemplo: Fibonacci**

A sequência de Fibonacci é definida por:
* fib(0) = 0
* fib(1) = 1
* fib(n) = fib(n-1) + fib(n-2) para n > 1

```python
def fibonacci(n):
  if n == 0 or n == 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

resultado = fibonacci(5)
print(resultado)  # Saída: 5
```

**Quando usar recursão?**

* **Problemas divisíveis em subproblemas menores:** Problemas como cálculo de fatorial, torre de Hanoi, busca binária.
* **Estruturas de dados recursivas:** Árvores, listas encadeadas.
* **Linguagens formais:** Análise de gramáticas.

**Cuidado com a recursão:**

* **Consumo de memória:** Cada chamada recursiva consome memória para armazenar o estado da função.
* **Desempenho:** Em alguns casos, a recursão pode ser menos eficiente do que um loop.

**Quando evitar a recursão:**

* **Problemas que podem ser resolvidos com loops:** Em geral, loops são mais eficientes que recursão.
* **Problemas que exigem muita profundidade de recursão:** Pode causar estouro de pilha.

**Conclusão:**

A recursão é uma ferramenta poderosa para resolver problemas complexos, mas deve ser usada com cuidado. Ao entender os conceitos de caso base e caso recursivo, você poderá aplicar a recursão em diversas situações.

## Escopo de Variáveis em Python: Local e Global

O escopo de uma variável define onde ela pode ser acessada dentro de um programa Python. Em outras palavras, determina a visibilidade de uma variável em diferentes partes do seu código.

### Variáveis Locais

* **Onde são definidas:** Dentro de uma função.
* **Visibilidade:** Somente dentro da função onde foram definidas.
* **Exemplo:**
  ```python
  def minha_funcao():
      x = 10  # x é uma variável local
      print(x)

  minha_funcao()  # Imprime 10
  print(x)  # Erro: x não está definida fora da função
  ```

### Variáveis Globais

* **Onde são definidas:** Fora de qualquer função.
* **Visibilidade:** Podem ser acessadas de qualquer lugar do programa.
* **Exemplo:**
  ```python
  x = 20  # x é uma variável global

  def minha_funcao():
      print(x)

  minha_funcao()  # Imprime 20
  print(x)  # Imprime 20
  ```

### Por que o escopo é importante?

* **Evita conflitos de nomes:** Variáveis com o mesmo nome podem existir em diferentes escopos sem causar problemas.
* **Organização do código:** Ajuda a manter o código mais organizado e fácil de entender.
* **Proteção de dados:** Variáveis locais são protegidas de alterações acidentais por outras partes do código.

### Modificando variáveis globais dentro de funções

Para modificar uma variável global dentro de uma função, você precisa usar a palavra-chave `global`:

```python
x = 10

def minha_funcao():
  global x
  x = 20

minha_funcao()
print(x)  # Imprime 20
```

**Atenção:** O uso excessivo de variáveis globais pode tornar o código mais difícil de entender e depurar. É geralmente recomendado usar variáveis locais e passar dados entre funções através de argumentos e valores de retorno.

### Escopo LEGB (Local, Enclosing, Global, Built-in)

Python segue a regra LEGB para determinar o escopo de uma variável:

* **Local:** Dentro da função atual.
* **Enclosing:** Dentro de funções aninhadas (não vamos aprofundar aqui).
* **Global:** No módulo atual.
* **Built-in:** Nomes predefinidos em Python (como `print`, `len`, etc.).

**Exemplo com escopo aninhado:**

```python
x = "global"

def outer():
  x = "outer"
  def inner():
    x = "inner"
    print(x)  # Imprime "inner"
  inner()
  print(x)  # Imprime "outer"

outer()
print(x)  # Imprime "global"
```

**Em resumo:**

O escopo de uma variável determina onde ela pode ser acessada em seu código Python. Entender os conceitos de escopo local e global é fundamental para escrever código Python limpo, organizado e livre de erros.

## Passagem de Argumentos por Valor e por Referência em Python

Quando chamamos uma função em Python, passamos valores para ela como argumentos. A forma como esses valores são tratados dentro da função depende do mecanismo de passagem de argumentos. Existem dois principais mecanismos: por valor e por referência.

### Passagem por Valor

* **O que acontece:** Ao passar um argumento por valor, uma cópia do valor é criada e passada para a função. Qualquer modificação feita à cópia dentro da função não afeta o valor original.
* **Tipos imutáveis:** Em Python, tipos imutáveis como números, strings e tuplas são sempre passados por valor.
* **Exemplo:**

```python
def dobrar_numero(x):
    x = x * 2
    print("Dentro da função:", x)

numero = 5
dobrar_numero(numero)
print("Fora da função:", numero)  # Imprime 5
```

* **Explicação:** Quando passamos `numero` para a função, uma cópia do valor 5 é criada dentro da função. A multiplicação por 2 modifica apenas essa cópia. O valor original de `numero` permanece inalterado.

### Passagem por Referência

* **O que acontece:** Ao passar um argumento por referência, é passada a referência (endereço de memória) do objeto para a função. Se a função modificar o objeto, a modificação será refletida no objeto original.
* **Tipos mutáveis:** Listas, dicionários e conjuntos são tipos mutáveis em Python e são passados por referência.
* **Exemplo:**

```python
def adicionar_elemento(minha_lista):
    minha_lista.append(4)

minha_lista = [1, 2, 3]
adicionar_elemento(minha_lista)
print(minha_lista)  # Imprime [1, 2, 3, 4]
```

* **Explicação:** Quando passamos `minha_lista` para a função, a referência para a lista é passada. Ao adicionar um elemento à lista dentro da função, estamos modificando a lista original, pois ambas as variáveis (dentro e fora da função) apontam para o mesmo objeto na memória.

### Resumindo

* **Tipos imutáveis:** Sempre são passados por valor.
* **Tipos mutáveis:** Sempre são passados por referência.

**Por que isso importa?**

* **Previsibilidade:** Entender a diferença entre passagem por valor e por referência é crucial para prever o comportamento do seu código e evitar bugs.
* **Eficiência:** Em alguns casos, pode ser mais eficiente passar objetos grandes por referência para evitar a criação de cópias.
* **Modificação de dados:** Se você precisa modificar um objeto dentro de uma função, é importante saber se ele será passado por valor ou por referência.

**Observações:**

* **Cópias rasas e profundas:** Para tipos compostos como listas e dicionários, a passagem por referência cria uma cópia rasa. Isso significa que os elementos de nível superior são referenciados, mas os elementos aninhados ainda são compartilhados. Para criar uma cópia completa, você pode usar métodos como `copy()` ou `deepcopy()`.
* **Funções puras:** Funções puras não modificam os argumentos passados e retornam um novo valor. Elas são geralmente preferíveis por serem mais previsíveis e fáceis de testar.

Ao entender esses conceitos, você poderá escrever código Python mais eficiente e seguro.





