from projeto_mvc.models.db import obter_conexao


def listar_usuarios():
    conn = obter_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT idUSER, login, email FROM usuario")
        return cursor.fetchall()
    except Exception as e:
        print(f"Erro ao buscar usuarios: {str(e)}")
        return []
    finally:
        cursor.close()
        conn.close()