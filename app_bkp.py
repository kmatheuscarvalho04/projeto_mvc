from flask import Flask, render_template, request, redirect, session, url_for, flash, send_file
import pyodbc
import mysql.connector
# from IPython.display import display
# from openpyxl import load_workbook, workbook, worksheet
# from datetime import date
##---------------------------------------------------------------------------------------------------------------------

import mysql.connector

def obter_conexao():
    host = '127.0.0.1'
    database = 'mydb'
    username = 'root'
    password = ''
    
    conexao = mysql.connector.connect(
        host=host,
        database=database,
        user=username,
        password=password
    )
    
    return conexao

##--------------------------------------------------------------------------------------------------------------------
#pagina principal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TESTE'

@app.route('/', methods=['POST','GET'])
def inicio():
    session.setdefault('menu_expandido', False)
    return render_template('index.html',menu_expandido=session['menu_expandido'])

##--------------------------------------------------------------------------------------------------------------------
### Menu onde aparece as opções

@app.route('/menu')
def menu():
    return render_template ('menu.html',menu_expandido=session['menu_expandido'])

@app.route('/toggle_menu', methods=['POST'])
def toggle_menu():
    session['menu_expandido'] = not session.get('menu_expandido',False)
    return '', 204 # Retorna sem conteúdo, só atualiza o estado


##--------------------------------------------------------------------------------------------------------------------

##visualizar dizimista

@app.route('/vis_dizimista', methods=['POST','GET'])
def vis_dizimista():
    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM DIZIMISTA")
        dados = cursor.fetchall()

    except Exception as e:
        mensagem = "erro ao visualizar registro"
        return mensagem

    finally:
        cursor.close()
        conn.close() 

    return render_template ('vis_dizimista.html', dados=dados)


##--------------------------------------------------------------------------------------------------------------------
#ins_dizimista
@app.route('/ins_dizimista', methods=['POST'])
def ins_diz():
        
    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM DIZIMISTA")
        dados = cursor.fetchall()

    except Exception as e:
        mensagem = "erro ao visualizar registro"
        return mensagem

    finally:
        cursor.close()
        conn.close() 

    return render_template ('ins_dizimista.html', dados=dados)

##--------------------------------------------------------------------------------------------------------------------

@app.route('/inserir', methods=['POST'])
def inserir_dados():
    cargo = request.form['cargo']
    nome = request.form['nome']
    id = request.form['id']

    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO DIZIMISTA (CARGO,NOME,RI) VALUES (?,?,?)", cargo,nome,id)
        conn.commit()
        flash("Registro inserido com sucesso!")
        return redirect(url_for('vis_dizimista'))
    
    except Exception as e:
        conn.rollback()
        mensagem =f"Erro ao inserir o registro: {str(e)}"

    finally:
        cursor.close()
        conn.close()

    return mensagem

##--------------------------------------------------------------------------------------------------------------------
#excluir dizimista

@app.route('/exc_dizimista', methods=['POST'])
def exc_diz():
        
    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM DIZIMISTA")
        dados = cursor.fetchall()

    except Exception as e:
        mensagem = "erro ao visualizar registro"
        return mensagem

    finally:
        cursor.close()
        conn.close() 

    return render_template ('exc_dizimista.html', dados=dados)

##================================================================
@app.route('/exclusao', methods=['POST'])

def exc_dizimista():
    exclusao = request.form['exclusao']
    conn = obter_conexao()
    cursor = conn.cursor()
    dizimista = 'DIZIMISTA'

    try:
        comando =f'DELETE FROM {dizimista} WHERE ID = ? OR RI = ?'
        cursor.execute(comando,(exclusao,exclusao))
        conn.commit()
        flash("Registro excluído com sucesso!")
        return redirect(url_for('vis_dizimista'))
    

    except Exception as e:
        mensagem = f"Erro ao excluir o registro: {str(e)}"        

    finally:
        cursor.close()
        conn.close() 

    return mensagem

##--------------------------------------------------------------------------------------------------------------------
@app.route('/alt_dizimista', methods=['POST'])
def alt_diz():
        
    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM DIZIMISTA")
        dados = cursor.fetchall()

    except Exception as e:
        mensagem = "erro ao visualizar registro"
        return mensagem

    finally:
        cursor.close()
        conn.close() 

    return render_template ('alt_dizimista.html', dados=dados)

#==============================================================
@app.route('/alteracao', methods=['POST'])
def alteracao():
    id_ou_ri = request.form['id_ou_ri']
    campo = request.form['campo']
    alteracao = request.form['alteracao']


    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        comando = f'UPDATE DIZIMISTA SET {campo} = ? WHERE ID = ? OR RI = ?'
        cursor.execute(comando,(alteracao,id_ou_ri,id_ou_ri))
        conn.commit()
        flash("Registro atualizado com sucesso!")
        return redirect(url_for('vis_dizimista'))
    

    except Exception as e:
        mensagem = f"Erro ao atualizar o registro: {str(e)}"        

    finally:
        cursor.close()
        conn.close() 

    return mensagem

##--------------------------------------------------------------------------------------------------------------------
#visualizar movimento (contribuição)

