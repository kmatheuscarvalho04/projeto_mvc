from projeto_mvc.models.db import obter_conexao

def relatorio_sintetico(mes_relatorio):
    conn = obter_conexao()
    cursor = conn.cursor()

    ano = mes_relatorio[:4]
    mes = mes_relatorio[-2:]
    try:
        consulta = """
            SELECT DISTINCT B.NOME, B.CARGO, B.RI
            FROM contribuicao A
            INNER JOIN membro B ON A.MEMBRO_idMEMBRO = B.idMEMBRO
            WHERE A.DATA LIKE %s
            ORDER BY CARGO DESC
        """

        parametro = (f"{ano}-{mes}%",)  # Ex: ('202505%',)
        cursor.execute(consulta, parametro)
        return cursor.fetchall()
    except Exception as e:
        print(f"Erro no relatório sintético: {str(e)}")
        return []
    finally:
        cursor.close()
        conn.close()

def relatorio_analitico(mes_relatorio):
    conn = obter_conexao()
    cursor = conn.cursor()

    ano = mes_relatorio[:4]
    mes = mes_relatorio[-2:]
    try:
        consulta = """
            SELECT A.DATA, B.CARGO, B.NOME, A.VALOR, B.RI
            FROM contribuicao A
            INNER JOIN membro B ON A.MEMBRO_idMEMBRO = B.idMEMBRO
            WHERE A.DATA LIKE %s
            ORDER BY A.DATA
        """
        parametro = (f"{ano}-{mes}%",)  # Ex: ('202505%',)
        cursor.execute(consulta, parametro)
        dados = cursor.fetchall()

        total_query = """
            SELECT SUM(A.VALOR)
            FROM contribuicao A
            INNER JOIN membro B ON A.MEMBRO_idMEMBRO = B.idMEMBRO
            WHERE A.DATA LIKE %s
        """
        
        cursor.execute(total_query, parametro)
        total = cursor.fetchall()

        return dados, total
    except Exception as e:
        print(f"Erro no relatório analítico: {str(e)}")
        return [], (0,)
    finally:
        cursor.close()
        conn.close()

# Remova o trecho abaixo deste arquivo!
# dados, total = relatorio_analitico(mes_relatorio)
# return render_template(
#     'relatorio/vis_analitico.html',
#     dados=dados,
#     total=total[0] if total and total[0] is not None else 0
# )
