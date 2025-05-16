from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import contribuicao, membro

bp_contribuicao = Blueprint('contribuicao', __name__)

@bp_contribuicao.route('/ins_movimento', methods=['GET', 'POST'])
def inserir():
    if request.method == 'POST':
        contribuicao.inserir_contribuicao(
            request.form['id_dizimista'],
            request.form['data'],
            request.form['valor']
        )
        flash("Movimento inserido com sucesso!")
        return redirect(url_for('contribuicao.visualizar'))
    membros = membro.listar_membros()
    return render_template('movimento/ins_movimento.html', dados=membros)


@bp_contribuicao.route('/filtragem', methods=['POST'])
def filtrar_movimentos():
    data_inicio = request.form.get('data_movimento_inicio')
    data_fim = request.form.get('data_movimento_fim')
    
    dados_filtrados = contribuicao.listar_contribuicoes(data_inicio, data_fim)
    return render_template('movimento/vis_movimento.html', dados=dados_filtrados)