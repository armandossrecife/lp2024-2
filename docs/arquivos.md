## Manipulando Sistema de Arquivos em Python

**Como manipular um sistema de arquivos usando Python?**

O sistema de arquivos em Python oferece um conjunto de ferramentas para interagir com o sistema operacional, permitindo que você crie, leia, escreva, renomeie, exclua e gerencie arquivos e diretórios. Essas funcionalidades são essenciais para qualquer aplicação que precise lidar com dados armazenados em disco.

**Módulos Principais:**

* **`os`:** Fornece funções para interagir com o sistema operacional de forma mais baixa.
* **`shutil`:** Oferece funções de alto nível para copiar, mover e remover arquivos e diretórios.
* **`pathlib`:** Uma interface mais moderna e orientada a objetos para trabalhar com caminhos de arquivos.

**Operações Comuns:**

* **Criar arquivos:**
  ```python
  with open("meu_arquivo.txt", "w") as arquivo:
      arquivo.write("Hello, world!")
  ```
* **Ler arquivos:**
  ```python
  with open("meu_arquivo.txt", "r") as arquivo:
      conteudo = arquivo.read()
      print(conteudo)
  ```
* **Obter informações sobre arquivos:**
  ```python
  import os
  import time

  arquivo = "meu_arquivo.txt"
  tamanho = os.path.getsize(arquivo)
  modificado = time.ctime(os.path.getmtime(arquivo))
  print(tamanho, modificado)
  ```
* **Listar arquivos em um diretório:**
  ```python
  import os

  for arquivo in os.listdir("."):
      print(arquivo)
  ```
* **Criar diretórios:**
  ```python
  import os

  os.mkdir("nova_pasta")
  ```
* **Renomear arquivos:**
  ```python
  import os

  os.rename("arquivo_antigo.txt", "novo_arquivo.txt")
  ```
* **Excluir arquivos:**
  ```python
  import os

  os.remove("arquivo_a_ser_excluido.txt")
  ```
* **Copiar arquivos:**
  ```python
  import shutil

  shutil.copy("arquivo_original.txt", "copia_do_arquivo.txt")
  ```
* **Mover arquivos:**
  ```python
  import shutil

  shutil.move("arquivo.txt", "nova_pasta")
  ```

**Conceitos Importantes:**

* **Caminhos absolutos e relativos:** Caminhos absolutos especificam a localização completa de um arquivo a partir da raiz do sistema de arquivos, enquanto caminhos relativos são especificados em relação ao diretório atual.
* **Modos de abertura de arquivos:** "r" para leitura, "w" para escrita (sobrescreve), "a" para append (adiciona ao final), "x" para criar um arquivo exclusivo, "b" para modo binário.
* **Gerenciamento de exceções:** É importante usar `try-except` para lidar com erros que podem ocorrer durante operações com arquivos, como arquivos não encontrados ou permissões insuficientes.

**Módulo `pathlib` (Python 3.4+):**

* **Objetos Path:** Representam caminhos de arquivos de forma mais intuitiva e orientada a objetos.
* **Operações:** Criar, remover, listar, ler, escrever, etc.
* **Métodos:** `exists()`, `is_dir()`, `is_file()`, `read_text()`, `write_text()`, etc.

**Exemplo com `pathlib`:**

```python
from pathlib import Path

caminho = Path("minha_pasta")
caminho.mkdir(exist_ok=True)  # Cria a pasta se não existir

arquivo = caminho / "meu_arquivo.txt"
arquivo.touch(exist_ok=True)  # Cria o arquivo se não existir

with arquivo.open("w") as f:
    f.write("Conteúdo do arquivo")
```

**Em resumo:**

O sistema de arquivos em Python oferece uma interface poderosa para interagir com o sistema operacional e gerenciar arquivos e diretórios. Ao dominar esses conceitos, você poderá criar aplicações que leem e escrevem dados em disco, automatizam tarefas e muito mais.

## Gerenciamento de Erros em Arquivos em Python

**Por que é importante gerenciar erros em arquivos?**

Ao trabalhar com arquivos, é comum encontrar diversos tipos de erros, como:

* **Arquivos não encontrados:** O arquivo especificado não existe.
* **Permissões insuficientes:** O programa não tem permissão para ler ou escrever no arquivo.
* **Erros de I/O:** Problemas com o dispositivo de armazenamento.
* **Formatos de arquivo inválidos:** O arquivo não está no formato esperado.

**Como lidar com exceções?**

A forma mais comum de lidar com exceções em Python é utilizando o bloco `try-except`:

```python
try:
    with open('meu_arquivo.txt', 'r') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado.")
except PermissionError:
    print("Você não tem permissão para acessar este arquivo.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
```

* **`try`:** Envolve o código que pode gerar exceções.
* **`except`:** Especifica os tipos de exceções que você deseja capturar e o código a ser executado caso a exceção ocorra.
* **`Exception`:** Captura qualquer tipo de exceção não especificada anteriormente.

**Exceções comuns:**

* **`FileNotFoundError`:** Lançada quando um arquivo não é encontrado.
* **`PermissionError`:** Lançada quando não há permissão para acessar um arquivo.
* **`IOError`:** Lançada para erros de entrada/saída gerais.

**Outras técnicas:**

* **`finally`:** Garante que um bloco de código seja executado, independentemente de ocorrer uma exceção ou não. É útil para fechar arquivos ou liberar recursos.
* **`raise`:** Lança uma exceção manualmente.
* **`assert`:** Verifica uma condição e lança uma `AssertionError` se a condição for falsa.

**Exemplo com `finally`:**

```python
try:
    with open('meu_arquivo.txt', 'r') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado.")
finally:
    print("Bloco finally sempre executado.")
```

**Boas práticas:**

* **Seja específico:** Capture apenas as exceções que você espera e sabe como lidar.
* **Use `finally` para limpeza:** Feche arquivos, libere recursos, etc.
* **Crie suas próprias exceções:** Para indicar erros específicos em sua aplicação.
* **Documente suas exceções:** Inclua mensagens claras e informativas.

**Gerenciando diferentes tipos de erros:**

```python
try:
    # Código que pode gerar diversos tipos de erros
except FileNotFoundError:
    print("Arquivo não encontrado.")
except PermissionError:
    print("Permissão negada.")
except ValueError:
    print("Erro de valor.")
except Exception as e:
    print(f"Erro inesperado: {e}")
```

**Conclusão:**

O gerenciamento de erros em arquivos é fundamental para criar programas robustos e confiáveis. Ao utilizar o bloco `try-except` e as técnicas apresentadas, você pode lidar com diversas situações inesperadas e evitar que seu programa pare de funcionar de forma abrupta.
