# Flask / MongoDB

Projeto de integração entre o framework Flask e o banco NoSQL MongoDB

## Executando o projeto

Instruções para rodar o projeto em sua máquina.

### Pré-requisitos

* [Python 3.6](https://www.python.org/downloads/release/python-367/)
* [Pip3](https://pip.pypa.io/en/stable/installing/)
* [Virtualenv](https://virtualenv.pypa.io/en/stable/userguide/#usage)

### Instalação

Como deixar o projeto rodando em sua máquina.

Clone o projeto em sua máquina

```
git clone git@github.com:camiheleno/modalities.git
```

Acesse a pasta do projeto

```
cd ~/modalities
```

Crie a virtualenv

```
virtualenv -p python3 venv
```

Ative a venv

```
source venv/bin/activate
```

Instale as dependências do projeto

```
pip3 install -r requirements.txt
```

Exporte a variável de ambiente para o arquivo de configuração do ambiente que está executando o projeto

```
export APP_CONFIG_FILE=development.cfg
```

Rode a aplicação

```
flask run
```

Acesse a url
```
http://127.0.0.1:5000
```

### Url de Exemplo

```
http://127.0.0.1:5000/modalities?modalidade=PRESENCIAL&data_inicio=2014-02-20&data_fim=2015-10-01
```

## Documentação

http://127.0.0.1:5000/apidocs

## Built With

* [Python 3.6](https://www.python.org/downloads/release/python-367/) - Linguagem
* [Flask](http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application) - Framework
* [PyMongo](https://api.mongodb.com/python/current/tutorial.html) - Dependência para conexão com banco de dados
* [Flasgger](https://github.com/rochacbruno/flasgger) - Dependência para documentação da API


## Versionamento

Utilizado o [GIT](https://git-scm.com/) para o versionamento do projeto.

## Autores

* **Camilla Heleno** - [GIT](https://github.com/camiheleno)
