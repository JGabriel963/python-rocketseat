# Python Rocketseat

Repositório de **estudos em Python**. Reúne vários projetos e exercícios feitos durante o aprendizado, cada um em sua própria pasta:

- `auth-jwt/` — autenticação com JWT, hash de senhas (bcrypt) e repositórios
- `mvc/` — projeto seguindo o padrão MVC
- `fastapi/` — estudos com FastAPI
- `flask/` e `flask-avançado/` — estudos com Flask
- `design_de_codigo/`, `solid/`, `POO/` — fundamentos de design de código, SOLID e POO
- `real-time/` — comunicação em tempo real
- `fundamentos/` — fundamentos da linguagem

## Pre-commit / Pylint

Existe um hook de `pre-commit` configurado na raiz do repositório que roda o **pylint**.

> **Importante:** o pylint está habilitado **apenas para o projeto `mvc/`**.

A configuração fica em `mvc/.pre-commit-config.yaml` e usa um filtro `files: ^mvc/`,
de modo que o hook **não** roda nos arquivos dos demais projetos. Assim, commits feitos
nas outras pastas (como `auth-jwt/`) não são bloqueados pelo lint.

Para o hook funcionar no `mvc/`, o `pylint` precisa estar disponível no ambiente
(instalado no venv usado para commitar).
