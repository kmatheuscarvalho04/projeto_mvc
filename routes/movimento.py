from flask import Blueprint, render_template, request, redirect, url_for, flash
from projeto_mvc.models import contribuicao

bp_mov = Blueprint('movimento', __name__)

@bp_mov.route('/vis_movimento')
def vis_movimento():
    dados = contribuicao.listar_contribuicoes()
    return render_template('vis_movimento.html', dados=dados)

@bp_mov.route('/ins_movimento')
def ins_movimento():
    dados = contribuicao.listar_membros()
    return render_template('ins_movimento.html', dados=dados)

@bp_mov.route('/ins_mov_diz', methods=['POST'])
def ins_mov_diz():
    sucesso, mensagem = contribuicao.inserir_contribuicao(request.form)
    flash(mensagem)
    if sucesso:
        return redirect(url_for('movimento.vis_movimento'))
    else:
        return redirect(url_for('movimento.ins_movimento'))