@app.route('/vis_movimento', methods=['POST','GET'])
def vis_movimento():
        
    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT A.ID, A.VALOR, A.DATA, A.ID_DIZIMISTA, B.NOME FROM CONTRIBUICAO A INNER JOIN DIZIMISTA B ON B.ID = A.ID_DIZIMISTA ")
        dados = cursor.fetchall()

    except Exception as e:
        mensagem = "erro ao visualizar registro"
        return mensagem

    finally:
        cursor.close()
        conn.close() 
    return render_template ('vis_movimento.html', dados=dados)
##--------------------------------------------------------------------------------------------------------------------
#inserir movimento (contribuição)

@app.route('/ins_movimento', methods=['POST','GET'])
def ins_movimento():
        
    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM DIZIMISTA")
        dados = cursor.fetchall()

    except Exception as e:
        mensagem = "erro ao visualizar registro"
        return mensagem

    finally:
        cursor.close()
        conn.close() 
    return render_template ('ins_movimento.html', dados=dados)
##--------------------------------------------------------------------------------------------------------------------
@app.route('/ins_mov_diz', methods=['POST'])
def ins_mov_diz():
    id_dizimista = request.form['id_dizimista']
    data = request.form['data']
    valor = request.form['valor']

    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        comando = f'INSERT INTO CONTRIBUICAO (ID_DIZIMISTA,DATA,VALOR) VALUES (?,?,?)'
        cursor.execute(comando,id_dizimista,data,valor)
        conn.commit()
        flash("Registro inserido com sucesso!")
        return redirect(url_for('ins_movimento'))
    

    except Exception as e:
        mensagem = f"Erro ao atualizar o registro: {str(e)}"        

    finally:
        cursor.close()
        conn.close() 

    return mensagem

##--------------------------------------------------------------------------------------------------------------------
#Alteração de movimento
@app.route('/alt_movimento', methods=['POST','GET'])
def alt_movimento():
        
    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT A.ID, A.VALOR, A.DATA, A.ID_DIZIMISTA, B.NOME FROM CONTRIBUICAO A INNER JOIN DIZIMISTA B ON B.ID = A.ID_DIZIMISTA ")
        dados = cursor.fetchall()

    except Exception as e:
        mensagem = f"erro ao visualizar registro: {str(e)}"  
        return mensagem

    finally:
        cursor.close()
        conn.close() 

    return render_template ('alt_movimento.html', dados=dados)
##--------------------------------------------------------------------------------------------------------------------

#Filtrando por mês na alteração de movimento

@app.route('/alteracao_mov', methods=['POST'])
def alteracao_mov():

    mes_movimento = request.form['mes_movimento']
        
    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        consulta = f"SELECT A.ID, A.VALOR, A.DATA, A.ID_DIZIMISTA, B.NOME FROM CONTRIBUICAO A INNER JOIN DIZIMISTA B ON B.ID = A.ID_DIZIMISTA WHERE A.DATA LIKE ? "
        cursor.execute(consulta,f'%{mes_movimento}%')
        dados = cursor.fetchall()

    except Exception as e:
        mensagem = f"erro ao visualizar registro: {str(e)}"  
        return mensagem

    finally:
        cursor.close()
        conn.close() 

    return render_template ('alt_movimento2.html', dados=dados)

##--------------------------------------------------------------------------------------------------------------------

@app.route('/alteracao_mov2', methods=['POST'])
def alteracao_mov2():

    id_movimento = request.form['id_movimento']
    campo_mov = request.form['campo_mov']
    atual_campo_mov = request.form['atual_campo_mov']
        
    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        consulta = f"UPDATE CONTRIBUICAO SET {campo_mov} = ? WHERE ID = ?"
        cursor.execute(consulta,atual_campo_mov,id_movimento)
        conn.commit()
        flash("Registro atualizado com sucesso!")
        return redirect(url_for('vis_movimento'))
    
    except Exception as e:
        mensagem = f"erro ao visualizar registro: {str(e)}"  

    finally:
        cursor.close()
        conn.close() 

    return mensagem
##--------------------------------------------------------------------------------------------------------------------
##acessar rotima para excluir movimento

@app.route('/exc_movimento', methods=['POST','GET'])
def exc_movimento():
        
    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT A.ID, A.VALOR, A.DATA, A.ID_DIZIMISTA, B.NOME FROM CONTRIBUICAO A INNER JOIN DIZIMISTA B ON B.ID = A.ID_DIZIMISTA ")
        dados = cursor.fetchall()

    except Exception as e:
        mensagem = f"erro ao visualizar registro: {str(e)}"  
        return mensagem

    finally:
        cursor.close()
        conn.close() 

    return render_template ('exc_movimento.html', dados=dados)

##--------------------------------------------------------------------------------------------------------------------
## filtrar para excluir movimento

