# API de Gerenciamento de Condomínios

Esta é uma API RESTful desenvolvida com Django e Django REST Framework para gerenciar informações de um condomínio, incluindo blocos, apartamentos e residentes. O principal objetivo da realização desse projeto foi colocar em prática o estudo realizado sobre APIs RESTful, caso tenha interesse, eu criei no Notion uma página detalhando a arquitetura REST, explicando seus príncipios, vantagens, entre outras coisas.

Link: https://www.notion.so/API-Rest-265bb6634ba980139030cbd7d3b9121e?source=copy_link

## Funcionalidades

- Autenticação de usuário via JWT (JSON Web Token).
- Operações CRUD (Criar, Ler, Atualizar, Deletar) para os seguintes recursos:
  - Blocos
  - Apartamentos
  - Residentes
- Cache implementado com Redis para otimizar o desempenho das consultas de listagem.
- Containerização com Docker facilitar o setup e o deploy.

## Tecnologias Utilizadas

- **Backend:**
  - Python 3.11
  - Django
  - Django REST Framework
  - Simple JWT for DRF
- **Banco de Dados:**
  - PostgreSQL
- **Cache:**
  - Redis
- **Containerização:**
  - Docker

## Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto em seu ambiente de desenvolvimento.

### Pré-requisitos

- Python 3.11+
- PostgreSQL
- Redis
- Git

### 1. Clone o repositório

```bash
git clone https://github.com/PedroLovatto99/condominios_api_restful.git
cd condominios_api_restful
```

### 2. Crie e ative um ambiente virtual

```bash
# Windows
py -m venv env
env\Scripts\activate

# Linux / macOS
python3 -m venv env
source env/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo chamado `.env` na raiz do projeto. Substitua os valores pelas suas credenciais.

```ini
DJANGO_SECRET_KEY="sua-chave-secreta-aqui"
DB_NAME=condominio_db
DB_USER=seu-usuario-postgres
DB_PASSWORD=sua-senha-postgres
DB_HOST=localhost
DB_PORT=5432
REDIS_HOST=localhost
```

### 5. Execute as migrações do banco de dados

```bash
python manage.py migrate
```

### 6. Crie um superusuário (para obter tokens)

```bash
python manage.py createsuperuser
```

### 7. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

A API estará disponível em `http://127.0.0.1:8000/`.

## Executando com Docker

Alternativamente, você pode executar o projeto usando Docker e Docker Compose.

### Pré-requisitos

- Docker

### 1. Configure o `.env`

Certifique-se de que seu arquivo `.env` está configurado. Ao usar Docker Compose, o `DB_HOST` deve ser o nome do serviço do banco de dados (ex: `db`) e `REDIS_HOST` deve ser `redis`.

### 2. Inicie os containers

Na raiz do projeto, execute o comando:

```bash
docker-compose up --build
```

A API estará disponível em `http://localhost:8000/`.

## Endpoints da API

Todas as rotas abaixo requerem autenticação. O token JWT deve ser enviado no cabeçalho `Authorization`.

`Authorization: Bearer <seu_token_de_acesso>`

Arquivo do postman com a estrutura de testes: [Baixar Coleção do Postman (JSON)](./Condominios_api.postman_collection.json)

### Autenticação

| Método | Endpoint  | Descrição                                                                                                                 |
| :----- | :-------- | :------------------------------------------------------------------------------------------------------------------------ |
| `POST` | `/token/` | Obtém um token de acesso e um de atualização. Corpo da requisição: `{"username": "seu_usuario", "password": "sua_senha"}` |

### Blocos

| Método   | Endpoint            | Descrição                                              |
| :------- | :------------------ | :----------------------------------------------------- | --- |
| `GET`    | `/api/blocos/`      | Lista todos os blocos (com cache).                     |
| `POST`   | `/api/blocos/`      | Cria um novo bloco.                                    |
| `GET`    | `/api/blocos/<id>/` | Detalha um bloco específico.                           |
| `PUT`    | `/api/blocos/<id>/` | Atualiza um bloco (necessário passar todos os campos). | .   |
| `PATCH`  | `/api/blocos/<id>/` | Atualiza um bloco.                                     |
| `DELETE` | `/api/blocos/<id>/` | Deleta um bloco.                                       |

### Apartamentos

| Método   | Endpoint                  | Descrição                                                    |
| :------- | :------------------------ | :----------------------------------------------------------- | --- |
| `GET`    | `/api/apartamentos/`      | Lista todos os apartamentos (com cache).                     |
| `POST`   | `/api/apartamentos/`      | Cria um novo apartamento.                                    |
| `GET`    | `/api/apartamentos/<id>/` | Detalha um apartamento específico.                           |
| `PUT`    | `/api/apartamentos/<id>/` | Atualiza um apartamento (necessário passar todos os campos). | .   |
| `PATCH`  | `/api/apartamentos/<id>/` | Atualiza um apartamento.                                     |
| `DELETE` | `/api/apartamentos/<id>/` | Deleta um apartamento.                                       |

### Residentes

| Método   | Endpoint                | Descrição                                                  |
| :------- | :---------------------- | :--------------------------------------------------------- |
| `GET`    | `/api/residentes/`      | Lista todos os residentes (com cache).                     |
| `POST`   | `/api/residentes/`      | Cria um novo residente.                                    |
| `GET`    | `/api/residentes/<id>/` | Detalha um residente específico.                           |
| `PUT`    | `/api/residentes/<id>/` | Atualiza um residente (necessário passar todos os campos). |
| `PATCH`  | `/api/residentes/<id>/` | Atualiza um residente.                                     |
| `DELETE` | `/api/residentes/<id>/` | Deleta um residente.                                       |
