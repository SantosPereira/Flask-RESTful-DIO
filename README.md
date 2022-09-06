# API RESTful com Flask

<!-- Opções [Ativo,Em Pausa,Encerrado] -->
![Status de Desenvolvimento](https://img.shields.io/badge/Desenvolvimento-Ativo-success)
![Linha de código no projeto](https://img.shields.io/tokei/lines/github/santospereira/Flask-RESTful-DIO?label=Linhas%20de%20c%C3%B3digo&style=flat)
![Quantidade de linguagens usadas](https://img.shields.io/github/languages/count/santospereira/Flask-RESTful-DIO?label=Linguagens&color=f27830)
![Data do último commit](https://img.shields.io/github/last-commit/santospereira/Flask-RESTful-DIO?label=%C3%9Altimo%20commit)

<!-- ![Licença](https://img.shields.io/github/license/santospereira/Flask-RESTful-DIO) -->

Projeto utilizando o que aprendi no curso *"Desenvolvimento avançado
Python com Flask e REST
API"*.
O conceito desse projeto é ser o sistema de uma concessionária de carros, que serve as APIs utilizadas em seu sites e app comercial, e administração interna.

Saiba mais sobre o projeto aqui: [docs](/docs/Projeto.md)

## Indíce

- [API RESTful com Flask](#api-restful-com-flask)
  - [Indíce](#indíce)
  - [Tecnologias](#tecnologias)
  - [Instalação](#instalação)
  - [Executar](#executar)
  - [Testes](#testes)
  - [Autor](#autor)

## Tecnologias

- Python
- Flask
  - RESTful
  - HTTPauth
- Unittest
- SQLAlchemy
- SQLite
- MVC (Padrão de Projeto)
  
## Instalação

Para a instalação do projeto use a ferramenta de versionamento de projeto [*Git*](https://git-scm.com/), ou baixe um zip do projeto [*aqui*]().

Após ter o projeto em sua máquina, abra um terminal no diretório do projeto e execute os comandos abaixo:

~~~bash
source ./install.sh
~~~

Se encontrar erro ao executar a ativação no windows, pode ser necessário habilitar a execução de scripts no PowerShell, para isso utilize o comando:

~~~PowerShell
set-executionpolicy remotesigned
~~~

## Executar


~~~bash
python app.py
~~~

## Testes

Para executar os teste é necessário ter a app rodando, em seguida usar o comando a seguir

~~~bash
python -m unittest
~~~

## Autor

E-mail: [pedrohenriquelemam@gmail.com](mailto:pedrohenriquelemam@gmail.com)

[Voltar ao topo](#nomedoprojeto)