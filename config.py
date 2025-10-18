import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

class Config:
    # Chave secreta para segurança do Flask (lida do .env)
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Pega as credenciais do banco de dados do arquivo .env
    db_user = os.getenv('DATABASE_USER')
    db_pass = os.getenv('DATABASE_PASSWORD') # Garante que está pegando a senha
    db_host = os.getenv('DATABASE_HOST')     # O endereço do servidor MySQL (ex: '127.0.0.1')
    db_name = os.getenv('DATABASE_NAME')     # O nome exato do banco de dados

    # Validação básica para garantir que as variáveis foram carregadas
    if not all([db_user, db_pass, db_host, db_name]):
        print("Erro: Variáveis de banco de dados não encontradas no arquivo .env.")
        print("Verifique se o .env existe e contém DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, e DATABASE_NAME.")
        # Você pode querer lançar uma exceção aqui em um cenário real
        # raise ValueError("Configuração do banco de dados incompleta no .env")

    # Monta a string de conexão SQLAlchemy no formato correto para MySQL com PyMySQL
    # Formato: mysql+pymysql://<usuario>:<senha>@<host>/<nome_banco>
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}'

    # Desativa o rastreamento de modificações do SQLAlchemy (recomendado para performance)
    SQLALCHEMY_TRACK_MODIFICATIONS = False