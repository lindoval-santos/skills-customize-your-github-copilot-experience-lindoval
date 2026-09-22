# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST simples com FastAPI, definindo rotas, modelos de dados e operações CRUD para manipular recursos em Python.

## 📝 Tarefas

### 🛠️ Configuração da Aplicação

#### Descrição
Crie uma aplicação FastAPI básica com uma rota inicial de boas-vindas e prepare a estrutura para trabalhar com uma lista de itens.

#### Requisitos
O programa concluído deve:

- Importar e inicializar `FastAPI`.
- Criar uma instância da aplicação com um nome descritivo.
- Adicionar uma rota `GET /` que retorne uma mensagem de boas-vindas.
- Preparar uma estrutura de dados em memória para armazenar itens.

### 🛠️ Implementação do CRUD

#### Descrição
Implemente operações para listar, criar, atualizar e excluir itens da API usando endpoints HTTP padrão.

#### Requisitos
O programa concluído deve:

- Criar uma rota `GET /items` para listar todos os itens.
- Criar uma rota `POST /items` para adicionar um novo item.
- Criar uma rota `GET /items/{item_id}` para consultar um item específico.
- Criar uma rota `PUT /items/{item_id}` para atualizar um item existente.
- Criar uma rota `DELETE /items/{item_id}` para remover um item.
- Retornar respostas JSON adequadas com status HTTP coerentes.

### 🛠️ Validação e Documentação

#### Descrição
Melhore a API com validação de dados e aproveite a documentação automática do FastAPI para testar os endpoints.

#### Requisitos
O programa concluído deve:

- Usar modelos de dados com `BaseModel` para validar entradas.
- Incluir pelo menos um campo obrigatório, como `title` ou `description`.
- Garantir que a documentação interativa da API esteja disponível no navegador.
- Incluir uma rota de exemplo que demonstre o uso do endpoint em um caso real.
