## Introdução do Protocolo HTTP

**O que é [HTTP](https://en.wikipedia.org/wiki/HTTP)?**

O Hypertext Transfer Protocol (HTTP) é o protocolo fundamental que permite a comunicação entre clientes (normalmente navegadores) e servidores na World Wide Web. É a base para a troca de informações na internet, como páginas web, imagens, vídeos e outros tipos de dados.

**Como funciona?**

* **[Modelo cliente-servidor](https://en.wikipedia.org/wiki/Client%E2%80%93server_model):** O cliente (navegador) envia uma requisição ao servidor, solicitando um recurso (ex: uma página web).
* **Requisições e respostas:** As requisições e respostas são trocadas em formato de texto, seguindo um padrão definido.
* **Métodos HTTP:** Existem diversos métodos, como GET (obter um recurso), POST (enviar dados para um servidor), PUT (atualizar um recurso), DELETE (excluir um recurso) e outros.
* **Códigos de status:** As respostas do servidor incluem um código de status que indica o resultado da requisição (ex: 200 OK, 404 Not Found).
* **Cabeçalhos:** Tanto as requisições quanto as respostas incluem cabeçalhos que fornecem informações adicionais, como o tipo de conteúdo, a data de modificação do recurso, etc.
* **Conexões persistentes:** O HTTP/1.1 introduziu conexões persistentes, permitindo que múltiplas requisições sejam feitas em uma única conexão, otimizando o desempenho.

**Histórico:**

* **HTTP/0.9 (1989):** Primeira versão, simples e com um único método (GET). By [T. Berners-Lee](https://en.wikipedia.org/wiki/Tim_Berners-Lee)
* **[HTTP/1.0](https://datatracker.ietf.org/doc/html/rfc1945) (1996):** Introduziu novos métodos (POST, HEAD) e suporte a diferentes tipos de conteúdo.
* **[HTTP/1.1](https://datatracker.ietf.org/doc/html/rfc9112) (2018):** Versão mais comum, com melhorias como conexões persistentes, pipelining e codificação de transferência em partes.
* **[HTTP/2](https://datatracker.ietf.org/doc/html/rfc9113) (2021):** Versão mais recente, com foco em desempenho e segurança.

**Componentes chave:**

* **Requisições:** Mensagens enviadas pelo cliente ao servidor.
* **Respostas:** Mensagens enviadas pelo servidor ao cliente.
* **Métodos HTTP:** Ações que podem ser realizadas em um recurso.
* **Códigos de status:** Indicam o resultado da requisição.
* **Cabeçalhos:** Fornecem informações adicionais sobre a requisição e resposta.
* **Corpo da mensagem:** Contém os dados da requisição ou resposta.

**Conceitos importantes:**

* **[Cookies](https://en.wikipedia.org/wiki/HTTP_cookie):** Pequenos arquivos armazenados no navegador para rastrear usuários e suas preferências.
* **[Sessões](https://en.wikipedia.org/wiki/Session_(computer_science)):** Mecanismo para manter o estado de um usuário entre múltiplas requisições.
* **[Cache](https://en.wikipedia.org/wiki/Cache_(computing)):** Armazenamento temporário de recursos para melhorar o desempenho.

**Em resumo:**

O HTTP é o [protocolo](https://en.wikipedia.org/wiki/Communication_protocol) que permite a comunicação entre clientes e servidores na [web](https://en.wikipedia.org/wiki/Web_content). Ele define as regras para as requisições e respostas, permitindo que navegadores e servidores se comuniquem de forma eficiente e segura. O entendimento do HTTP é fundamental para o desenvolvimento web e para a compreensão de como a internet funciona. Além disso, vale destacar a importância da [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web), uma rede interconectada de páginas web, que utiliza o HTTP para transmitir documentos [HTML](https://en.wikipedia.org/wiki/HTML) identificados por [URLs](https://en.wikipedia.org/wiki/URL) únicas, permitindo aos usuários acessar e navegar por informações globalmente.
