from projeto_mvc.models.db import obter_conexao

def listar_contribuicoes():
    conn = obter_conexao()
    cursor = conn.cursor()
    try:
        query = """
            SELECT A.idCONTRIBUICAO, A.VALOR, A.DATA, A.MEMBRO_idMEMBRO, B.NOME
            FROM contribuicao A
            INNER JOIN membro B ON B.idMEMBRO = A.MEMBRO_idMEMBRO
        """
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Erro ao listar contribuições: {str(e)}")
        return []
    finally:
        cursor.close()
        conn.close()

def listar_membros():
    conn = obter_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT idMEMBRO, NOME FROM membro")
        return cursor.fetchall()
    except Exception as e:
        print(f"Erro ao listar membros: {str(e)}")
        return []
    finally:
        cursor.close()
        conn.close()

def inserir_contribuicao(form):
    id_dizimista = form.get('id_dizimista')
    data = form.get('data')
    valor = form.get('valor')

    conn = obter_conexao()
    cursor = conn.cursor()
    try:
        comando = """
            INSERT INTO contribuicao (MEMBRO_idMEMBRO, DATA, VALOR)
            VALUES (%s, %s, %s)
        """
        cursor.execute(comando, (id_dizimista, data, valor))
        conn.commit()
        return True, "Contribuição registrada com sucesso!"
    except Exception as e:
        conn.rollback()
        return False, f"Erro ao inserir a contribuição: {str(e)}"
    finally:
        cursor.close()
        conn.close()