@app.route('/exclusao_mov', methods=['POST','GET'])
def exclusao_mov():
   
    mes_exclusao = request.form['mes_exclusao']
        
    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        consulta = f"SELECT A.ID, A.VALOR, A.DATA, A.ID_DIZIMISTA, B.NOME FROM CONTRIBUICAO A INNER JOIN DIZIMISTA B ON B.ID = A.ID_DIZIMISTA WHERE A.DATA LIKE ? "
        cursor.execute(consulta,f'%{mes_exclusao}%')
        dados = cursor.fetchall()

    except Exception as e:
        mensagem = f"erro ao visualizar registro: {str(e)}"  
        return mensagem

    finally:
        cursor.close()
        conn.close() 

    return render_template ('exc_movimento2.html', dados=dados)

##--------------------------------------------------------------------------------------------------------------------
## excluir movimento

@app.route('/exclusao_mov2', methods=['POST','GET'])
def exclusao_mov2():
   
    exclusao_id_mov = request.form['exclusao_id_mov']
        
    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        consulta = f"DELETE FROM CONTRIBUICAO WHERE ID = ? "
        cursor.execute(consulta,exclusao_id_mov)
        conn.commit()
        flash("Registro excluído com sucesso!")
        return redirect(url_for('vis_movimento'))
    
    except Exception as e:
        mensagem = f"Erro ao excluir o registro: {str(e)}"        

    finally:
        cursor.close()
        conn.close() 

    return mensagem



##--------------------------------------------------------------------------------------------------------------------

#Geração do relatório
@app.route('/gerar_relatorio', methods=['POST'])
def gerar_relatorio():
    return render_template('gerar_relatorio.html')

##--------------------------------------------------------------------------------------------------------------------

# Gerando o relatório pedindo as opcoes
@app.route('/relatorio', methods=['POST','GET'])
def relatorio():
    de_data = request.form['de_data']
    strde = de_data.replace("-","")
    para_data = request.form['para_data']
    strpara = para_data.replace("-","")
    tipo_relatorio = request.form['tipo_relatorio']

    conn = obter_conexao()
    cursor = conn.cursor()

    if tipo_relatorio == 'SINTÉTICO':
        

        try:
            consulta = f"SELECT DISTINCT NOME, CARGO, RI FROM CONTRIBUICAO A INNER JOIN DIZIMISTA B ON A.ID_DIZIMISTA = B.ID WHERE A.DATA BETWEEN ? AND ? ORDER BY CARGO DESC"
            cursor.execute(consulta, [f'{strde}', f'{strpara}'])            
            dados = cursor.fetchall()

        except Exception as e:
            mensagem = "erro ao visualizar registro"
            return mensagem

        finally:
            cursor.close()
            conn.close() 
        return render_template ('vis_sintetico.html', dados=dados)
        
    
    else:
        if tipo_relatorio == 'ANALÍTICO':
        
            try:
                consulta1 = f"SELECT CONVERT(varchar(10),DATA,103) AS DATA,CARGO,NOME,VALOR, RI FROM CONTRIBUICAO A INNER JOIN DIZIMISTA B ON A.ID_DIZIMISTA = B.ID WHERE A.DATA BETWEEN ? AND ? ORDER BY DATA"
                cursor.execute(consulta1, [f'{strde}', f'{strpara}'])            
                dados = cursor.fetchall()

                total_consulta = "SELECT SUM(VALOR) TOTAL FROM CONTRIBUICAO A INNER JOIN DIZIMISTA B ON A.ID_DIZIMISTA = B.ID WHERE A.DATA BETWEEN ? AND ?"
                cursor.execute(total_consulta, [f'{strde}', f'{strpara}'])
                dados_totalconsult = cursor.fetchall()

            except Exception as e:
                mensagem = "erro ao visualizar registro"
                return mensagem

            finally:
                cursor.close()
                conn.close() 
            return render_template ('vis_analitico.html', dados=dados, dados_totalconsult = dados_totalconsult )
        

    


##--------------------------------------------------------------------------------------------------------------------

# Tela de contas a pagar:
@app.route('/contas_a_pagar', methods=['POST','GET'])
def contas_a_pagar():
    return render_template('contas_a_pagar.html')




##--------------------------------------------------------------------------------------------------------------------

#Inserir Contas a Pagar


@app.route('/inserir_ctas_pagar', methods =['GET','POST'])
def inserir_ctas_pagar():
    num_titulo = request.form['num_titulo']
    recebedor = request.form['recebedor']
    historico = request.form['historico']
    emissao = request.form['emissao']
    vencimento = request.form['vencimento']
    valor = request.form['valor']
    # saldo = request.form['saldo']           
           
    conn = obter_conexao()
    cursor = conn.cursor()


    try:
        consulta = f"INSERT INTO CONTAS_A_PG (NUMTITULO,RECEBEDOR,HIST,EMISSAO,VENCIMENTO,VALOR) VALUES (?,?,?,?,?,?)"
        cursor.execute(consulta,num_titulo,recebedor,historico,emissao,vencimento,valor)
        conn.commit()
        flash("Registro incluído com sucesso com sucesso!")
        return redirect(url_for('vis_movimento'))
    
    except Exception as e:
        mensagem = f"Erro ao incluir o registro: {str(e)}"        

    finally:
        cursor.close()
        conn.close() 

    return mensagem


if __name__ == '__main__':
    app.run(debug=True)