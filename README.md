Sistema de Gerenciamento de Clientes do E-commerce
Este projeto é uma API RESTful desenvolvida em Python com o framework Flask para gerenciar o cadastro de clientes de um e-commerce. A aplicação segue o padrão de arquitetura MVC (Model-View-Controller) e utiliza um banco de dados SQLite para armazenamento de dados.

Funcionalidades
A API oferece as seguintes operações CRUD para o gerenciamento de clientes:

Contagem de Clientes:

GET /api/clientes/count: Retorna o número total de clientes cadastrados.

Listar Todos os Clientes:

GET /api/clientes/findAll: Retorna uma lista com todos os clientes.

Buscar Cliente por ID:

GET /api/clientes/findById/{id}: Retorna os dados de um cliente específico.

Buscar Clientes por Nome:

GET /api/clientes/findByName/{nome}: Retorna uma lista de clientes cujos nomes correspondem ao termo pesquisado.

Criar Cliente:

POST /api/clientes: Adiciona um novo cliente ao banco de dados.

Atualizar Cliente:

PUT /api/clientes/{id}: Atualiza os dados de um cliente existente.

Excluir Cliente:

DELETE /api/clientes/{id}: Remove um cliente do banco de dados.

Tecnologias Utilizadas
Python: Linguagem de programação principal.

Flask: Framework web para desenvolvimento da API.

Flask-SQLAlchemy: Biblioteca para integração com o banco de dados.

SQLite: Banco de dados para armazenamento local.

Postman: Ferramenta para testar os endpoints da API.

Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Contato
Autor: Evandro Galvão

Email: [seu-email@example.com]

GitHub: seu-usuario

Esse README fornece uma visão completa do projeto, desde a instalação até exemplos de uso e diagramas de arquitetura. Se precisar de mais detalhes ou ajustes, é só perguntar! 😊
