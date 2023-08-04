## Rodando a aplicação
### Docker
Você precisa ter o [Docker](https://docs.docker.com/engine/install/) e [Docker Compose](https://docs.docker.com/compose/install/) instalado.

#### Iniciando a aplicação
```
docker-compose up --build resh
```

Após iniciado o container, a aplicação estará disponível em `http://localhost:8000`.

#### Resetando o banco de dados e toda a aplicação
Caso queira deletar o banco de dados e resetar a aplicação para o seu estado inicial.

```
docker-compose down
docker-compose rm
docker volume rm reshdb
```

### Virtualenv
Para questões de desenvolvimento, é possivel rodar a aplicação utilizando o virtualenv. Para isso você primeiro precisa iniciar a instância do banco de dados utilizando o Docker Compose e depois inicializar a aplicação no virtualenv.

#### Criando um virtulenv
```
virtualenv -p python3 venv
```

#### Se estiver utilizando o Windows
```
python -m venv venv
```

#### Iniciando o banco de dados e aplicação
```
docker-compose up -d database
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py runserver
```

#### Se estiver utilizando o Windows
```
docker-compose up -d database
source venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

## Rodando testes
```
pip install -r requirements.txt
pytest -n auto
```