# API RESTful com Flask

![Badge](https://img.shields.io/badge/Desenvolvimento-ativo-brightgreen)

Projeto utilizando o que aprendi no curso *"Desenvolvimento avançado
Python com Flask e REST
API"*.
O conceito desse projeto é ser o sistema de uma concessionária de carros, que serve as APIs utilizadas em seu sites e app comercial, e administração interna.

Saiba mais sobre o projeto aqui: [docs](/docs/Projeto.md)

## Tecnologias

- Python
- Flask
  - RESTful
  - HTTPauth
- SQLAlchemy
- SQLite
- MVC (Padrão de Projeto)
  
## Instalação

Para a instalação do projeto use a ferramenta de versionamento de projeto [*Git*](https://git-scm.com/), ou baixe um zip do projeto [*aqui*]().

Após ter o projeto em sua máquina, abra um terminal no diretório do projeto e execute os comandos abaixo:

~~~bash
# Criação do ambiente virtual
$ python -m venv env

# Ativação do ambiente:
# Windows
$ .\/env/Scripts/Activate.ps1

# Linux/Mac
$ source ./env/Scripts/activate

# Instalação das dependências do projeto
$ pip install -r requirements.txt
~~~

Se encontrar erro ao executar a ativação no windows, pode ser necessário habilitar a execução de scripts no PowerShell, para isso utilize o comando:

~~~PowerShell
set-executionpolicy remotesigned
~~~

## Autor

E-mail: [pedrohenriquelemam@gmail.com](mailto:pedrohenriquelemam@gmail.com)
