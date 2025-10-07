# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Aprender a criar uma API REST simples utilizando o framework FastAPI em Python. O estudante irá construir endpoints para manipular dados de uma lista de tarefas (to-do list).

## 📝 Tasks

### 🛠️ Criar Estrutura Básica da API

#### Description
Crie um arquivo Python chamado `main.py` que inicializa uma aplicação FastAPI e define um endpoint raiz (`/`) que retorna uma mensagem de boas-vindas.

#### Requirements
Completed program should:

- Inicializar uma aplicação FastAPI
- Definir um endpoint GET `/` que retorna um JSON com uma mensagem de boas-vindas
- Rodar localmente usando `uvicorn`


### 🛠️ Endpoints para Gerenciar Tarefas

#### Description
Implemente endpoints para criar, listar e remover tarefas de uma lista em memória.

#### Requirements
Completed program should:

- Definir um endpoint GET `/tasks` que retorna todas as tarefas
- Definir um endpoint POST `/tasks` para adicionar uma nova tarefa (recebe JSON com campo `title`)
- Definir um endpoint DELETE `/tasks/{task_id}` para remover uma tarefa pelo índice
- Utilizar uma lista Python em memória para armazenar as tarefas
