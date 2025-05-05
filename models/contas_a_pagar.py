from projeto_mvc.models.db import obter_conexao

def inserir_conta(form):
    num_titulo = form.get('num_titulo')
    recebedor = form.get('recebedor')
    historico = form.get('historico')
    emissao = form.get('emissao')
    vencimento = form.get('vencimento')
    valor = form.get('valor')

    conn = obter_conexao()
    cursor = conn.cursor()
    try:
        query = """
            INSERT INTO contas_a_pg (num_titulo, recebedor, hist, emissao, vencimento, valor)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (num_titulo, recebedor, historico, emissao, vencimento, valor))
        conn.commit()
        return True, "Conta a pagar inserida com sucesso!"
    except Exception as e:
        conn.rollback()
        return False, f"Erro ao inserir conta a pagar: {str(e)}"
    finally:
        cursor.close()
        conn.close()
