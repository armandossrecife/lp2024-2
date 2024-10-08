## Organizando e Manipulando Dados de Pessoas em Arquivo

### Introdução

Vamos mostrar como criar um programa em Python que permite cadastrar, listar e salvar informações de pessoas. Para isso, utilizaremos um dicionário para armazenar os dados e um arquivo texto para persistir as informações.

### Conceitos-chave

* **Dicionário:** Uma estrutura de dados em Python que armazena pares chave-valor. No nosso caso, o CPF será a chave e os dados da pessoa (nome e telefone) serão o valor.
* **Arquivo:** Um local de armazenamento de dados em um dispositivo. Neste exemplo, utilizaremos um arquivo texto para salvar as informações das pessoas.
* **Funções:** Blocos de código reutilizáveis que realizam tarefas específicas.

### Recomendações para o código

* **Criação do dicionário:** Inicializamos um dicionário vazio chamado `pessoas` para armazenar as informações das pessoas.

```python
# Crie um dicionario para armazenar as informacoes das pessoas
pessoas = {}
```

* **Função `ler_dados`:** Essa função solicita ao usuário o CPF, nome e telefone de uma pessoa e retorna esses dados em uma tupla.

```python
# ler os dados de uma pessoa
def ler_dados():
  # ...
```

* **Função `cadastrar_pessoa`:** Chama a função `ler_dados` para obter os dados da pessoa, e adiciona esses dados ao dicionário `pessoas`, usando o CPF como chave.

```python
# cadastrar uma pessoa
def cadastrar_pessoa():
  # ...
```

* **Função `listar_pessoas`:** Itera sobre o dicionário `pessoas` e imprime as informações de cada pessoa.

```python
# listar dados das pessoas cadastradas
def listar_pessoas():
  # ...
```

* **Função `salvar_dados`:** Abre o arquivo "pessoas.txt" no modo de escrita, itera sobre o dicionário `pessoas` e escreve cada registro em uma linha do arquivo, separando os campos por vírgulas.

```python
# Salva dados das pessoas em um arquivo
def salvar_dados(pessoas):
  # ...
```

* **Função `carregar_dados`:** Abre o arquivo "pessoas.txt" no modo de leitura, lê cada linha, separa os campos e adiciona as informações ao dicionário `pessoas`.

```python
# Carrega dados das pessoas de um arquivo
def carregar_dados(pessoas):
  # ...
```

### Como usar o programa

1. **Executar o código:** Execute o código Python.
2. **Carregar dados:** Chame a função `carregar_dados(pessoas)` para carregar as informações de um arquivo existente.
3. **Cadastrar pessoas:** Chame a função `cadastrar_pessoa()` para adicionar novas pessoas ao dicionário.
4. **Listar pessoas:** Chame a função `listar_pessoas()` para ver a lista de pessoas cadastradas.
5. **Salvar dados:** Chame a função `salvar_dados(pessoas)` para salvar as informações no arquivo "pessoas.txt".

### Explicando a estrutura de dados

O dicionário `pessoas` é uma estrutura de dados muito útil para armazenar informações de forma organizada. Cada chave do dicionário representa um CPF único, e o valor associado a essa chave é outro dicionário que contém as informações da pessoa (nome e telefone).

### Vantagens deste código

* **Organizado:** O código está dividido em funções bem definidas, facilitando a compreensão e a manutenção.
* **Reutilizável:** As funções podem ser reutilizadas em outros projetos.
* **Flexível:** É possível adicionar novas funcionalidades, como buscar pessoas por nome ou editar informações existentes.
* **Persistência:** Os dados são salvos em um arquivo, permitindo que o programa seja executado várias vezes sem perder as informações.

### Exercícios

* **Buscar pessoa:** Crie uma função para buscar uma pessoa pelo CPF.
* **Editar dados:** Crie uma função para editar os dados de uma pessoa.
* **Excluir pessoa:** Crie uma função para excluir uma pessoa do cadastro.
* **Validar dados:** Adicione validações para garantir que os dados inseridos pelo usuário sejam válidos (por exemplo, verificar se o CPF tem o formato correto).

## Atualizando o código com a biblioteca JSON

### Introdução à Biblioteca JSON

A biblioteca JSON em Python oferece uma maneira fácil de converter dados Python em formato JSON e vice-versa. Isso é especialmente útil para armazenar dados de forma estruturada em arquivos. O formato JSON é leve e legível, tornando-o uma excelente escolha para armazenar dados de forma persistente.

### Código Atualizado

```python
import json

def carregar_dados(arquivo):
    """Carrega dados de um arquivo JSON.

    Args:
        arquivo (str): Nome do arquivo JSON.

    Returns:
        dict: Dicionário com os dados carregados.
    """
    try:
        with open(arquivo, 'r') as f:
            dados = json.load(f)
    except FileNotFoundError:
        dados = {}
    return dados

def salvar_dados(dados, arquivo):
    """Salva dados em um arquivo JSON.

    Args:
        dados (dict): Dicionário com os dados a serem salvos.
        arquivo (str): Nome do arquivo JSON.
    """
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

# ... resto do código ...

# Carregar dados do arquivo JSON
pessoas = carregar_dados('pessoas.json')

# ... resto do código ...

# Salvar dados no arquivo JSON
salvar_dados(pessoas, 'pessoas.json')
```

### Explicação das Alterações

1. **Importação do módulo JSON:** A primeira linha importa o módulo `json`, que fornece as funções para trabalhar com dados JSON.
2. **Função `carregar_dados`:**
   * **Abertura do arquivo:** Abre o arquivo JSON no modo leitura.
   * **Carregamento dos dados:** Utiliza `json.load()` para carregar os dados do arquivo e convertê-los em um dicionário Python.
   * **Tratamento de erros:** Se o arquivo não existir, cria um dicionário vazio.
3. **Função `salvar_dados`:**
   * **Abertura do arquivo:** Abre o arquivo JSON no modo escrita.
   * **Salvamento dos dados:** Utiliza `json.dump()` para converter o dicionário Python em formato JSON e escrever no arquivo. O parâmetro `indent=4` formata o JSON com indentação para melhor legibilidade.

### Vantagens de Usar JSON

* **Facilidade de leitura:** O formato JSON é human-legível, facilitando a depuração e a visualização dos dados.
* **Estrutura:** Permite representar dados complexos, como listas e aninhados, de forma clara e organizada.
* **Suporte amplo:** É amplamente utilizado em diversas linguagens de programação e tecnologias.
* **Eficiência:** A biblioteca JSON do Python é otimizada para realizar a conversão entre Python e JSON de forma eficiente.

Com a utilização do JSON, você tem uma solução mais flexível e escalável para armazenar e manipular dados em seu programa.
