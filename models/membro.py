from projeto_mvc.models.db import obter_conexao

def listar_membros():
    conn = obter_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT idMEMBRO, RI, CARGO, NOME, TELEFONE FROM membro")
        return cursor.fetchall()
    except Exception as e:
        print(f"Erro ao buscar membros: {str(e)}")
        return []
    finally:
        cursor.close()
        conn.close()

# ==================================================================

def inserir_membro(form):
    cargo = form.get('cargo')
    nome = form.get('nome')
    ri = form.get('ri')
    telefone = form.get('telefone')

    conn = obter_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO membro (CARGO, NOME, RI, TELEFONE) VALUES (%s, %s, %s, %s)", 
                       (cargo, nome, ri, telefone))
        conn.commit()
        return True, "Registro inserido com sucesso!"
    except Exception as e:
        conn.rollback()
        return False, f"Erro ao inserir o registro: {str(e)}"
    finally:
        cursor.close()
        conn.close()

# ==================================================================

def alterar_membro(form):
    id_ou_ri = form.get('id_ou_ri')
    campo = form.get('campo')
    conteudo = form.get('conteudo')

    conn = obter_conexao()
    cursor = conn.cursor()
    try:
        comando = f'UPDATE membro SET {campo} = %s WHERE idMEMBRO = %s OR RI = %s'
        cursor.execute(comando,(conteudo,id_ou_ri,id_ou_ri))
        conn.commit()
        return True, "Registro alterado com sucesso!"
    except Exception as e:
        conn.rollback()
        return False, f"Erro ao alterar o registro: {str(e)}"
    finally:
        cursor.close()
        conn.close()

# ==================================================================

def excluir_membro(form):
    id_ou_ri = form.get('id_ou_ri')
    # exclusao = form.get('exclusao')

    conn = obter_conexao()
    cursor = conn.cursor()

    try: 
        comando = f'DELETE FROM membro WHERE idMEMBRO = %s OR RI = %s'
        cursor.execute(comando,(id_ou_ri,id_ou_ri))
        conn.commit()
        return True, "Registro excluido com sucesso!"
    except Exception as e:
        conn.rollback()
        return False, f"Erro ao excluir o registro: {str(e)}"
    finally:
        cursor.close()
        conn.close()