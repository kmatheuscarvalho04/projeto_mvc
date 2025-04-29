import mysql.connector
from config import DB_CONFIG

def obter_conexao():
    return mysql.connector.connect(**DB_CONFIG)