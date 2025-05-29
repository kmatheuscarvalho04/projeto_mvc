from flask import Blueprint, render_template, request, redirect, url_for, flash
from projeto_mvc.models import contribuicao

bp_mov = Blueprint('movimento', __name__)

@bp_mov.route('/fil_movimento', methods=['GET','POST'])
def fil_movimento():
    dados = contribuicao.listar_contribuicoes()
    return render_template('movimento/filtro_movimento.html', dados = dados)

@bp_mov.route('/filtragem', methods=['POST'])
def filtrar_movimentos():
    data_inicio = request.form.get('data_movimento_inicio')
    data_fim = request.form.get('data_movimento_fim')
    
    dados_filtrados = contribuicao.listar_contribuicoes(data_inicio, data_fim)

    return render_template('movimento/vis_movimento.html', dados=dados_filtrados)

@bp_mov.route('/ins_movimento', methods=['GET','POST'])
def ins_movimento():
    dados = contribuicao.listar_membros()
    return render_template('movimento/ins_movimento.html', dados=dados)

@bp_mov.route('/ins_mov_diz', methods=['POST'])
def ins_mov_diz():
    sucesso, mensagem = contribuicao.inserir_contribuicao(request.form)
    flash(mensagem)
    if sucesso:
        return redirect(url_for('movimento.vis_movimento'))
    else:
        return redirect(url_for('movimento.ins_movimento'))


@bp_mov.route('/vis_movimento', methods=['GET'])
def vis_movimento():
    dados = contribuicao.listar_contribuicoes()
    return render_template('movimento/vis_movimento.html', dados=dados)

@bp_mov.route('/alterarmov/<id_movimento>')
def rota_alterarmov(id_movimento):
    return render_template('movimento/alt_movimento.html', id_movimento=id_movimento)

@bp_mov.route('/exc_movimento', methods=['GET','POST'])
def exc_movimento():
    sucesso, mensagem = contribuicao.excluir_movimentacao(request.form)
    flash(mensagem)
    if sucesso:
        return redirect(url_for('movimento.vis_movimento'))
    else:
        return redirect(url_for('movimento.alt_movimento'))
