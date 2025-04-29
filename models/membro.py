from .db import obter_conexao

def listar_membros():
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT idMEMBRO, RI, CARGO, NOME, TELEFONE FROM membro")
    dados = cursor.fetchall()
    cursor.close()
    conn.close()
    return dados

def inserir_membro(cargo, nome, ri, telefone):
    conn = obter_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO membro (CARGO, NOME, RI, TELEFONE) VALUES (%s, %s, %s, %s)", (cargo, nome, ri, telefone))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def deletar_membro(idMEMBRO, ri):
    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM membro WHERE ID = %s OR RI =%s" ,(idMEMBRO, ri))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()
# outros: deletar_membro, atualizar_membro...
