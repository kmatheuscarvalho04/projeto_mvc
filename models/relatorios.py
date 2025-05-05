from projeto_mvc.models.db import obter_conexao

def relatorio_sintetico(data_inicio, data_fim):
    conn = obter_conexao()
    cursor = conn.cursor()
    try:
        consulta = """
            SELECT DISTINCT NOME, CARGO, RI
            FROM contribuicao A
            INNER JOIN membro B ON A.MEMBRO_idMEMBRO = B.idMEMBRO
            WHERE A.DATA BETWEEN %s AND %s
            ORDER BY CARGO DESC
        """
        cursor.execute(consulta, (data_inicio, data_fim))
        return cursor.fetchall()
    except Exception as e:
        print(f"Erro no relatório sintético: {str(e)}")
        return []
    finally:
        cursor.close()
        conn.close()

def relatorio_analitico(data_inicio, data_fim):
    conn = obter_conexao()
    cursor = conn.cursor()
    try:
        consulta = """
            SELECT A.DATA, B.CARGO, B.NOME, A.VALOR, B.RI
            FROM contribuicao A
            INNER JOIN membro B ON A.MEMBRO_idMEMBRO = B.idMEMBRO
            WHERE A.DATA BETWEEN %s AND %s
            ORDER BY A.DATA
        """
        cursor.execute(consulta, (data_inicio, data_fim))
        dados = cursor.fetchall()

        total_query = """
            SELECT SUM(VALOR)
            FROM contribuicao A
            INNER JOIN membro B ON A.MEMBRO_idMEMBRO = B.idMEMBRO
            WHERE A.DATA BETWEEN %s AND %s
        """
        cursor.execute(total_query, (data_inicio, data_fim))
        total = cursor.fetchone()

        return dados, total
    except Exception as e:
        print(f"Erro no relatório analítico: {str(e)}")
        return [], (0,)
    finally:
        cursor.close()
        conn.close()
