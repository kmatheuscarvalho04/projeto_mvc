from .db import obter_conexao

def listar_contribuicoes():
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT A.idCONTRIBUICAO, A.VALOR, A.DATA, A.MEMBRO_idMEMBRO, B.NOME 
        FROM contribuicao A 
        INNER JOIN membro B ON B.idMEMBRO = A.MEMBRO_idMEMBRO
    """)
    dados = cursor.fetchall()
    cursor.close()
    conn.close()
    return dados

def inserir_contribuicao(id_dizimista, data, valor):
    conn = obter_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO contribuicao (MEMBRO_idMEMBRO, DATA, VALOR) VALUES (%s, %s, %s)", (id_dizimista, data, valor))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()
